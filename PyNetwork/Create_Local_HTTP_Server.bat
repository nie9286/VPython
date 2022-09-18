@echo off

rem 127.0.0.1:8000

:launch_server
echo Python deteced!

cd S:\Solarland\Singularity_staging-unity-v12.1
if not exist LocalSolarlandCDN\ md LocalSolarlandCDN\
cd LocalSolarlandCDN
C:\Python\37\python.exe -m http.server

