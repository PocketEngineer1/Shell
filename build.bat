@ECHO OFF
pyinstaller main.py
mkdir "%CD%\dist\main\lang"
xcopy /s "%CD%\lang" "%CD%\dist\main\lang"