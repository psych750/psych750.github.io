#!/usr/bin/env python
# coding: utf-8

# # Python essentials to get you started

# ## Variable types and assignments

# Python is a dynamically typed language meaning that you don't have to declare the type of variable (string, integer, boolean, float, etc.) before assigning a value to it. For example, let's look at these 6 innanely-named variables.

# In[16]:


var_1 = "five"
var_2 = 5
var_3 = "5"
var_4 = 5.0
var_5 = True
var_6 = "True"


# Now let's print them out

# In[26]:


print('var_1 = ',var_1)
print('var_2 = ',var_2)
print('var_3 = ',var_3)
print('var_4 = ',var_4)
print('var_5 = ',var_5)
print('var_6 = ',var_6)


# Now let's print out the **types** of variables these are:

# In[25]:


print('var_1 = ',type(var_1))
print('var_2 = ',type(var_2))
print('var_3 = ',type(var_3))
print('var_4 = ',type(var_4))
print('var_5 = ',type(var_5))
print('var_6 = ',type(var_6))


# Notice that `var_2` and `var_3` have exactly the same printed value (5) as doe `var_5` and `var_6` (True), but they are of different types, e.g., `var_2` is an integer while `var_3` is a string. 
# 
# Does this matter? Yes it does! Have a look at what happens when we try to add 3 to `var_2` vs. `var_3`

# In[32]:


print(var_2+3)
print(var_3+3)


# The first one is 8 because... 5+3=8. The second one throws a TypeError because you tried to combine two types (a string and an integer) in a way that could not be resolved. The string '5' + the integer 3 is...???
# 
# 
# Now have a look at this. Try to predict what happens before looking at the output

# In[33]:


print(var_3+'3')


# What happened here?! The Python interpreter was asked to add the string '3' to the string '5'. A human is cognizant that these are numbers, but the Python interpreter doesn't care. To it, these are just text strings. What's a reasonable thing to do when asked to add two strings? Python defines string addition as **concatenation**, i.e.,`string1a+string2=string1string2`. That's why we get `52` (which is itself a string!!) as the answer.
# 
# So, in the context of numbers (integers and floats) `+` is arithmetic addition. In the context of strings, it's concatenation. This is called [operator overloading](https://www.geeksforgeeks.org/operator-overloading-in-python/)

# Now let's try this one. Let's *multiply* `var_2` and `var_3` by 3. What do you think will happen?

# In[35]:


print(var_2*3)
print(var_3*3)


# ## A bit more about printing

# Although printing is not something we'll be doing much of as an end in itself, it's massively useful for debugging your code, i.e., for knowing what a value of vertain variables is at a certain point in your code. We'll talk more about this when we discuss debugging. 
# 
# When you print, Python will try to convert what you are printing to a string. But if you try to print several different data types or combine the printing of strings and variables -- both of which is something you'll be doing a lot of when debugging -- it gets cumbersome. Observe:

# Simple enough:

# In[1]:


name = "George's dog"


# But what about this?

# In[3]:


name = "George"
print(name+"'s "+"dog")


# Yuck... that's a lot of quotes and figuring out where the spaces should go. 

# Python 3 provides a bit of "syntactic sugar" for printing combinations of raw strings and variables of different types:

# In[7]:


name = "George"
print(f"{name}'s dog")


# To use so-calld f (for formatted) strings, just encase the variables in curly-braces and write out raw strings as normal. Read more about these f-strings [here](https://realpython.com/python-f-strings/)

# ## Lists and iterating through them 

# A data structure you'll be using a whole lot in Python is a [list](https://learnpython.com/blog/python-array-vs-list/). For those coming from other programming languages, lists are largely the same as arrays, although Python lists can mix different types of variables. For example:

# In[37]:


a_list = [1, '1', 'two', 'three', 4]
print(a_list)
print(a_list[0], 'is a', type(a_list[0]))


# A common way of iterating through lists is by using a `for` loop. 

# In[38]:


animals = ['dog', 'cat', 'pig']
for animal in animals:
    print(animal)


# A common use of `for` loops is to do something a certain number of times. Fr example, let's print the first 10 integers, beginning from 0:

# In[9]:


for num in range(10):
    print(num)


# ```{dropdown} What happened here?
# `range()` generated a list of numbers in the specified range, beginning from 0. Then `for` iterates through those numbers, printing the value of each.
# ```

# ```{note}
# Technically range() returns a `range object` which is a ["lazy iterable"](https://treyhunner.com/2018/02/python-range-is-not-an-iterator/) and is executed only later, when we try to access its values. This is different from Python 2 where `range()` returns a regular list.
# ```

# ## A `while` loop

# Another kind of loop we'll use is a `while` loop. We use this to itereate until a condition is met (or is no longer met, as the case may be).

# In[41]:


another_num=5
while another_num <= 5 and another_num>0:
    print(f"I'm a {another_num} and I'm less than or equal to 5!")
    another_num -= 1


# In[42]:


s = ""
while len(s)<10: 
    s+="z"
    print(s)


# ```{note}
# `+=` is shorthand for add and self-assign, i.e., 
# s+="z" is equivalent to s = s+"z"
# ```

# ## A few simple conditionals (`if` statements)

# In[7]:


my_num = 5

if my_num == 5:
    print("it's a 5!")
else:
    print("it's not a 5!")


# In[6]:


if 5<2:
    print('yes indeed')
elif 10<2:
    print('this is true too!')


# Predict what each of these statements will return. Then check.

# In[61]:


my_num = '5'
if my_num == 5:
    print("it's a 5!")
else:
    print("it's not a 5!")


# In[13]:


print('s'==True)


# In[12]:


print(1==True)


# In[11]:


print (0==True)


# In[10]:


print (True==False)


# In[9]:


print ((True or False)==True)


# Let's end with a weird one...

# In[6]:


if print==True or print==False:
    print('all is good')
else:
    print('uh oh')


# In[9]:


print(type(print))
print(print==True)
print(print==False)

