import os
from PIL import Image

files = "abc.png"
img = Image.open(files)
img = img.resize((256,256), Image.ANTIALIAS)
img.convert('RGBA').save('output.png')

