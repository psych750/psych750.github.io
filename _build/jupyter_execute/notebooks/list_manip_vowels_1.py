#!/usr/bin/env python
# coding: utf-8

# # List/string manipulation exercise
# 
# For this exercise, you'll be writing some code to count up vowels in lists of words

# In[44]:


vowels = ['a','e','i','o','u']
words = ['', 'rhythms', 'abracadabra', '12324', 'trysts','a','zebra', 'refrigerator']


# 1. Figure out which word in `words` has the most vowels. Your code should print out the word in`words` containing the most vowels
# 2. If you didn't use a function for part 1, define a function `count_vowels_in_string()` that takes in a string and outputs the number of vowels it has. Then use this function to compute which word has the most vowels. 
# 3. Update your code so that it now outputs  the word containing the most vowels *and* the number of vowels it contains.
# 4. Make sure your code can deal with a list that contains integers, not just strings. For example, `words` might contain the element 
# 
# 
# ```{admonitions} Challenge
# Does your code allow you to easily change the function from computing the maximum number to computing the minimum number? If not, think of an alternate solution that will let you do this.
# ```
