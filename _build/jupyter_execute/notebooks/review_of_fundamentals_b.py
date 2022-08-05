#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc" style="margin-top: 1em;"><ul class="toc-item"><li><span><a href="#Review-of-fundamentals-B" data-toc-modified-id="Review-of-fundamentals-B-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Review of fundamentals B</a></span><ul class="toc-item"><li><span><a href="#Lists,-randomization,-and-list-comprehension" data-toc-modified-id="Lists,-randomization,-and-list-comprehension-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Lists, randomization, and list comprehension</a></span></li><li><span><a href="#Dictionaries" data-toc-modified-id="Dictionaries-1.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Dictionaries</a></span></li></ul></li></ul></div>

# # Review of fundamentals B
# In this notebook, you will review the additional python syntax we've covered since the first review of fundamentals. You should be able to correctly predict what happens in all of these cases. If you get something wrong, figure out why!

# ## Lists, randomization, and list comprehension

# In[1]:


my_list = ['spam']
print len(my_list), len(my_list[0])


# In[2]:


print range(10)[-5:]


# In[3]:


import random
my_list = ['a','b','c']*3 + ['c','d','e']*3
random.shuffle(my_list)
my_list[0:5]


# In[4]:


import random
my_list = ['a','b','c'] + ['c','d','e']
random.sample(my_list,7)


# In[12]:


import random
[round(random.random(),1) for i in range(15)]


# In[11]:


vowels = ['a', 'e', 'i','o','u']
print [element*i for i,element in enumerate(vowels)]


# In[10]:


print ' '.join([' '.join((i, 'and a')) for i in ('one', 'two', 'three', 'four')])


# In[9]:


responses = 'ccctcttcttttcccttctcccctctctccc'
[i for i,curResp in enumerate(responses) if curResp=='c']


# In[8]:


import random

positions = ['left', 'middle', 'right']
positions2 = positions

positions.append('bottom')
random.shuffle(positions2)

print positions, positions2
print len(positions), len(positions2)
print positions==positions2


# ## Dictionaries

# In[5]:


positions = {'left':(-100,0), 'middle':(0,0), 'right':(100,0)}
[random.choice(positions.keys()) for i in range(10)]


# In[6]:


positions = {'left':(-100,0), 'middle':(0,0), 'right':(100,0)}
[positions[random.choice(positions.keys())] for i in range(10)]


# In[7]:


responses = 'ccctcttcttttcccttctcccctctctccc'
responsesMapping = {'c':'chair','t':'table'}
[responsesMapping[curResp] for curResp in responses]


# In[ ]:




