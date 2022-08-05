#!/usr/bin/env python
# coding: utf-8

# # Python essentials to get you started

# ## Assigning a variable and printing its value

# In[3]:


my_string = "I am a string"
my_num = 5

print(type(my_string))
print(type(my_num))
print("Hello world")
print(my_string, "and I'm a", my_num)


# Or for a more compact printing when you need to intermix fixed strings and variables:

# In[3]:


print(f"{my_string} and I'm a {my_num}")


# In[ ]:


print()


# ## Iterating through a list using a `for` loop

# In[3]:


print range(10)
for num in range(10):
    print num


# ```{dropdown} What happened here?
# As the first line shows, `range()` generated a list of numbers in the specified range. Then `for` iterated through those numbers.```
# 

# ### Another `for` loop

# In[5]:


animals = ['dog', 'cat', 'pig']
for animal in animals:
    print(animal)


# ## A few simple conditionals (`if` statements)

# In[7]:


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


# In[8]:


print (print==True)


# ## A `while` loop

# In[14]:


another_num=5
while another_num <= 5 and another_num>0:
    print(f"I'm a {another_num} and I'm less than or equal to 5!")
    another_num -= 1

