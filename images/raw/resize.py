import os, sys
from PIL import Image
import glob

saveTo = '..'
size = 400, 300

min_width = 400
min_height = 300

def main():
    images = []

    for ext in ('*.gif', '*.jpg', '*.png'):
        images.extend(glob.glob(ext))

    for path in images:
        print('processing', path)
        image = Image.open(path)
        ratio = max(min_width / image.width, min_height / image.height)
        print(ratio)
        
        image = image.resize((int(image.width * ratio), int(image.height * ratio)), Image.ANTIALIAS)
        image.save(os.path.join(saveTo, path), 'png')        

if __name__ == '__main__':
    main()