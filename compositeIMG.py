
# coding: utf-8

# In[1]:


from PIL import Image
import os

def filelist(dir):
    list = os.listdir(dir)
    return list


# In[2]:


bgdir = './style_bg/'
cropdir = './multistyle_croped/'
frame = filelist(bgdir[:-1])
outputdir = 'merged_'+cropdir[2:-1]

if not os.path.exists(outputdir):
    os.makedirs(outputdir)

for file in frame:
    foreground = Image.open(cropdir+file[:-3]+"png")
    background = Image.open(bgdir+file)
    width = background.width
    height = background.height
    background.paste(foreground, (0,0), foreground)
    background.save(outputdir+'/'+file)

