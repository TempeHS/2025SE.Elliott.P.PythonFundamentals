import sys
import PIL
from PIL import Image
import os


i = sys.argv[1]
f = sys.argv[2]
Ipath, Iext = os.path.splitext(sys.argv[1])
Fpath, Fext = os.path.splitext(sys.argv[2])
formo = [".jpg"]

if len(sys.argv) > 2:

    sys.exit
elif Iext != Fext:
    print("out not match inp")
    sys.exit

# try:

with Image.open(i) as im:
    imorg = PIL.Image.open(i)  # FORMATS IS BEING ANNOYING
    # PIL.ImageOps.fit(image: i, size: tuple[150, 150])
    imorg.paste("images/took.png", box=None, mask=None)

# except (FileNotFoundError, ValueError):
# print("exception")
