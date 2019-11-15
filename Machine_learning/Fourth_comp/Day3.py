#!/usr/bin/env python
# coding: utf-8

# In[4]:


import gzip
from gensim.models import Word2Vec, LdaMulticore
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS
from gensim.corpora import Dictionary

import numpy as np
import pandas as pd
import pyLDAvis
from pyLDAvis import gensim


# ## Dane

# In[33]:


ls -lh data


# In[80]:


def preprocessing(sentence):
    return [word for word in simple_preprocess(sentence) 
            if word not in STOPWORDS]
    
def read_sentence(filename):
    f = open(filename, 'rb')
    for line in f:
        yield preprocessing(line)


# In[81]:


sentences = list(read_sentence('data/reviews_data.txt'))


# ## Model

# In[82]:


model = Word2Vec(sentences, size=100, min_count=2, window=4)


# ## Reprezentacja wektorowa

# In[97]:


model.wv.most_similar('denver')


# ## Topic modeling - LDA
# 

# In[98]:


sentences_light = np.random.permutation(sentences)


# In[106]:


sentences_light = sentences_light[:1000]


# In[107]:


get_ipython().run_line_magic('time', 'dictionary = Dictionary(sentences_light)')


# In[109]:


len(dictionary)


# In[111]:


bow_corpus = [dictionary.doc2bow(sent) for sent in sentences_light]


# In[113]:


dictionary.doc2bow(['car'])


# In[115]:


dictionary.token2id['car']


# In[116]:


lda_model = LdaMulticore(bow_corpus, id2word=dictionary, num_topics=100,passes=20, workers=8)


# In[120]:


for idx, topic in lda_model.print_topics(-1):
    print('Topic: {} \nWords: {}'.format(idx,topic))


# ## Wizualizacja tematów

# In[121]:


get_ipython().run_line_magic('time', 'lda_vis = pyLDAvis.gensim.prepare(lda_model, bow_corpus, dictionary)')
pyLDAvis.display(lda_vis)


# ## Podobne słowa

# In[147]:


model = Word2Vec(sentences, size=50, window=4, min_count = 1)


# In[153]:


model.wv.most_similar('10', topn=3)


# ## Skutek uboczny - nauka matematyki - typ unspupervised ale możemy dotrenować używając gotowych wyników i nauki nadzorowanej

# In[149]:


model.wv.most_similar(positive = ['10', '8'], negative=['5'], topn=3)

