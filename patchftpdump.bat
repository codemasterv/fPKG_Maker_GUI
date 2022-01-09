@ECHO off
%USERPROFILE%\AppData\Local\Microsoft\WindowsApps\ubuntu2004.exe run -e --shutdown
%USERPROFILE%\AppData\Local\Microsoft\WindowsApps\ubuntu2004.exe run -e dos2unix yourftpdump
%USERPROFILE%\AppData\Local\Microsoft\WindowsApps\ubuntu2004.exe run -e ./yourftpdump -p %*