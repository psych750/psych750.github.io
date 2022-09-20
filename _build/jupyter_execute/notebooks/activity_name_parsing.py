#!/usr/bin/env python
# coding: utf-8

# # String manipulation exercise
# 
# 

# In[23]:


import pandas as pd
names = pd.read_csv('https://raw.githubusercontent.com/psych750/resources/main/stimuli/psych750_roster.csv')
full_names = list(names['Name'])
print(full_names)


# ## Output first names only
# 
# Write a loop with code that processes the `full_names` list and outputs just the first names

# ## Now turn it into a function
# 
# Complete the body of this function to return a list containing just the first names in the same order as the full names that were given to the function.

# In[27]:





# ## Test your function

# In[32]:


first_names = return_first_names(full_names)
try:
    assert first_names == ['Lauren', 'Drew', 'Alexander', 'Carol', 'Emma', 'Meng', 'Sizhe', 'Benjamin', 'Kendall', 'Lihao', 'Jacob', 'Yuanxue', 'Michelle', 'Lucas', 'Matthew', 'Andrea', 'Sujin', 'Ezgi', 'Zhuolun', 'Yan']
except AssertionError:
    print("Woops something's not right with your list")

