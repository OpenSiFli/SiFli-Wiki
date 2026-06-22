from __future__ import annotations

import argparse
import os
from concurrent.futures import ProcessPoolExecutor
from dataclasses import dataclass
from pathlib import Path
from tempfile import NamedTemporaryFile

from PIL import Image


@dataclass
class OptimizeResult:
    scanned: int = 0
    optimized: int = 0
    skipped: int = 0
    failed: int = 0
    original_bytes: int = 0
    optimized_bytes: int = 0

    @property
    def saved_bytes(self) -> int:
        return self.original_bytes - self.optimized_bytes


def iter_png_files(paths: list[Path]):
    for root in paths:
        if root.is_file() and root.suffix.lower() == ".png":
            yield root
        elif root.is_dir():
            yield from root.rglob("*.png")


def rendered_rgba_bytes(path: Path) -> tuple[tuple[int, int], bytes]:
    with Image.open(path) as image:
        image.load()
        return image.size, image.convert("RGBA").tobytes()


def images_match(original_path: Path, optimized_path: Path) -> bool:
    original_size, original_pixels = rendered_rgba_bytes(original_path)
    optimized_size, optimized_pixels = rendered_rgba_bytes(optimized_path)
    return original_size == optimized_size and original_pixels == optimized_pixels


def optimize_png(path: Path) -> tuple[bool, int, int, str | None]:
    original_size = path.stat().st_size

    try:
        with Image.open(path) as image:
            if getattr(image, "is_animated", False):
                return False, original_size, original_size, "animated PNG skipped"

            image.load()
            with NamedTemporaryFile(delete=False, suffix=".png", dir=path.parent) as temp_file:
                temp_path = Path(temp_file.name)

            try:
                image.save(temp_path, format="PNG", optimize=True, compress_level=9)
                optimized_size = temp_path.stat().st_size

                if optimized_size >= original_size:
                    temp_path.unlink(missing_ok=True)
                    return False, original_size, original_size, None

                if not images_match(path, temp_path):
                    temp_path.unlink(missing_ok=True)
                    return False, original_size, original_size, "pixel verification failed"

                temp_path.replace(path)
                return True, original_size, optimized_size, None
            except Exception:
                temp_path.unlink(missing_ok=True)
                raise
    except Exception as exc:
        return False, original_size, original_size, str(exc)


def optimize_png_with_path(path: Path) -> tuple[Path, bool, int, int, str | None]:
    optimized, original_size, optimized_size, error = optimize_png(path)
    return path, optimized, original_size, optimized_size, error


def default_jobs() -> int:
    return max(1, min(os.cpu_count() or 1, 4))


def update_result(
    result: OptimizeResult,
    path: Path,
    optimized: bool,
    original_size: int,
    optimized_size: int,
    error: str | None,
    verbose: bool,
) -> None:
    result.scanned += 1
    result.original_bytes += original_size
    result.optimized_bytes += optimized_size

    if error:
        result.failed += 1
        print(f"Warning: {path}: {error}")
    elif optimized:
        result.optimized += 1
        if verbose:
            saved = original_size - optimized_size
            print(f"Optimized {path}: saved {saved} bytes")
    else:
        result.skipped += 1


def optimize_images(paths: list[Path], verbose: bool, jobs: int) -> OptimizeResult:
    result = OptimizeResult()
    png_files = list(iter_png_files(paths))

    if jobs == 1 or len(png_files) <= 1:
        for path in png_files:
            optimized, original_size, optimized_size, error = optimize_png(path)
            update_result(result, path, optimized, original_size, optimized_size, error, verbose)
        return result

    with ProcessPoolExecutor(max_workers=jobs) as executor:
        for path, optimized, original_size, optimized_size, error in executor.map(optimize_png_with_path, png_files):
            update_result(result, path, optimized, original_size, optimized_size, error, verbose)

    return result


def format_size(size: int) -> str:
    return f"{size / 1024 / 1024:.2f} MiB"


def main() -> int:
    parser = argparse.ArgumentParser(description="Losslessly optimize PNG images in build output.")
    parser.add_argument("paths", nargs="+", type=Path, help="Files or directories to scan")
    parser.add_argument("--verbose", action="store_true", help="Print each optimized image")
    parser.add_argument(
        "--jobs",
        type=int,
        default=default_jobs(),
        help="Number of worker processes to use. Defaults to min(CPU count, 4). Use 1 for serial mode.",
    )
    args = parser.parse_args()

    if args.jobs < 1:
        print("Error: --jobs must be at least 1")
        return 2

    missing_paths = [path for path in args.paths if not path.exists()]
    if missing_paths:
        for path in missing_paths:
            print(f"Error: path does not exist: {path}")
        return 2

    result = optimize_images(args.paths, args.verbose, args.jobs)
    print(
        "PNG optimization summary: "
        f"jobs={args.jobs}, scanned={result.scanned}, optimized={result.optimized}, "
        f"skipped={result.skipped}, failed={result.failed}, "
        f"before={format_size(result.original_bytes)}, "
        f"after={format_size(result.optimized_bytes)}, "
        f"saved={format_size(result.saved_bytes)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
