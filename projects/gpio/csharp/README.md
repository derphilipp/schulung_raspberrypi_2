# Building/Running
1. Install mono: `sudo apt-get install mono-runtime`
2. Get RaspberryPi.Net Library: `git clone https://github.com/cypherkey/RaspberryPi.Net.git`
3. Build RaspberryPi.Net Library:
```
cd RaspberryPiNet
xbuild
cp RaspberryPiDotNet/bin/Debug/RaspberryPiDotNet.dll PROJECTDIRECTORY
```
4. Building: `mcs main.cs -r:RaspberryPiDotNet.dll`
5. Running: `mono main.exe` or  `sudo mono main.exe`
