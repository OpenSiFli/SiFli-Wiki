#!/usr/bin/env python3
"""
PR管理脚本
用于创建和管理自动翻译的Pull Request
"""

import os
import subprocess
import json
import argparse
from datetime import datetime

class PRManager:
    def __init__(self, repo_owner="OpenSiFli", repo_name="SiFli-Wiki"):
        self.repo_owner = repo_owner
        self.repo_name = repo_name
        self.github_token = os.getenv('GITHUB_TOKEN')
        
    def create_pr_with_gh_cli(self, source_branch, target_branch, title, body):
        """使用GitHub CLI创建PR"""
        try:
            cmd = [
                "gh", "pr", "create",
                "--title", title,
                "--body", body,
                "--base", target_branch,
                "--head", source_branch,
                "--label", "🤖 auto-translation,📚 documentation"
            ]
            
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            pr_url = result.stdout.strip()
            print(f"PR创建成功: {pr_url}")
            return pr_url
            
        except subprocess.CalledProcessError as e:
            print(f"创建PR失败: {e}")
            print(f"错误输出: {e.stderr}")
            return None

    def generate_pr_title(self, source_branch, target_branch, lang_direction):
        """生成PR标题"""
        timestamp = datetime.now().strftime("%Y%m%d-%H%M")
        direction_map = {
            "en": "中文 → 英文",
            "zh": "英文 → 中文"
        }
        direction = direction_map.get(lang_direction, "自动翻译")
        
        return f"🤖 自动翻译 ({direction}) - {timestamp}"

    def generate_pr_body(self, source_branch, target_branch, lang_direction, changed_files=[]):
        """生成PR描述"""
        direction_map = {
            "en": "中文 → 英文",
            "zh": "英文 → 中文"
        }
        direction = direction_map.get(lang_direction, "自动翻译")
        
        body = f"""## 🤖 自动翻译 PR

此PR由GitHub Actions自动生成，包含文档的自动翻译更新。

### 📋 翻译信息
- **源分支**: `{source_branch}`
- **目标分支**: `{target_branch}`
- **翻译方向**: {direction}
- **更新时间**: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

### 📝 更改文件"""

        if changed_files:
            body += f" ({len(changed_files)} 个文件)\n"
            for file in changed_files:
                body += f"- `{file}`\n"
        else:
            body += "\n自动检测的变更文件将在此显示\n"

        body += """
### ⚠️ 审查要点
请仔细审查以下内容：
- [ ] 技术术语翻译准确性
- [ ] 代码示例和API引用保持不变
- [ ] reStructuredText格式正确
- [ ] 链接和图片引用有效
- [ ] 整体语言表达自然流畅

### 🔧 使用的工具
- **翻译引擎**: Qwen/Qwen2.5-72B-Instruct (SiliconFlow API)
- **翻译脚本**: `auto_translation.py`
- **触发方式**: GitHub Actions

### 📚 相关文档
- [翻译规范](docs/translation-guide.md)
- [文档贡献指南](CONTRIBUTING.md)

---
*此PR由 [auto-translation workflow](.github/workflows/auto-translation.yml) 自动创建*
"""
        return body

    def check_existing_pr(self, source_branch, target_branch):
        """检查是否已存在相同的PR"""
        try:
            cmd = [
                "gh", "pr", "list",
                "--base", target_branch,
                "--head", source_branch,
                "--json", "number,title,state"
            ]
            
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            prs = json.loads(result.stdout)
            
            open_prs = [pr for pr in prs if pr['state'] == 'OPEN']
            return open_prs
            
        except subprocess.CalledProcessError as e:
            print(f"检查现有PR失败: {e}")
            return []

    def update_existing_pr(self, pr_number, title, body):
        """更新现有PR"""
        try:
            cmd = [
                "gh", "pr", "edit", str(pr_number),
                "--title", title,
                "--body", body
            ]
            
            subprocess.run(cmd, check=True)
            print(f"已更新PR #{pr_number}")
            return True
            
        except subprocess.CalledProcessError as e:
            print(f"更新PR失败: {e}")
            return False

    def create_or_update_pr(self, source_branch, target_branch, lang_direction, changed_files=[]):
        """创建或更新PR"""
        title = self.generate_pr_title(source_branch, target_branch, lang_direction)
        body = self.generate_pr_body(source_branch, target_branch, lang_direction, changed_files)
        
        # 检查是否已存在PR
        existing_prs = self.check_existing_pr(source_branch, target_branch)
        
        if existing_prs:
            # 更新现有PR
            pr_number = existing_prs[0]['number']
            print(f"发现现有PR #{pr_number}，正在更新...")
            return self.update_existing_pr(pr_number, title, body)
        else:
            # 创建新PR
            print("创建新的PR...")
            return self.create_pr_with_gh_cli(source_branch, target_branch, title, body)

def main():
    parser = argparse.ArgumentParser(description='PR管理工具')
    parser.add_argument('--source-branch', required=True, help='源分支')
    parser.add_argument('--target-branch', required=True, help='目标分支')
    parser.add_argument('--lang-direction', required=True, choices=['en', 'zh'], help='翻译方向')
    parser.add_argument('--changed-files', nargs='*', help='变更的文件列表')
    
    args = parser.parse_args()
    
    pr_manager = PRManager()
    result = pr_manager.create_or_update_pr(
        args.source_branch,
        args.target_branch,
        args.lang_direction,
        args.changed_files or []
    )
    
    if result:
        print("PR操作成功完成")
    else:
        print("PR操作失败")
        exit(1)

if __name__ == "__main__":
    main()
