# 3 KEIL
## 3.1 Modify the Configuration File
The scons --target=mdk5 command generates the current project based on the project under sdk\tools\build\template\template.uvprojx.<br>
For the uvprojx project, after opening template.uvprojx in keil, modifying it, saving it, and exiting, the default result of the next scons --target=mdk5 command will follow the modifications made to the template.uvprojx project.<br>
Using it correctly can reduce repeated work and improve efficiency.<br>
Recommended modification 1:<br>
![alt text](./assets/keil001.png)<br> 
Recommended modification 2:<br>
Customize batch operations before and after compilation. Common operations include<br>
1) Copying lcpu_img.c in the prebuil.bat batch file,<br>
2) Disassemble the axf file into an asm assembly file,<br>
![alt text](./assets/keil002.png)<br>
