#!/usr/bin/python

import cgi
import cgitb
import subprocess as sp

cgitb.enable()

print "Content-Type: text/html\n\n";

command = "df -Th"

print("<p>" + command + "</p>")

output = sp.check_output(["df", "-Th"])

print(type(output))
print(output.replace("\n","<br>").replace(" ","&nbsp;"))
