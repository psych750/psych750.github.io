#!/usr/bin/env python
# coding: utf-8

# # Debugging practice
# 
# Debugging your code is an inescapable part of coding just like revising your writing is an inescapable part of writing. These exercises are designd to help you practice your debugging skills while demonstrating a few common pitfalls.
# 

# 1. This bit of code is supposed to iterate through a shuffled list. Why is it not working?

# In[7]:


import random
vowels = ['a','e','i','o','u']
random.shuffle(vowels)
print(vowels)

for cur_vowel in vowels:
	print(cur_vowel)


# 2. `Sets` are like lists except they allow us to perform set operations like union, intersection, difference etc. Unlike lists which have no restrictions on duplicated elements, a set -- by definition -- only contains unique elements. Because sets are implemented in a very efficient way, we can use them to remove duplicates from a list. For example:

# In[9]:


list_with_duplicates = ['dog', 'cat', 'wolf', 'dog', 'dog']
print(list_with_duplicates)
print(list(set(list_with_duplicates))) #voila, duplicates gone!


# I'm trying to do something similar here, but running into a problem. Help!

# In[16]:


duplicated_list = ['violin', 'guitar', 'guitar', 'piano']
print(list(set(duplicated_list))) #voila, duplicates gone?


# 4. I'm trying to iterate through a list, check if each element is a palindrome (reads the same backwards and forwards), and if it's not, remove it from the list so that I only have palindromes at the end. The palindrome checker is working... but something else is not..

# In[39]:


def is_palindrome(str):
    str = str.replace(' ','') # remove spaces
    return str == str[::-1]

list_of_strings = ['dog', 'rotator', 'dod', 'cat', 'kayak', 'malyalam', 'a man a plan a canal panama']

for cur_elt,cur_string in enumerate(list_of_strings):
    if not is_palindrome(cur_string):
        list_of_strings.remove(cur_elt)


# 5. I'm trying to iterate through a list, but something is wrong. What happened?
# 

# In[26]:


myList = []
for i in range(10):
    myList.append(i)

listSize = len(myList)
for index in range(listSize+1):
    print(myList[index])


# 6. Now instead of a list, I'm trying to iterate through a dictionary and print out the various car models stored inside it. Why isn't it working?

# In[28]:


thisDict = {
    'brand':['Alfa Romeo','BMW','Chevrolet','Dodge'],
    'year':[2018,2023,1997,1969],
    'model':['Stelvio','M3','Corvette','Challenger'],
    'color':['black','green','red','black'],
    'horsepower':[280,473,345,425]
}

for index in range(len(thisDict['model'])):
    print(thisDict['model'][index])


# 7. The function I defined is doing two addition operations. I'm trying to access the result of one of the additions, but Python keeps throwing an error at me. What is going on?

# In[31]:


def myFunction(x):
    y = x + 3
    z = x + 5
    return y

y = 5
b = myFunction(y)
print(b)



# 8. I'm trying to create a function that multiplies the number I input by 3, but why does it result in `None`? And why can't I print x??

# In[34]:


def multiplyByThree(x):
    x *= 3
    print(x)
    return x

a = 5
b = multiplyByThree(a)
print(b)
print(x)

