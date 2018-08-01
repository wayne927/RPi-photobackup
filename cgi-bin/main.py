#!/usr/bin/python

import cgi
import cgitb
import os
import umount_form

cgitb.enable()

print "Content-Type: text/html\n\n";

print("<p>Current volumes in /media/pi/:</p>")

media_path = "/media/pi"

ls_list = [x for x in os.listdir(media_path) if not x.startswith('.')]

if len(ls_list) == 0 :
    print("<p>[empty]</p>")
else :
    ls_list = sorted(ls_list)
    print("<ul>")
    for file in ls_list :
        print("<li>" + file + "</li>");
    print("</ul>\n<p>" + str(len(ls_list)) + " volumes</p>")

if len(ls_list) > 1 :
    fullpath_source = None
    fullpath_target = None
    basepath_source = None
    basepath_target = None
    
    if "photobackup" in ls_list[0].lower() :
        fullpath_source = media_path + "/" + ls_list[1]
        fullpath_target = media_path + "/" + ls_list[0]
        basepath_source = ls_list[1]
        basepath_target = ls_list[0]
    else :
        fullpath_source = media_path + "/" + ls_list[0]
        fullpath_target = media_path + "/" + ls_list[1]
        basepath_source = ls_list[0]
        basepath_target = ls_list[1]
    
    print("<p>Source = " + fullpath_source + "<br>")
    print("Target = " + fullpath_target + "</p>")

    print("<p><a href='/cgi-bin/do_rsync.py?source="+basepath_source+"&target="+basepath_target+"&dryrun=1'>Sync " + basepath_source + " into " + basepath_target + " --dry-run</a></p>")
    print("<p><a href='/cgi-bin/do_rsync.py?source="+basepath_source+"&target="+basepath_target+"&dryrun=0'>Sync " + basepath_source + " into " + basepath_target + "</a></p>")
    

umount_form.printform(ls_list)
