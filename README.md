 # You need to be on Windows 10 or Preferably Windows 11 with its more simplified Windows Subsystem Linux. 
 
 # Windows 8.1, Windows 8 and Windows 7 will not work with this tool.

![alt text](https://github.com/codemasterv/fPKG_Maker_GUI/blob/master/Capture.PNG?raw=true)

# All fields need to be filled out before the patch will build properly, Meaning fill out the base game information first before trying to build the patch for the base game.

# If not insalled already, Be sure to install WSL2 Ubuntu 20.04 via the button in the bottom left corner of the program. This program requires that version!

# Updating the ftpdump script from hippie68

if you do want to use a new ftpdump script from hippie68, all you have to do is replace the ftpdump file in the same folder as the _fPKG_Maker_GUI.exe. Edit it and add two spaces after the

ip=

and add the port you want to use. 

port=2121

the program will make a copy of ftpdump named yourftpdump. it keeps the ftpdump persistent for updates to his script.

# ###############

Video of how it works

https://www.youtube.com/watch?v=6IIYGGSWvbg

# fPKG_Maker_GUI
A user friendly User Interface for fPKG Tools for PS4

I need to thank a few people before you read the steps

Thank you to CyB1K for his updated fPKG Tools, You can find his github here;

https://github.com/CyB1K/PS4-Fake-PKG-Tools-3.87

Thank you to hippie68 for his outstanding FTP Dump Linux Script. You can find his github here;

https://github.com/hippie68/ftpdump

Thank you to all the devs in the community!

and thank you to LightningMods, Keep that homebrew scene going my dude. He runs an outstanding website you can find by searching for DKS.

# ####################################

There is still much to do to this tool

# Some planned features are;

//Add DLC Unlocker

//Add Terminal Window to see what is going on

//Add dropdown menu to open all tools separate from this program

//Add back port tools

//UI Polish

# ####################################



I wanted to drop this before I go silent again for my next semester of school. This is an early build so expect some bugs but as it is right now it will;

Dump the game via FTP and GoldenHen on port 2121

Generate gp4 files 

Build the games from the gp4 files.

