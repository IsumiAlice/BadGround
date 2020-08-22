__author__ = 'a1261'
import tkinter
import tkinter.messagebox 
import os, os.path
import threading  
import tkinter.simpledialog 
from tkinter import filedialog
from tkinter import *
from hashlib import *
import psutil
import time
import datetime
import signal
from PIL import Image, ImageTk

class Window:
    def __init__(self):
        self.root = tkinter.Tk()

        menu = tkinter.Menu(self.root)

        submenu0 = tkinter.Menu(menu, tearoff=0)
        submenu0.add_command(label="Exit", command = self.MenuExit)
        menu.add_cascade(label="Main", menu=submenu0)


        submenu3 = tkinter.Menu(menu, tearoff=0)
        submenu3.add_command(label="Choose a Folder", command = self.dooo)
        menu.add_cascade(label="Do Something", menu=submenu3)


        self.root.config(menu=menu)

        #标签，显示状态信息
        self.progress = tkinter.Label(self.root, anchor=tkinter.W, text="Status", bitmap="hourglass", compound="left")
        self.progress.place(x=10,y=570,width=780,height=15)


        #文本框，滚动条
        self.flist = tkinter.Text(self.root)
        self.flist.place(x=10,y=10,width=780,height=550)

        self.vscroll = tkinter.Scrollbar(self.flist)
        self.vscroll.pack(side="right", fill="y")
        self.flist["yscrollcommand"] = self.vscroll.set
        self.vscroll["command"] = self.flist.yview()

    def MainLoop(self):
        self.root.title("NNAAMMEE")
        self.root.minsize(800,600)
        self.root.maxsize(800,600)
        self.root.mainloop()

    def MenuExit(self):
        self.root.quit()

    def dooo(self):
        filedir = filedialog.askdirectory(title='Pick a directory')
        self.flist.insert(tkinter.END, "Folder is: " + filedir +'\n')

        # dosomething        


if __name__ == "__main__":
    window = Window()
    window.MainLoop()
