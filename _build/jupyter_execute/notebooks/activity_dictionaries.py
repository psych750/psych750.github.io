#!/usr/bin/env python
# coding: utf-8

# # Dictionary Exercises

# ## Selective dictionary access

# Given the following dictionary, find the mean value of the keys that begin with a vowel.
# 
# ```Python
# a_dict = 
# {'--': 2,
#  'Air': 3,
#  'At': 2,
#  'Big': 3,
#  'But': 3,
#  'Figure': 6,
#  'Freestyle': 9,
#  'Olympics': 8,
#  'Pyeongchang,': 12,
#  'Skating.': 8,
#  'Skiing': 6,
#  'Snowboarding': 12,
#  'To': 2,
#  'Winter': 6,
#  'a': 1,
#  'air.': 4,
#  'and': 3,
#  'body': 4,
#  'corks': 5,
#  'do': 2,
#  'four': 4,
#  'got': 3,
#  'have': 4,
#  'in': 2,
#  'jumps': 5,
#  'less': 4,
#  'limit': 5,
#  'may': 3,
#  'of': 2,
#  'or': 2,
#  'possible?': 9,
#  'quad': 4,
#  'quad,': 5,
#  'reached': 7,
#  'second': 6,
#  'see': 3,
#  "skater's": 8,
#  'than': 4,
#  'the': 3,
#  'their': 5,
#  'this': 4,
#  'times': 5,
#  'to': 2,
#  'turn': 4,
#  'twists': 6,
#  'we': 2,
#  "we'll": 5,
#  "what's": 6,
#  "year's": 6}
# ```
# 
#  Here's some code to help get you started:

# In[4]:


import numpy as np

vowels = ['a','e','i','o','u']

def isVowel(letter):
    return letter in vowels

def isVowelOnset(string):
    return isVowel(string[0])

#to find a mean of a list, use the mean() function from the numpy library
print(np.mean(range(10)))
#it is commonly imported as np so that you can type np.mean() instead of numpy.mean()


# ```{note}```
# By taking advantage of statements that already return True/False values, the code above avoids having to have code like: if X return True, else return Y.
# ```

# ### Selective access continued
# 
# Now do the same for consonants
# 
# <div class="alert alert-block alert-info">
# Hint: You don't need to write separate isConsonant/isConsonantOnset functions!</div>
# 

# ## Letter counts
# 
# Complete the implementation of the function `letter_counts()` which receives a string as input and returns a dictionary with (lowercase) letters as keys and their respective counts as values.

# In[3]:


def letter_counts(string):
    letter_sums = {}
    letters = [letter for letter in string.lower() if c.isalpha()]
    for curLetter in letters:
        pass
    
    return letter_sums

#Replace pass with appropriate code to make the function work. You only need a couple lines of code.


# ### Test your letter_counts function

# In[2]:


letter_counts("Complete the implementation of the function. `letter_counts()` receives a string as input and returns a dictionary with (lowercase) letters and their respective counts. The keys are the letters and the counts are how many times a given letter occurred.")
```python
{'a': 12, 'c': 10, 'e': 32, 'd': 4, 'g': 1, 'f': 1, 'i': 12, 'h': 7, 'k': 0, 'm': 4, 'l': 6, 'o': 10, 'n': 15, 'p': 3, 's': 12, 'r': 15, 'u': 6, 't': 27, 'w': 2, 'v': 2, 'y': 2}
```


# ## Given a string, find the n most/least frequent letters in it

# In[ ]:



def most_frequent(string,n):
    pass

def least_frequent(string,n):
    pass


# ### Test most_frequent() and least_frequent() 

# In[ ]:


a_string = "At this year's Winter Olympics in Pyeongchang, we may see quad corks in Big Air Snowboarding or in Freestyle Skiing -- and we'll see quad twists and quad jumps in Figure Skating. But have we reached the limit of what's possible? To do a quad, a skater's got less than a second to turn their body four times in the air."

>most_frequent(a_string,3)
#should return [('e', 24), ('a', 21), ('i', 21)]

>least_frequent(a_string,4)
# should return [('j', 0), ('v', 0), ('f', 3)]


# ## Bonus: Calculate most/least frequent letters in words beginning with consonants or vowels

# Implement `most_frequent2()` which makes the following function-called produce the desired results:
# 
# ```Python
# def most_frequent2(string,n):
# ''' Given a string, return the n most frequent letters occurring in words beginning with vowels.
# '''
#     pass
# 
# def least_frequent2(string,n):
# ''' Given a string, return the n least frequent letters occurring in words beginning with vowels
# '''
#     pass
# ```
# 

# ### Test most_frequent2() and least_frequent2()

# In[ ]:


a_string = "At this year's Winter Olympics in Pyeongchang, we may see quad corks in Big Air Snowboarding or in Freestyle Skiing -- and we'll see quad twists and quad jumps in Figure Skating. But have we reached the limit of what's possible? To do a quad, a skater's got less than a second to turn their body four times in the air."

most_frequent2(a_string,3)
#should return [('n', 6), ('a', 5), ('i', 5)]

least_frequent2(a_string,3)
#should return [('f', 0), ('d', 1), ('o', 1)]

