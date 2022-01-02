@ECHO off
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
%USERPROFILE%\AppData\Local\Programs\Python\Python310\python.exe get-pip.py
py -m pip install --upgrade pip
py -m pip install bs4 lxml requests
Py -m pip install beautifulsoup4 lxml requests