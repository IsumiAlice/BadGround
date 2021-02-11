from PIL import Image
import os

def jpg2png(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            filepath = os.path.join(root, file)
            fileper, fileext = os.path.splitext(filepath)
            if fileext == ('.png' or '.PNG'):
                img = Image.open(filepath).convert("RGB")
                img.save(filepath.replace('png', 'jpg'))
                # src = cv2.imread(filepath)
                print(filepath.replace('png', 'jpg'))
                # cv2.imwrite(filepath.replace('png', 'jpg'), src)
                # cv2.imwrite('1.jpg', src)
                os.remove(filepath)


if __name__ == "__main__":
    path = r"C:\Users\Administrator\Desktop\GTA4"
    jpg2png(path)
