#!/usr/bin/env python
# coding: utf-8

# In[401]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[402]:


df = pd.read_csv(r"C:\Users\tjb1dl\Desktop\NCU18WF104F6SRB.csv")


# In[403]:


drop_indexes = list(range(0, 45)) + list(range(146, 196))
df_dropped = df.drop(index=drop_indexes, axis=0).astype(float)
df_diff = df_dropped.diff();
df_diff['  R25  '] = df_dropped['  R25  '] 


# In[404]:


V_val_temp = {"Value":3000*(3740/((df_dropped['k ohm +/- ']*1000)+3740))}
V_values = pd.DataFrame(data=V_val_temp)
V_values_diff = V_values.diff()
V_values.insert(0, "R25", df_diff['  R25  '])
V_values


# In[405]:


V_values_diff.insert(0, "R25", df_diff['  R25  '])


# In[406]:


V_values_diff


# In[407]:


df_dropped.columns


# In[408]:


pd.options.display.max_rows = 195
df_diff


# In[409]:


df_diff_mean = df_diff.mean(axis=0)
V_values_mean = V_values_diff.mean(axis=0)


# In[410]:


V_values_mean


# In[411]:


x = V_values['R25'].astype(int).to_numpy()
y = V_values['Value'].astype(int).to_numpy()


# In[412]:


z = np.polyfit(y, x, 5)
p = np.poly1d(z)

p(0)

c = p(y)
c , z, p(350)


# In[413]:


#xp = np.linspace(-2, 6, 100)
_ = plt.plot(x, y, '.')
plt.show()

