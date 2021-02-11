from PIL import Image
import os

def png2jpg(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            filepath = os.path.join(root, file)
            fileper, fileext = os.path.splitext(filepath)
            if fileext == ('.png' or '.PNG'):
                img = Image.open(filepath).convert("RGB")
                img.save(filepath.replace('png', 'jpg'))
                print(filepath.replace('png', 'jpg'))
                os.remove(filepath)

if __name__ == "__main__":
    path = r"C:\Users\Administrator\Desktop\GTA4"
    png2jpg(path)
