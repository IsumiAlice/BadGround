import os

for root, dirs, files in os.walk('./'):

    for file in files:
        filepath = os.path.join(root, file)
        fileper, fileext = os.path.splitext(filepath)  # 分離拓展名
        if fileext == '.jfif':
            os.rename(filepath, fileper + '.jpg')
            print(fileper+'.jpg')