#!/usr/bin/env python
# coding: utf-8

# In[92]:


from gensim.models import Word2Vec

import numpy as np
import pandas as pd

from sklearn.decomposition import PCA

import seaborn as sns
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')


# ## Dane

# In[139]:


sentences = []

for i in range(100000):
    start = np.random.randint(0,20)
    finish = start + np.random.randint(1,10)
    sentence = [str(x) for x in list(range(start, finish))]
    sentences.append(sentence)


# In[140]:


sentences


# ## Model Word2Vec

# In[141]:


model = Word2Vec(sentences, size=20, window=4, min_count = 1)
model


# In[142]:


model.wv['1']


# In[143]:


def plot_heatmap(model):
    plt.figure(figsize=(15, 10))
    sns.heatmap(model.wv[model.wv.vocab], linewidths=0.5)


# In[144]:


plot_heatmap(Word2Vec(sentences, size=50, window=4, min_count = 1))


# ## PCA

# In[145]:


def plot_PCA(model):
    X = model.wv[model.wv.vocab]
    pca_model = PCA(n_components=2)
    result = pca_model.fit_transform(X)

    plt.figure(figsize=(15,8))
    plt.scatter(result[:,0],result[:,1]);


    words = list(model.wv.vocab)
    for i, word in enumerate(words):
        plt.annotate(word, xy=(result[i, 0], result[i, 1]))


# In[146]:


plot_PCA(Word2Vec(sentences, size=50, window=4, min_count = 1))


# ## Podobne słowa

# In[147]:


model = Word2Vec(sentences, size=50, window=4, min_count = 1)


# In[153]:


model.wv.most_similar('10', topn=3)


# ## Skutek uboczny - nauka matematyki - typ unspupervised ale możemy dotrenować używając gotowych wyników i nauki nadzorowanej

# In[149]:


model.wv.most_similar(positive = ['10', '8'], negative=['5'], topn=3)

