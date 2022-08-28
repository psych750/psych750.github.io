#!/usr/bin/env python
# coding: utf-8

# # Playing around with dictionaries

# ## Practice with operations on dictionary values
# 
# Here's a [deep thought (by Jack Handey)](https://philip.greenspun.com/humor/deep-thoughts)

# In[13]:


a_deep_thought = '''If you saw two guys named Hambone and Flippy, which one would you think liked dolphins the most? 
I'd say Flippy, wouldn't you? You'd be wrong, though. It's Hambone.'''


# Let's create a dictionary out of it where each word is a key and its number of letters is a value.

# In[17]:


deep_thought_dict = {}
for cur_word in a_deep_thought.split(' '):
    deep_thought_dict[cur_word.lower()]=len(cur_word)
print(deep_thought_dict)


# :::{tip}
# Common operations like this often have one-line solutions. We can accomplish the same behavior without an explicit `for` loop by using [dictionary comprehension](https://www.programiz.com/python-programming/dictionary-comprehension):
# ```python
# deep_thought_dict = {cur_word.lower(): len(cur_word) for cur_word in a_deep_thought.split(' ')}
# ```  
# :::

# Now that we have this information in a dictionary, do the following:
# 
# * What's the average number of letters in these words?
# 
# :::{tip} 
# To find an average use `mean()` from the `numpy` library. For example,
# ```python
# import numpy as np
# print(np.mean(range(10)))
# ```
# :::
# 
# 
# * What's the average number of letters in words beginning with vowels?
# 
# :::{tip}
# By taking advantage of statements that already return True/False values, the code below avoids having to have code like: if X return True, else return Y.
# ```python
# def is_vowel(letter):
#     return letter in ['a','e','i','o','u']
# ```
# :::
# 

# * Now return the mean length of words beginning with a consonant
# ```{tip}
# You don't need to write separate is_consonant() functions!
# ```
# 

# ## Using a dictionary as a look-up table
# 
# Dictionaries are a useful data-type for dynamically choosing actions based on the value of some variable.
# 
# For example, suppose we want to show different stimuli based on whether participant responded with a particular arrow key (up, down, left, right). Depending on their response, we want to update the position of a stimulus, moving it 10 pixels to the right, left, etc.We might initially write code like this:
# 
# ```python
# if resp == 'left':
#     stim.pos += (-10,0)
# elif resp == 'right':
#     stim.pos += (10,0)
# elif resp == 'up':
#     stim.pos += (0,10)
# elif resp == 'down':
#     stim.pos += (0,-10)
# ```
# 
# This is bearable if we have just 4 alternatives, but what if we have 10? 30? Remember, anytime you're finding yourself repeating a piece of code with minor variation, there's gonna be a better way. In this case, one better way is to use dictionaries.
# 
# ```python
# resps_to_positions = {'left':(-10,0), 'right':(10,0)}
# ```
# 
# Finish this activity by specifying the rest of the dictionary. Then rewrite the conditional above to use this dictionary, replacing the multi-pronged conditional with a single line of code.
# 

# In[ ]:


get_ipython().run_line_magic('load', '"solution_dictionary_look_up.py"')

