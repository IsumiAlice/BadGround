import cv2
import os
import numpy as np


def cv_imread(file_path):
    cv_img = cv2.imdecode(np.fromfile(filepath, dtype=np.uint8), -1)
    return cv_img


def cv_imwrite(file_path, img):
    cv2.imencode('.jpg', img)[1].tofile(file_path)


for root, dirs, files in os.walk('./'):
    for file in files:
        filepath = os.path.join(root, file)
        fileper, fileext = os.path.splitext(filepath)
        if fileext == '.png':
            print(filepath)
            src = cv_imread(filepath)
            cv_imwrite(filepath.replace('png', 'jpg'), src)
            os.remove(filepath)
        elif fileext == '.PNG':
            print(filepath)
            src = cv_imread(filepath)
            cv_imwrite(filepath.replace('png', 'jpg'), src)
            os.remove(filepath)
