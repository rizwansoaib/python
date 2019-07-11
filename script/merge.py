
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

a=cret('grep | ls *.MP4 *.mp4')
a=str(a.decode())
b=list(map(str,a.split('\n')))
b.sort()
b.pop(0)
print(b)
print("Total video found: ",len(b))

exec="mkvmerge -o single.mkv " 

for x in b:
	exec+=x+" \+ "
	print(x)


out=cret(exec)

print(exec)
print(out)
print("Successfully executed: ")

