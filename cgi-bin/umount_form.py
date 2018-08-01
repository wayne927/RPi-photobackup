#import subprocess as sp
import os

def printform(paths) :
    print("<h1>Unmount volumes</h1>")
    media_path = '/media/pi'
    for p in paths :
        command = 'df | grep -i '+media_path+"/"+p.replace(" ", "\ ")
        output = os.popen(command).read()
        #print("command = "+command+"<br>")
        output = output.split(" ")
        print("<a href='/cgi-bin/umount.py?dev=" + output[0] + "'>Umount " + p + "</a> (" + output[0] + ")")
        print("<br><br>")
        
