#!/usr/bin/python

import cgi
import cgitb
import os
import sys

cgitb.enable()

print "Content-Type: text/html\n\n";

form = cgi.FieldStorage()

device = form["dev"].value

command = "sudo umount " + device

print("Executing command <br><pre>" + command + "</pre><br>")
rc = os.system(command)

if rc == 0 :
    print("<div style='color: green;'>Succesfully unmounted " + device + "</div>")
else :
    print("<div style='color: red;'>Failed to umount " + device + "</div>")

