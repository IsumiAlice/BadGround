import opencc
import os


# converter = opencc.OpenCC('s2t.json')
# converter = opencc.OpenCC('t2s.json')
converter = opencc.OpenCC('s2twp.json')
# print(converter.convert('隨機性和隨機數'))  # 漢字


sc_file = open(
    r"D:\OneDrive - Office365\Blog_src\xxx.txt", 'r', encoding='UTF-8')
output_file = open(
    r"D:\OneDrive - Office365\Blog_src\xxx_tw.txt", 'w')  # 建立輸出文件，若不存在會新建

for line in sc_file.readlines():
    try:
        output_file.write(converter.convert(line))
    except:
        print (line)
    # print(line)
sc_file.close()
output_file.close()

