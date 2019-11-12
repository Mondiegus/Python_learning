#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


# In[38]:


df = pd.read_csv('https://raw.githubusercontent.com/dataworkshop/webinar-titanic/master/input/train.csv')
df.head()


# In[41]:


df['Sex'].value_counts();
df['Sex_cat'] = df['Sex'].factorize()[0]


# In[42]:


features = ['Pclass', 'Fare', 'Sex_cat']
X = df[features].values
y = df['Survived'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3)
X_train.shape, X_test.shape


# In[35]:


model = DecisionTreeClassifier(max_depth=10)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

accuracy_score(y_test, y_pred)


# In[29]:





# In[26]:


type(df['Sex'])

