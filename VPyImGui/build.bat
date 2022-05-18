set EXE=%~dp0\main.py
set Python38Scripts=D:\Python\3.8\Scripts
set path=%Python38Scripts%;%path%
pyinstaller --onefile %EXE%

::to overwrite the file without any prompt.
xcopy %~dp0\Dlls\*.* %~dp0\dist\. /Y