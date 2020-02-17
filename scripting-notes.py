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
######################################
# # takes arity away from function
# def func(*args):
#     for arg in args:
#         print(arg)


# func(1, 2, 5, 4, 'asdf')

# # print out pairs

# def func2(*args, **kwargs):
#     for i in kwargs.items():
#         print(i)


# func2(a=1, b=2, c=3)
######################################
# create classes during run time\
# B = type("BaseClass", (object,), {})
# C1 = type("C1", (B,), {'val': 5})
# C2 = type("C2", (B,), {'val': 10})


# def ClassCreator(bool):
#     if bool:
#         return C1()
#     else:
#         return C2()


# print(ClassCreator(True).val)
# print(ClassCreator(False).val)
#####################################
# class and static methods
# class Demo:
#     # class method
#     @classmethod
#     def addOne(self, x):
#         return x+1
#     # static method
#     @staticmethod
#     def addTwo(x):
#         return x+2


# print(Demo.addOne(10))
# obj = Demo()
# print(obj.addTwo(10))
####################################
# from tkinter import *
# from tkinter import ttk

# root = Tk()
# frame = Frame(root)

# labelText = StringVar()
# label = Label(frame, textvariable=labelText)
# labelText.set("this is a label")

# button = Button(frame, text="Click Me")

# label.pack()
# button.pack()
# frame.pack()

# root.mainloop()
