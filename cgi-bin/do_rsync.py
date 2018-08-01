#!/usr/bin/python

import os
import subprocess
import cgi

form = cgi.FieldStorage()

source = form["source"].value
target = form["target"].value
dryrun = form["dryrun"].value

subprocess.Popen(['/home/pi/web/cgi-bin/asynchronous_rsync.sh', source, target, dryrun])
print("Status: 302 Moved")
print("Location: /sync_status.html\n\n")
