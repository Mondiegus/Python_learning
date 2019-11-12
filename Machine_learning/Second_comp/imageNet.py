#!/usr/bin/env python
# coding: utf-8

# In[73]:


from keras.applications.resnet50 import ResNet50, decode_predictions, preprocess_input
from keras.preprocessing import image
import numpy as np

import requests
from io import BytesIO
from PIL import Image


# In[74]:


model = ResNet50(weights = 'imagenet')


# In[75]:


model.summary()


# ![](https://images.unsplash.com/photo-1518791841217-8f162f1e1131?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80)

# In[76]:


url_img = 'https://gfx.antyradio.pl/var/antyradio/storage/images/adrenalina/duperele/grumpy-cat-zdechl-przyczyna-smierci-31845/7334832-1-pol-PL/Grumpy-Cat-zdechl.-Co-bylo-przyczyna-smierci-najpopularniejszego-kota-internetu_article.jpg'

response = requests.get(url_img)
img = Image.open(BytesIO(response.content))
img = img.resize((224,224))


# In[77]:


X = image.img_to_array(img)
X = np.expand_dims(X, axis = 0)
X.shape


# In[78]:


y_pred = model.predict(X)


# In[79]:


decode_predictions(y_pred,top = 3)

