@ECHO off
wsl --install -d Ubuntu-20.04
%HOMEPATH%\AppData\Local\Microsoft\WindowsApps\ubuntu2004.exe run -e sudo apt install dos2unix -y 
%HOMEPATH%\AppData\Local\Microsoft\WindowsApps\ubuntu2004.exe run -e sudo apt install wget -y
%HOMEPATH%\AppData\Local\Microsoft\WindowsApps\ubuntu2004.exe run -e sudo apt install curl -y