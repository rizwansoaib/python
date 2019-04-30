#! /usr/bin/python3




import os
from subprocess import PIPE, Popen
#function for returning terminal command cret=command return
def cret(command):
    process = Popen(
        args=command,
        stdout=PIPE,
        shell=True
    )
    return process.communicate()[0]

a=cret('mediainfo --Inform="Video;%Duration/String3%" *.MP4')
a=str(a.decode())
b=list(map(str,a.split('.')))
minute,sec=0,0
for i in range(len(b)-1):
	l=[]
	l=list(map(str,b[i].split(':')))
	minute+=int(l[1])
	sec+=int(l[2])
msec=int(sec/60)
minute+=msec

print("Total Videos : ",len(b)-1,"\nTotal length : ",minute,"min")