#!/usr/bin/env python3

import argparse, random, sys

parser = argparse.ArgumentParser(epilog="""
This python script creates files that can be used to create and 
destroy a set of guest users. You need to supply a prefix for 
the filenames created, and a number of users to create.

Use <output_prefix>_create.sh as root to create the users.

Use <output_prefix>_destroy.sh as root to destroy the users.

<output_prefix>.html can be printed to create slips of paper to
give out with usernames and passwords.
""", formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument("output_prefix",help="Output files prefix.")
parser.add_argument("n",type=int,help="Number of users.")
parser.add_argument("-p","--prefix",help="User name prefix.",default="guest")
parser.add_argument("-u","--url",help="URL to direct users to.",default="biotraining.erc.monash.edu")
args = parser.parse_args()

n = args.n
users = [ ("%s%d" % (args.prefix, i+1), ''.join( random.choice("abcdefghkmnpqrstuvwxyz") for i in range(8) ))
          for i in range(args.n) ]

with open(args.output_prefix+"_create.sh", "w") as f:
    for name, password in users:
       print("adduser "+name+" --gecos "+name+" --disabled-password", file=f)
       print("echo "+name+":"+password+" |chpasswd", file=f)

    print("rstudio-server restart #RStudio can become confused if there is a new user with the same username as an old user", file=f)

with open(args.output_prefix+"_destroy.sh", "w") as f:
    for name, password in users:
       print("pkill -u "+name+" ; deluser "+name+" --backup --remove-home", file=f)

with open(args.output_prefix+".html","w") as f:
    print("<!DOCTYPE html>", file=f)
    for i, (name, password) in enumerate(users):
        print("<pre style=\"font-size: 110%; page-break-inside: avoid\">", file=f)
        print("   Go to: "+args.url, file=f)
        print("Username: "+name, file=f)
        print("Password: "+password, file=f)
        print("", file=f)
        print("", file=f)
        print("</pre>", file=f)
        if i % 10 == 9:
             print('<p style="page-break-after: always;">&nbsp;</p>', file=f)
             #print('<p style="page-break-after: always;">&nbsp;</p>', file=f)


