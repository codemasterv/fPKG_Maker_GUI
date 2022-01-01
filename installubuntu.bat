@ECHO off
wsl --install -d Ubuntu-20.04
%USERPROFILE%\AppData\Local\Microsoft\WindowsApps\ubuntu2004.exe run -e sudo apt install dos2unix -y 
%USERPROFILE%\AppData\Local\Microsoft\WindowsApps\ubuntu2004.exe run -e sudo apt install wget -y

