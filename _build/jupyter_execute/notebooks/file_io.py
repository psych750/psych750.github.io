#!/usr/bin/env python
# coding: utf-8

# # Getting filenames
# 
# I have advocated for preloading your stimuli at experiment start-time by grabbing all the files in a directoryt that match your criteria (e.g., all the png files) and loading them into memory. The `loadFiles()` function

# In[2]:


import os
import glob


# In[30]:


special_stims = [stim for stim in open('special_stims.txt','r')]


# A bit on managing paths in Python. For more info, see `help(os.path)`

# In[53]:


print os.getcwd() #current working directory
print os.path.join(os.getcwd(), 'stimuli/visual/') #creating a longer path
os.path.exists(os.path.join(os.getcwd(), 'stimuli/visual/')) #checking if a path exists


# Getting all the files in a directory

# In[61]:


allFiles = glob.glob(os.path.join(os.getcwd(), 'stimuli/visual/*'))
print allFiles


# Now let's get just the filename part of the path

# In[62]:


just_names = [os.path.basename(file) for file in allFiles]
print just_names


# Now let's get just the category name.

# In[ ]:


#go for it!


# Now figure out which of these files don't occur in special_stims and so are just regular stims.
