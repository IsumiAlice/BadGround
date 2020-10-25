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
import cv2
import os
import numpy as np

str = """
使用 Opencv 將 PNG 批量轉換為 JPG
"""


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


        self.flist.insert(tkinter.END, str +'\n')

        self.vscroll = tkinter.Scrollbar(self.flist)
        self.vscroll.pack(side="right", fill="y")
        self.flist["yscrollcommand"] = self.vscroll.set
        self.vscroll["command"] = self.flist.yview()

    def MainLoop(self):
        self.root.title("JFIF2JPG")
        self.root.minsize(800,600)
        self.root.maxsize(800,600)
        self.root.mainloop()

    def MenuExit(self):
        self.root.quit()

    def cv_imread(self, file_path):
        cv_img = cv2.imdecode(np.fromfile(file_path, dtype=np.uint8), -1)
        return cv_img


    def cv_imwrite(self, file_path, img):
        cv2.imencode('.jpg', img)[1].tofile(file_path)
    
    def dooo(self):
        filedir = filedialog.askdirectory(title='Pick a directory')
        self.flist.insert(tkinter.END, "Folder is: " + filedir +'\n')
    
        for root, dirs, files in os.walk(filedir):
            for file in files:
                filepath = os.path.join(root, file)
                fileper, fileext = os.path.splitext(filepath)
                if fileext == '.png':
                    self.flist.insert(tkinter.END, filepath+'\n')
                    src = self.cv_imread(filepath)
                    self.cv_imwrite(filepath.replace('.png', '.jpg'), src)
                    os.remove(filepath)
                elif fileext == '.PNG':
                    self.flist.insert(tkinter.END, filepath+'\n')
                    src = self.cv_imread(filepath)
                    self.cv_imwrite(filepath.replace('.PNG', '.jpg'), src)
                    os.remove(filepath)
        
        self.flist.insert(tkinter.END, "Done"+'\n')


if __name__ == "__main__":
    window = Window()
    window.MainLoop()