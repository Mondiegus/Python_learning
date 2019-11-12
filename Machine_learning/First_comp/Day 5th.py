#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np

from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import cross_val_score

get_ipython().run_line_magic('matplotlib', 'inline')


# In[6]:


df = pd.read_csv('https://raw.githubusercontent.com/aczepielik/KRKtram/master/reports/report_07-23.csv')
df.head()


# In[10]:


df[df.tripId == 6351558574044883205]


# In[15]:


df.delay.value_counts(normalize=True)


# In[25]:


df.delay.hist(bins=15);


# In[26]:


df.delay.describe()


# In[69]:


df.columns


# In[77]:


df['plannedTime'] = pd.to_datetime(df['plannedTime'])
df['plannedTime'] = df['plannedTime'].factorize()[0]


# In[79]:


df ['delay_sec'] = df['delay'].map(lambda x: x*60)
df['direction_cat'] = df['direction'].factorize()[0]
df['vehicleId'] = df['vehicleId'].fillna(-1)
df['seq_num'] = df['seq_num'].fillna(-1)

df['number_diretion_id'] = df.apply(lambda x: '{} {}'.format(x['number'], x['direction']), axis=1).factorize()[0]
df['stop_diretion_id'] = df.apply(lambda x: '{} {}'.format(x['stop'], x['direction']), axis=1).factorize()[0]
feats = [
    'number',
    'stop', 
    'direction_cat', 
    'vehicleId', 
    'seq_num',
    'number_diretion_id',
    'stop_diretion_id'
]
X = df[feats].values
Y = df['delay_sec'].values

#model = RandomForestRegressor(max_depth=10, n_estimators=50, n_jobs=4)
model = DecisionTreeRegressor(max_depth=10, random_state=0)
scores = cross_val_score(model,X,Y,cv = 3, scoring='neg_mean_absolute_error')
np.mean(scores), np.std(scores)


# In[53]:


df.apply(lambda x: '{} {}'.format(x['number'], x['direction']), axis=1).factorize()[0]


# In[ ]:





# In[ ]:





# y_pred => [0,3,2]
# y_test => [1,2,0]
# 
# error =>  [1,1,2]

# In[32]:


np.mean([1,1,2])

