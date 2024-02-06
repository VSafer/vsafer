@echo off

SET "PROJECTDIR=%~dp0.."
SET "ASSETSDIR=%PROJECTDIR%\assets"
echo %ASSETSDIR%

pyinstaller.exe ^
 --noconfirm ^
 --log-level=WARN ^
 --uac-admin ^
 --onefile ^
 --windowed ^
 --add-data "%ASSETSDIR%\icon.png;." ^
 --icon "%ASSETSDIR%\icon.ico" ^
 %PROJECTDIR%\vsafer\main.py
