#!/usr/bin/env python
# coding: utf-8

# # Debugging practice
# 
# Debugging your code is an inescapable part of coding just like revising your writing is an inescapable part of writing. These exercises are designd to help you practice your debugging skills while demonstrating a few common pitfalls.
# 

# This bit of code is supposed to iterate through a shuffled list. Why is it not working?

# In[5]:


vowels = ['a','e','i','o','u']
for cur_vowel in random.shuffle(vowels):
	print(cur_vowel)


# `Sets` are like lists except they allow us to perform set operations like union, intersection, difference etc. Unlike lists which have no restrictions on duplicated elements, a set -- by definition -- only contains unique elements. Because sets are implemented in a very efficient way, we can use them to remove duplicates from a list. For example:

# In[6]:


list_with_duplicates = ['dog', 'cat', 'wolf', 'dog']
print(list_with_duplicates)
print(list(set(list_with_duplicates))) #voila, duplicates gone!


# I'm trying to do something similar here, but running into a problem. Help!

# In[7]:


list = ['violin', 'guitar', 'guitar', 'piano']
print(list(set(list))) #voila, duplicates gone?


# I'm trying to iterate through a list, check if each element is a palindrom (reads the same backwards and forwards), and if it's not, remove it from the list so that I only have palindromes at the end. The palindrome checker is working... but something else is not..

# In[24]:


def is_palindrome(str):
    str = str.replace(' ','') # remove spaces
    return str == str[::-1]

list_of_strings = ['dog', 'rotator', 'dod', 'cat', 'kayak', 'malyalam', 'a man a plan a canal panama']

for cur_elt,cur_string in enumerate(list_of_strings):
    if not is_palindrome(cur_string):
        list_of_strings.remove(cur_elt)


# I'm trying to access the last item from a list using index, but something is wrong. What happened?
# 

# In[9]:


thisList = ['violin', 'guitar', 'saxophone', 'piano','cello']
thisList[5]


# Now instead of a list, I'm trying to access a key from a dictionary, and it's not working

# In[13]:


thisDict = {
    'brand':['Alfa Romeo','BMW','Chevrolet','Dodge'],
    'year':[2018,2023,1997,1969],
    'model':['Stelvio','M3','Corvette','Challenger']
}

thisDict['modle']


# I'm trying to access a variable but the program keeps throwing this error at me. What is going on?

# In[11]:


def myFunction(x):
    y = x + 3
    z = x + 5
    return y

a = 5
b = myFunction(a)
print(z)


# I'm trying to create a function that multiplies the number I input by 3, but why does it result in `None`? And why can't I print x??

# In[31]:


def multiplyByThree(x):
    x *= 3

a = 5
b = multiplyByThree(a)
print(b)
print(x)

