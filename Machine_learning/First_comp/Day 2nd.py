#!/usr/bin/env python
# coding: utf-8

# In[17]:


import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[7]:


a = 1
np.random.seed(10)
np.random.rand(4,5)


# In[18]:


x = np.linspace(1,10,100)
y = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y)
plt.plot(x, y2)

