import os
from PIL import Image

def search(dirname):
    filenames = os.listdir(dirname)
    return filenames;

files = search('./data')
inDIR = './data/'
outDIR = './resizedoutput/'
mywidth = 300

for file in files:
    
    img = Image.open(inDIR+file)
    wpercent = (mywidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((mywidth,hsize), PIL.Image.ANTIALIAS)
    img.save(outDIR+file)
    print(outDIR+file)


# In[4]:




