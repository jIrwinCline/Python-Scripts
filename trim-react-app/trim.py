#!/usr/bin/env python
import os
import sys
import time
import smtplib
from os import path
import dotenv

nargs = len(sys.argv)


def createFile(dest):
    if not (path.isfile(dest)):
        f = open(dest, 'w')
        f.write("wecome to Python Scripting")
        f.close()


dest = 'C:\\Users\\jakob\\projects\\python-scripts\\trim-react-app\\sample.txt'


def edit_file(filename):
    pass
# if not 3 <= nargs <= 5:
#     print("usage: %s search_text replace_text [infile [outfile]]" %
#           os.path.basename(sys.argv[0]))
# else:
#     stext = sys.argv[1]
#     rtext = sys.argv[2]
#     input = sys.stdin
#     output = sys.stdout
#     if nargs > 3:
#         input = open(sys.argv[3])
#     if nargs > 4:
#         output = open(sys.argv[4], 'w')
#     for s in input.xreadlines(  ):
#         output.write(s.replace(stext, rtext))
#     output.close(  )
#     input.close(  )


createFile(dest)
print("File Created")

######################################

# this works, but I had to go into google account settings and disable decure access
# smtObj = smtplib.SMTP('smtp.gmail.com', 587)
# smtObj.ehlo()
# smtObj.starttls()
# smtObj.login('jci.develo@gmail.com', 'Ibanez12$')
# smtObj.sendmail('jci.develo@gmail.com', 'jakobinwins@gmail.com',
#                 "Subject: this is a test \n This is a test email")
# smtObj.quit()
# print("email Sent")

#####################################
