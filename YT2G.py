import sys
import pafy 
import os
#--- Color  ---#
W  = '\033[0m'  # white (default)
R  = '\033[31m' # red
G  = '\033[1;32m' # green bold
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[36m' # cyan
GR = '\033[37m' # gray
os.system('clear')
print("""[\033[1;32m*\033[1;m]
 ██▄  ▄██  ▀▀▀██▀▀▀  █▀▀▀▀██▄   ██▀▀▀▀█
  ██▄▄██      ██           ██  ██
   ▀██▀       ██         ▄█▀   ██  ▄▄▄▄
    ██        ██       ▄█▀     ██  ▀▀██
    ██        ██     ▄██▄▄▄▄▄   ██▄▄▄██
    ▀▀        ▀▀     ▀▀▀▀▀▀▀▀     ▀▀▀▀ You Tube Downloader
A Tool By Isuruwaaa""")

print("----------------------------------------------------==") 
url = input("""[\033[36m]enter your url = """)
print("""[\033[34m] Available formats : mp4,3gp,webm,flv,m4a""")
reso = input("enter video format  = ")
print("""[\033[33m] internal = type as /sdcard
   external= type as ~/storage/external""")
storage=input("""[\033[36m]enter your saving path = """)
video = pafy.new(url) 
print(video.title)
print(video.rating) 
print(video.viewcount)
print(video.author)
print(video.length)
print(video.duration)
streams = video.streams
for i in streams: 

    print(i) 
print(i.resolution)
print(i.extension)
print(i.get_filesize)
best = video.getbest(preftype = reso)
best.download(filepath=storage)
