import cv2
import os
import numpy as np
def cv_imread(file_path):
    cv_img = cv2.imdecode(np.fromfile(filepath, dtype=np.uint8),-1)
    return cv_img

def cv_imwrite(file_path, img):
    cv2.imencode('.jpg', img)[1].tofile(file_path)

for root, dirs, files in os.walk('./'):
    for file in files:
        filepath = os.path.join(root, file)
        fileper, fileext = os.path.splitext(filepath)  # 分離拓展名
        if fileext == '.png':
            print(filepath)
            src = cv_imread(filepath)
            cv_imwrite(filepath.replace('png', 'jpg'), src)
            # cv2.imencode('.jpg', src).tofile(filepath.replace('png', 'jpg'))
            os.remove(filepath)
            # os.rename(filepath, fileper + '.jpg')
            # print(fileper+'.jpg')
# src = cv2.imread('1.png')
# cv2.imwrite('2.jpg', src)
