__author__ = 'a1261'
import tkinter
import tkinter.messagebox   #输出信息
import os, os.path
import threading            #多线程
import tkinter.simpledialog #接受输入信息
from tkinter import filedialog
from tkinter import *
from hashlib import *
import psutil
import time
import datetime
import signal
from PIL import Image, ImageTk

rubbishExt = [".tmp", ".bak", ".old", ".wbk", ".xlk", "._mp", ".log", ".gid", ".chk", ".syd", ".$$$", ".@@@", ".~*"]

def GetDrivers():
    drivers = []
    for i in range(65,91):
        vol = chr(i) + ":/"
        if os.path.isdir(vol):
            drivers.append(vol)
    # return tuple(drivers)
    return ["d:/"]

class Window:
    def __init__(self):
        self.root = tkinter.Tk()

        menu = tkinter.Menu(self.root)

        submenu0 = tkinter.Menu(menu, tearoff=0)
        submenu0.add_command(label="显示系统信息", command = self.MenuAbout)
        submenu0.add_separator()
        submenu0.add_command(label="退出", command = self.MenuExit)
        menu.add_cascade(label="系统", menu=submenu0)

        submenu1 = tkinter.Menu(menu, tearoff=0)
        submenu1.add_command(label="扫描垃圾文件", command = self.MenuScanRubbish)
        submenu1.add_command(label="删除垃圾文件", command = self.MenuDelRubbish)
        menu.add_cascade(label="清理", menu=submenu1)

        submenu2 = tkinter.Menu(menu, tearoff=0)
        submenu2.add_command(label="搜索大文件", command = self.MenuScanBigFile)
        submenu2.add_separator()
        submenu2.add_command(label="按文件名搜索", command = self.MenuSearchFile)
        menu.add_cascade(label="搜索", menu=submenu2)

        self.root.config(menu=menu)

        #标签，显示状态信息
        self.progress = tkinter.Label(self.root, anchor=tkinter.W, text="状态", bitmap="hourglass", compound="left")
        self.progress.place(x=10,y=570,width=780,height=15)
        # bm = PhotoImage(file='/home/fangxu/图片/4.png')
        # label2 = Label(top, image=bm)
        # label2.bm = bm

        #文本框，滚动条
        self.flist = tkinter.Text(self.root)
        self.flist.place(x=10,y=10,width=780,height=550)

        self.vscroll = tkinter.Scrollbar(self.flist)
        self.vscroll.pack(side="right", fill="y")
        self.flist["yscrollcommand"] = self.vscroll.set
        self.vscroll["command"] = self.flist.yview()

        submenu3 = tkinter.Menu(menu, tearoff=0)
        submenu3.add_command(label="选择一个文件", command = self.MenuHash)
        menu.add_cascade(label="文件校验", menu=submenu3)

        submenu4 = tkinter.Menu(menu, tearoff=0)
        #submenu4.add_command(label="显示当前所有进程", command = self.MenuProcessAll)

        #submenu4.add_separator()
        submm = tkinter.Menu(submenu4,tearoff=0)
        submenu4.add_cascade(label="显示当前所有进程",menu=submm)
        submm.add_command(label="按照pid排序", command = self.MenuProcessPid)
        submm.add_command(label="按照占用内存排序", command = self.MenuProcessMem)
        submenu4.add_command(label="按pid结束进程", command = self.MenuDeleteProcess)
        submenu4.add_command(label='按pid显示进程详细信息',command = self.MenuProcessMessage)
        menu.add_cascade(label="进程管理", menu=submenu4)

        submenu5 = tkinter.Menu(menu, tearoff=0)
        submenu5.add_command(label="全部文件重命名", command = self.MenuRenameAll)    #将整个文件夹重命名000-999，拓展名为3位（不算点）
        submenu5.add_separator()
        submenu5.add_command(label="在文件名头添加字符", command = self.MenuRenameHead)
        submenu5.add_command(label="在文件尾部添加字符", command = self.MenuRenameTail)
        menu.add_cascade(label="重命名", menu=submenu5)

    def MainLoop(self):
        self.root.title("fff")
        self.root.minsize(800,600)
        self.root.maxsize(800,600)
        self.root.mainloop()

    def MenuAbout(self):
        self.flist.delete(0.0, tkinter.END)
        #tkinter.messagebox.showinfo("About", "本程序可以做...\n欢迎使用")
        #filename = filedialog.askopenfilename()
        #print (filename)
        self.flist.insert(tkinter.END, "系统启动时间： "+str(datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")) + '\n\n')
        self.flist.insert(tkinter.END, "处理器信息" + '\n')
        self.flist.insert(tkinter.END, "处理器物理数量： "+str(psutil.cpu_count()) + '\n')
        self.flist.insert(tkinter.END, "处理器逻辑数量： "+str(psutil.cpu_count(logical=False)) + '\n\n')

        self.flist.insert(tkinter.END, "内存信息" + '\n')
        mem=psutil.virtual_memory()
        self.flist.insert(tkinter.END, "内存： "+str(mem.total/1024/1024)[:4] + 'MB\n')
        self.flist.insert(tkinter.END, "当前可用内存大小： "+str(mem.available/1024/1024)[:4] + 'MB\n')
        self.flist.insert(tkinter.END, "当前内存使用率： "+str(mem.percent) + '%\n\n')

        self.flist.insert(tkinter.END, "磁盘信息" + '\n')
        self.flist.insert(tkinter.END, str(psutil.disk_partitions()) + '\n')
        #self.flist.insert(tkinter.END, "： "+str(psutil.pids()) + '\n')

    def MenuExit(self):
        self.root.quit()

    def MenuScanRubbish(self):
        result = tkinter.messagebox.askquestion("扫描垃圾","扫描垃圾需要较长时间，是否继续？")
        if result == 'no':
            return
        else:
            tkinter.messagebox.showinfo("扫描垃圾", "开始扫描垃圾文件...")
            #self.ScanRubbish()
            self.drivers = GetDrivers()
            t = threading.Thread(target = self.ScanRubbish, args=(self.drivers,))   #创建线程
            t.start()

    def MenuDelRubbish(self):
        result = tkinter.messagebox.askquestion("删除垃圾","删除垃圾需要较长时间，是否继续？")
        if result == 'no':
            return
        else:
            tkinter.messagebox.showinfo("删除垃圾", "开始删除垃圾文件...")
            self.drivers = GetDrivers()
            t = threading.Thread(target=self.DeleteRubbish(self.drivers))
            t.start()

    def MenuScanBigFile(self):
        s = tkinter.simpledialog.askinteger("Input", "请设置文件大小（MB）")
        t = threading.Thread(target=self.ScanBigFile,args=(s,))
        t.start()

    def MenuSearchFile(self):
        s = tkinter.simpledialog.askstring("Input", "输入要搜索的文件名")
        t = threading.Thread(target=self.SearchFile,args=(s,))
        t.start()
    def MenuProcessPid(self):
        self.flist.delete(0.0, tkinter.END)
        # self.flist.insert(tkinter.END, "： "+str(psutil.pids()) + '\n')
        #self.flist.insert(tkinter.END, '进程ID\t' + '进程名\t'+'进程路径' + '\n')
        list = psutil.pids()
        list.sort()
        for pid in list:
            #print (pid)
            i = 0;
            p = psutil.Process(pid)
            mem=psutil.virtual_memory()
            memsize = str(p.memory_percent()*(mem.total/1024/1024)/100)[:4]+'MB'
            self.flist.insert(tkinter.END,str(p.pid) + '\t' + str(p.name())+'\t\t\t\t' + memsize +'\t'+'\n')
    def MenuProcessMem(self):
        return
    def MenuProcessMessage(self):
        self.flist.delete(0.0, tkinter.END)
        pid = tkinter.simpledialog.askinteger("Input", "请输入进程pid")
        try:
            p = psutil.Process(pid)
        except:
            self.flist.insert(tkinter.END,'未找到此进程')
            return
        self.flist.insert(tkinter.END,'进程名称:'+p.name()+'\n')
        self.flist.insert(tkinter.END,'进程pid:'+str(p.pid)+'\n')
        try:
            self.flist.insert(tkinter.END,'父进程pid：'+str(p.ppid())+'\n')
        except:
            pass
        try:
            self.flist.insert(tkinter.END,'bin路径：'+str(p.exe())+'\n')
        except:
            pass

        try:
            self.flist.insert(tkinter.END,'绝对路径：'+str(p.cwd())+'\n')
        except:
            pass

        self.flist.insert(tkinter.END,'状态：'+p.status()+'\n')
        self.flist.insert(tkinter.END,'创建时间：'+str(datetime.datetime.fromtimestamp(p.create_time()))+'\n')
        mem=psutil.virtual_memory()
        memsize = str(p.memory_percent()*(mem.total/1024/1024)/100)[:4]+'MB'
        self.flist.insert(tkinter.END,'内存占用：'+memsize+'\n')
        self.flist.insert(tkinter.END,'内存详细：'+str(p.memory_info())+'\n')
        self.flist.insert(tkinter.END,'IO信息：'+str(p.io_counters())+'\n')
        self.flist.insert(tkinter.END,'进程开启的线程数：'+str(p.num_threads())+'\n')
    def MenuDeleteProcess(self):
        pid = tkinter.simpledialog.askinteger("Input", "请输入进程pid")
        list = psutil.pids()
        try:
            a = os.kill(pid, signal.SIGTERM)
            tkinter.messagebox.showinfo("Note", '已杀死pid为%s的进程,　返回值是:%s' % (pid, a))
            #self.flist.insert(tkinter.END,'已杀死pid为%s的进程,　返回值是:%s' % (pid, a)+'\n')
        except OSError as e:
            tkinter.messagebox.showinfo("Note", '杀死进程失败，或没有此进程')
            #self.flist.insert(tkinter.END,'杀死进程失败，或没有此进程'+'\n')

    def ScanRubbish(self, scanpath):
        self.flist.delete(0.0, tkinter.END)
        global rubbishExt
        total = 0
        filesize = 0
        for drive in scanpath:
            for root,dirs,files in os.walk(drive):
                try:
                    for fil in files:
                        filesplit = os.path.splitext(fil)
                        fname = os.path.join(os.path.abspath(root),fil)
                        self.progress["text"] = fname
                        if filesplit[1] == '':  #文件无扩展名
                            continue
                        try:
                            if rubbishExt.index(filesplit[1]) >= 0:     #扩展名在列表里
                                # fname = os.path.join(os.path.abspath(root),fil)
                                filesize += os.path.getsize(fname)
                                l = len(fname)
                                # if l > 60:
                                #     self.progress["text"] = fname[:30] + "..." + fname[l - 30:1]
                                # else:
                                #     self.progress["text"] = fname
                                total += 1
                                self.flist.insert(tkinter.END, fname + '\n')
                        except ValueError:
                            pass
                except Exception as e:
                    print (e)
                    pass
        self.progress["text"] = "共找到 %s 个文件， 占用 %.2f M 空间" %(total, filesize/1024/1024)

    def DeleteRubbish(self, scanpath):
        self.flist.delete(0.0, tkinter.END)
        global rubbishExt
        total = 0
        filesize = 0
        for drive in scanpath:
            for root,dirs,files in os.walk(drive):
                try:
                    for fil in files:
                        filesplit = os.path.splitext(fil)
                        fname = os.path.join(os.path.abspath(root),fil)
                        self.progress["text"] = fname
                        if filesplit[1] == '':  #文件无扩展名
                            continue
                        try:
                            if rubbishExt.index(filesplit[1]) >= 0:     #扩展名在列表里
                                # fname = os.path.join(os.path.abspath(root),fil)
                                filesize += os.path.getsize(fname)
                                try:
                                    os.remove(fname)
                                    l = len(fname)
                                    # if l > 50:
                                    #    fname = fname[:25] + "..." + fname[l - 25:1]
                                    self.flist.insert(tkinter.END, "已经删除："+ fname + '\n')
                                    # self.progress["text"] = fname
                                    total += 1
                                except:
                                    pass
                        except ValueError:
                            pass
                except Exception as e:
                    print (e)
                    pass
        self.progress["text"] = "共清理 %s 个文件， 释放 %.2f M 磁盘空间" %(total, filesize/1024/1024)

    def ScanBigFile(self,filesize):
        self.flist.delete(0.0, tkinter.END)
        total = 0
        filesize = int(filesize) * 1024 * 1024
        for drive in GetDrivers():
            for root,dirs,files in os.walk(drive):
                for fil in files:
                    try:
                        fname = os.path.abspath(os.path.join(root,fil))
                        fsize = os.path.getsize(fname)

                        self.progress['text'] = fname   #在状态标签显示每个遍历的文件
                        if fsize >= filesize:
                            total += 1
                            self.flist.insert(tkinter.END, "%s, [%.2f M]\n" %(fname,fsize/1024/1024))
                    except:
                        pass
        self.progress["text"] = "找到 %s 个超过 %s M 的文件"  %(total, filesize/1024/1024)

    def SearchFile(self, fname):
        self.flist.delete(0.0, tkinter.END)
        total = 0
        fname = fname.upper()
        for drive in GetDrivers():
            for root, dirs, files in os.walk(drive):
                for fil in files:
                    try:
                        fn = os.path.abspath(os.path.join(root,fil))
                        l = len(fn)
                        if l > 50:
                            self.progress['text'] = fn[:25] +  '...' + fn[l-25:l]
                        else:
                            self.progress['text'] = fn

                        if fil.upper().find(fname) >= 0 :
                            total += 1
                            self.flist.insert(tkinter.END, fn + '\n')
                    except:
                        pass
        self.progress['text'] = "找到 %s 个文件" % (total)

    def MenuHash(self):
        self.flist.delete(0.0, tkinter.END)
        filename = filedialog.askopenfilename()
        # print (filename)
        self.flist.insert(tkinter.END, filename + '\n')
        # print ("大小：",end = '')
        self.flist.insert(tkinter.END, "大小：")
        # print (os.path.getsize(filename),end = '')
        self.flist.insert(tkinter.END, os.path.getsize(filename))
        # print ("字节")
        self.flist.insert(tkinter.END, "字节"+ '\n')
        self.Generate_file_md5value(filename)
        self.Generate_file_sha1value(filename)

    def Generate_file_md5value(self, fpath):
        m = md5()
        # 需要使用二进制格式读取文件内容
        a_file = open(fpath, 'rb')
        m.update(a_file.read())
        a_file.close()
        # print ("MD5："+ m.hexdigest())
        self.flist.insert(tkinter.END, "MD5："+ m.hexdigest() + '\n')

    def Generate_file_sha1value(self, fpath):
        m = sha1()
        # 需要使用二进制格式读取文件内容
        a_file = open(fpath, 'rb')
        m.update(a_file.read())
        a_file.close()
        # print ("SHA1："+ m.hexdigest())
        self.flist.insert(tkinter.END, "SHA1："+ m.hexdigest() + '\n')

    def MenuRenameAll(self):
        filedir = filedialog.askdirectory(title='Pick a directory')
        for parent, dirnames, filenames in os.walk(filedir):
            for dirname in dirnames:    #输出文件夹信息

                print ("parent is: " + parent)
                print ("dirname is: " + dirname)
        i = 0
        newname = ''
        for parent, dirnames, filenames in os.walk(filedir):
            for filename in filenames:  # 输出文件信息
                # print ("parent is: " + parent)
                self.flist.insert(tkinter.END,"filename is: " + filename+'\n')
                # print ("the full name of the file is: " + os.path.join(parent,filename)) #输出文件路径信息
                if i < 10:
                    newname = '00' + str(i)
                elif i < 100:
                    newname = '0' + str(i)
                elif i < 1000:
                    newname = str(i)
                newname += filename[-4:]
                os.rename(os.path.join(parent, filename), os.path.join(parent, newname))
                i += 1

    def MenuRenameHead(self):
        filedir = filedialog.askdirectory(title='Pick a directory')
        head = tkinter.simpledialog.askstring("Input", "输入要在文件名头位置添加的字符")
        for parent, dirnames, filenames in os.walk(filedir):
            for filename in filenames:  # 输出文件信息
                # print ("parent is: " + parent)
                self.flist.insert(tkinter.END,"filename is: " + filename+'\n')
                # print ("the full name of the file is: " + os.path.join(parent,filename)) #输出文件路径信息

                newname = head + filename
                os.rename(os.path.join(parent, filename), os.path.join(parent, newname))
    def MenuRenameTail(self):
        filedir = filedialog.askdirectory(title='Pick a directory')
        tail = tkinter.simpledialog.askstring("Input", "输入要在文件名尾位置添加的字符")
        for parent, dirnames, filenames in os.walk(filedir):
            for filename in filenames:  # 输出文件信息
                # print ("parent is: " + parent)
                self.flist.insert(tkinter.END,"filename is: " + filename+'\n')
                # print ("the full name of the file is: " + os.path.join(parent,filename)) #输出文件路径信息
                str = filename[:-4]
                newname =  str + tail +filename[-4:]
                os.rename(os.path.join(parent, filename), os.path.join(parent, newname))

if __name__ == "__main__":
    window = Window()
    window.MainLoop()