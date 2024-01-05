# MLWProj

# IMPORTANT: pyinstaller Windows version is required, Visual Studio for Windows required

Python Executables:
pip install -r requirements.txt

pyinstaller.exe .\game.spec 

pyinstaller.exe .\shell.spec

pyinstaller.exe .\ransom\ransom.spec

C Executables:

cl \o shpol.exe .\mlw\shpol.c
