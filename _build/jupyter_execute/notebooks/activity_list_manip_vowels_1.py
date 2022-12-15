#!/usr/bin/env python
# coding: utf-8

# # List/string manipulation exercises
# 
# ## Exercise 1
# 
# For the first exercise, you'll be reading in some names and manipulating them.
# 
# First, let's grab your full names from the course roster.
# 
# 

# In[1]:


import pandas as pd
names = pd.read_csv('https://raw.githubusercontent.com/psych750/resources/main/stimuli/psych750_roster.csv')
full_names = list(names['Name'])
print(full_names)


# In[ ]:


for cur_name in full_names:
    
    first_middle = cur_name.split(',')[1]
    if len(first_middle.split( ))>1:
        print(first_middle.split( )[0])
    else:
        print(first_middle)


# ### Output first names only
# 
# Write a loop with code that processes the `full_names` list and outputs just the first names

# ## Now turn it into a function
# 
# Complete the body of this function to return a list containing just the first names in the same order as the full names that were given to the function.

# In[ ]:


def return_first_names(names):
    pass


# ### Now test it by running this code:

# 
# 
# ```{python}
# first_names = return_first_names(full_names)
# try:
#     assert first_names == ['Lauren', 'Drew', 'Alexander', 'Carol', 'Emma', 'Meng', 'Sizhe', 'Benjamin', 'Kendall', 'Lihao', 'Jacob', 'Yuanxue', 'Michelle', 'Lucas', 'Matthew', 'Andrea', 'Sujin', 'Ezgi', 'Zhuolun', 'Yan']
# except AssertionError:
#     print("Woops something's not right with your list")
# ```

# ## Exercise 2
# 
# In this more extended exercise, you'll be writing some code to count up vowels in lists of words

# In[44]:


vowels = ['a','e','i','o','u']
words = ['', 'rhythms', 'abracadabra', '12324', 'trysts','a','zebra', 'refrigerator']



# 1. Figure out which word in `words` has the most vowels. Your code should print out the element of the `words` list that contains the most vowels.
# 2. If you didn't use a function for part 1, define a function `count_vowels_in_string()` that takes in a string and outputs the number of vowels it has. Then use this function to compute which word has the most vowels. 
# 3. Update your code so that it now outputs  the word containing the most vowels *and* the number of vowels it contains.
# 4. Make sure your code can deal with a list that contains integers, not just strings. For example, `words` might contain the element 
# 
# 
# ```{admonitions} Challenge
# Does your code allow you to easily change the function from computing the maximum number to computing the minimum number? If not, think of an alternate solution that will let you do this.
# ```
