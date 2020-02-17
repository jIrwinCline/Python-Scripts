import os
import time
import smtplib
from os import path
import dotenv

# def current_directory():
#     cwd = os.getcwd()
#     print(cwd)


# def file_path(filename):
#     path = os.path.abspath((filename))
#     print(path)


# current_directory()
# filename = 'sample.txt'
# file_path(filename)
####################################
# epc = time.time()
# localtime = time.localtime(epc)
# print(localtime.tm_year)

# print(time.ctime(epc))
####################################
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
# def createFile(dest):
#     if not (path.isfile(dest)):
#         f = open(dest, 'w')
#         f.write("wecome to Python Scripting")
#         f.close()


# dest = 'C:\\Users\\jakob\\projects\\python-scripts\\trim-react-app\\sample.txt'

# createFile(dest)

# print("File Created")
