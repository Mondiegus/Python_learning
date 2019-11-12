#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


tf = pd.read_csv('d:\===\driving_log.csv',
                 names = ["center", "left", "right", "steering_angle", "throttle", "break", "speed"])
tf.head()


# In[5]:


tf["break"].plot()


# In[6]:


img = Image.open(tf["left"][0])
plt.imshow(img)


# In[7]:


img = np.asarray(img)
img.shape


# In[8]:


def loadimage(fname):
    return np.asarray(Image.open(fname))


# In[9]:


def processImage(img):
    return img[10:130:2, ::4,:]


# In[10]:


img = processImage(loadimage(tf["center"][0]))
plt.imshow(img)


# In[11]:


X = [processImage(loadimage(fname)) for fname in tf["center"]]
X += [processImage(loadimage(fname)) for fname in tf["left"]]
X += [processImage(loadimage(fname)) for fname in tf["right"]]
y = np.array(tf["steering_angle"])
y = np.concatenate([y, y+0.4, y-0.4])


# In[12]:


X = np.array(X)
print(X.shape)
print(y.shape)


# In[13]:


plt.plot(y)
plt.show();


# In[14]:


np.save('d:\===\X.npy',X)
np.save('d:\===\Y.npy',y)

