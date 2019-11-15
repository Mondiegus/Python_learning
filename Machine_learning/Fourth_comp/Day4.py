#!/usr/bin/env python
# coding: utf-8

# In[11]:


import numpy as np
import pandas as pd

from gensim.utils import simple_preprocess
from gensim.models import Word2Vec
from gensim.models.phrases import Phrases, Phraser

from sklearn.decomposition import PCA

import seaborn as sns
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')


# ## Dane

# In[139]:


ls -lh data


# In[8]:


df = pd.read_csv('data/job_offer.csv')
df.shape


# In[9]:


df.head


# ## Word2Vec

# In[10]:


corpus = df['title'].map(simple_preprocess) 


# In[ ]:


model = Word2Vec(corpus, size=100, window=2, min_count=1)


# In[142]:


model.wv.most_similar['machine']


# ## Example

# In[17]:


corpus = [
    ['machine', 'learning', 'c'],
    ['machine', 'learning', 'x'],
    ['y', 'machine', 'learning', 'w'],
    ['q', 'machine', 'learning', 'u', 'k'],
]
bigram = Phraser (Phrases(corpus, min_count=1, threshold=1))

bigram [['k', 'machine', 'learning', 'c']]


# ## Title + phrases

# In[18]:


title_corpus = df['title'].map(simple_preprocess) 

title_bigram = Phraser (Phrases(title_corpus, min_count=1, threshold=1)) 


# In[20]:


title_corpus_phrase = [title_bigram[sent] for sent in title_corpus]


# In[21]:


model = Word2Vec(title_corpus_phrase, size=100, window=2, min_count=1)


# In[22]:


model.wv.most_similar('machine')


# In[24]:


def prepare_corpus(corpus, bigram):
    for sent in corpus:
        yield bigram[sent] + sent


# In[26]:


title_model = Word2Vec(list(prepare_corpus(title_corpus, title_bigram)), size=100, window=2, min_count=1)


# In[27]:


model.wv.most_similar('machine')


# ## Description

# In[38]:


description_corpus = df['description'].map(simple_preprocess) 

description_bigram = Phraser (Phrases(description_corpus, min_count=1, threshold=1)) 


# In[39]:


ext_corp = list(prepare_corpus(description_corpus description_bigram))
description_model = Word2Vec(ext_corp, size=100, window=2, min_count=1)


# In[41]:


description_model.wv.most_similar['machine']

