import os
import cv2
import sys
import time
import ctypes
import subprocess
import numpy as np

# 暗蓝色
FOREGROUND_DARKBLUE = 0x01
# 暗绿色
FOREGROUND_DARKGREEN = 0x02
# 暗天蓝色
FOREGROUND_DARKSKYBLUE = 0x03
# 暗红色
FOREGROUND_DARKRED = 0x04
# 暗粉红色
FOREGROUND_DARKPINK = 0x05
# 暗黄色
FOREGROUND_DARKYELLOW = 0x06
# 暗白色
FOREGROUND_DARKWHITE = 0x07
# 暗灰色
FOREGROUND_DARKGRAY = 0x08
# 蓝色
FOREGROUND_BLUE = 0x09
# 绿色
FOREGROUND_GREEN = 0x0a
# 天蓝色
FOREGROUND_SKYBLUE = 0x0b
# 红色
FOREGROUND_RED = 0x0c
# 粉红色
FOREGROUND_PINK = 0x0d
# 黄色
FOREGROUND_YELLOW = 0x0e
# 白色
FOREGROUND_WHITE = 0x0f
# 上面颜色对应的RGB值
cmd_colors = {
				'FOREGROUND_DARKBLUE': [FOREGROUND_DARKBLUE, (0, 0, 139)],
				'FOREGROUND_DARKGREEN': [FOREGROUND_DARKGREEN, (0, 100, 0)],
				'FOREGROUND_DARKSKYBLUE': [FOREGROUND_DARKSKYBLUE, (2, 142, 185)],
				'FOREGROUND_DARKRED': [FOREGROUND_DARKRED, (139, 0, 0)],
				'FOREGROUND_DARKPINK': [FOREGROUND_DARKPINK, (231, 84, 128)],
				'FOREGROUND_DARKYELLOW': [FOREGROUND_DARKYELLOW, (204, 204, 0)],
				'FOREGROUND_DARKWHITE': [FOREGROUND_DARKWHITE, (255, 250, 250)],
				'FOREGROUND_DARKGRAY': [FOREGROUND_DARKGRAY, (169, 169, 169)],
				'FOREGROUND_BLUE': [FOREGROUND_BLUE, (0, 0, 255)],
				'FOREGROUND_GREEN': [FOREGROUND_GREEN, (0, 128, 0)],
				'FOREGROUND_SKYBLUE': [FOREGROUND_SKYBLUE, (135, 206, 235)],
				'FOREGROUND_RED': [FOREGROUND_RED, (255, 0, 0)],
				'FOREGROUND_PINK': [FOREGROUND_PINK, (255, 192, 203)],
				'FOREGROUND_YELLOW': [FOREGROUND_YELLOW, (255, 255, 0)],
				'FOREGROUND_WHITE': [FOREGROUND_WHITE, (255, 255, 255)]
			}
CHARS = " .,-'`:!1+*abcdefghijklmnopqrstuvwxyz<>()\/{}[]?234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ%&@#$"

def video2img(video_path, img_size, interval=1):
    imgs = []
    capture = cv2.VideoCapture(video_path)
    i = -1
    while capture.isOpened():
        i += 1
        ret, frame = capture.read()
        if ret:
            if i % interval == 0:
                img = cv2.resize(frame, img_size, interpolation = cv2.INTER_AREA)
                imgs.append(img)
        else:
            break
    capture.release()
    return imgs

# imgs = video2img('test0.mp4', (800, 480))
# for k in range(10, 1000,100):
#     cv2.imshow('hi', imgs[k])
#     cv2.waitKey()

def img2chars(img):
    img_chars = []
    height, width, channel = img.shape
    for row in range(height):
        line = ''
        for col in range(width):
            percent = int(np.array(img[row][col]).sum() / 3) / 255
            char_index = int(percent * (len(CHARS) - 1))
            line += CHARS[char_index] + ' '
        img_chars.append(line)
    return img_chars

def imgs2chars(imgs):
    video_chars = []
    for img in imgs:
        video_chars.append(img2chars(img))
    return video_chars

def play(video_chars, color = None, iscmd = True):
    if color and iscmd:
        STD_OUTPUT_HANDLE = -11
        std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
        color_choice = None
        if color.isdigit():
            color_choice = list(cmd_colors.values())[int(color)][0]
        else:
            color_choice = cmd_colors.get(color)[0]
            
