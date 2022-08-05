#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc" style="margin-top: 1em;"><ul class="toc-item"><li><span><a href="#If-Statements" data-toc-modified-id="If-Statements-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>If Statements</a></span></li><li><span><a href="#What-is-an-if-statement?" data-toc-modified-id="What-is-an-if-statement?-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>What is an <em>if</em> statement?</a></span><ul class="toc-item"><li><span><a href="#Example" data-toc-modified-id="Example-2.1"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>Example</a></span><ul class="toc-item"><li><ul class="toc-item"><li><span><a href="#What-happens-in-this-program?" data-toc-modified-id="What-happens-in-this-program?-2.1.0.1"><span class="toc-item-num">2.1.0.1&nbsp;&nbsp;</span>What happens in this program?</a></span></li></ul></li></ul></li></ul></li><li><span><a href="#Logical-Tests" data-toc-modified-id="Logical-Tests-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Logical Tests</a></span><ul class="toc-item"><li><ul class="toc-item"><li><span><a href="#Whitespace" data-toc-modified-id="Whitespace-3.0.1"><span class="toc-item-num">3.0.1&nbsp;&nbsp;</span>Whitespace</a></span></li></ul></li><li><span><a href="#Equality" data-toc-modified-id="Equality-3.1"><span class="toc-item-num">3.1&nbsp;&nbsp;</span>Equality</a></span></li><li><span><a href="#Inequality" data-toc-modified-id="Inequality-3.2"><span class="toc-item-num">3.2&nbsp;&nbsp;</span>Inequality</a></span></li><li><span><a href="#Other-Inequalities" data-toc-modified-id="Other-Inequalities-3.3"><span class="toc-item-num">3.3&nbsp;&nbsp;</span>Other Inequalities</a></span><ul class="toc-item"><li><span><a href="#greater-than" data-toc-modified-id="greater-than-3.3.1"><span class="toc-item-num">3.3.1&nbsp;&nbsp;</span>greater than</a></span></li><li><span><a href="#greater-than-or-equal-to" data-toc-modified-id="greater-than-or-equal-to-3.3.2"><span class="toc-item-num">3.3.2&nbsp;&nbsp;</span>greater than or equal to</a></span></li><li><span><a href="#less-than" data-toc-modified-id="less-than-3.3.3"><span class="toc-item-num">3.3.3&nbsp;&nbsp;</span>less than</a></span></li><li><span><a href="#less-than-or-equal-to" data-toc-modified-id="less-than-or-equal-to-3.3.4"><span class="toc-item-num">3.3.4&nbsp;&nbsp;</span>less than or equal to</a></span></li></ul></li><li><span><a href="#Checking-if-an-item-is-in-a-list" data-toc-modified-id="Checking-if-an-item-is-in-a-list-3.4"><span class="toc-item-num">3.4&nbsp;&nbsp;</span>Checking if an item is <strong>in</strong> a list</a></span></li></ul></li><li><span><a href="#The-if-elif...else-chain" data-toc-modified-id="The-if-elif...else-chain-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>The if-elif...else chain</a></span><ul class="toc-item"><li><span><a href="#Simple-if-statements" data-toc-modified-id="Simple-if-statements-4.1"><span class="toc-item-num">4.1&nbsp;&nbsp;</span>Simple if statements</a></span></li><li><span><a href="#if-else-statements" data-toc-modified-id="if-else-statements-4.2"><span class="toc-item-num">4.2&nbsp;&nbsp;</span>if-else statements</a></span></li><li><span><a href="#if-elif...else-chains" data-toc-modified-id="if-elif...else-chains-4.3"><span class="toc-item-num">4.3&nbsp;&nbsp;</span>if-elif...else chains</a></span></li></ul></li><li><span><a href="#More-than-one-passing-test" data-toc-modified-id="More-than-one-passing-test-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>More than one passing test</a></span></li><li><span><a href="#True-and-False-values" data-toc-modified-id="True-and-False-values-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>True and False values</a></span></li></ul></div>

# If Statements
# ===
# By allowing you to respond selectively to different situations and conditions, if statements open up whole new possibilities for your programs. In this section, you will learn how to test for certain conditions, and then respond in appropriate ways to those conditions.

# What is an *if* statement?
# ===
# An *if* statement tests for a condition, and then responds to that condition. If the condition is true, then whatever action is listed next gets carried out. You can test for multiple conditions at the same time, and respond appropriately to each condition.
# 
# Example
# ---
# Here is an example that shows a number of the desserts I like. It lists those desserts, but lets you know which one is my favorite.

# In[3]:


# A list of desserts I like.
desserts = ['ice cream', 'chocolate', 'apple crisp', 'cookies']
favorite_dessert = 'apple crisp'

# Print the desserts out, but let everyone know my favorite dessert.
for dessert in desserts:
    if dessert == favorite_dessert:
        # This dessert is my favorite, let's let everyone know!
        print dessert, "is my favorite dessert!"
    else:
        # I like these desserts, but they are not my favorite.
        print "I like", dessert


# #### What happens in this program?
# 
# - The program starts out with a list of desserts, and one dessert is identified as a favorite.
# - The for loop runs through all the desserts.
# - Inside the for loop, each item in the list is tested.
#     - If the current value of *dessert* is equal to the value of *favorite_dessert*, a message is printed that this is my favorite.
#     - If the current value of *dessert* is not equal to the value of *favorite_dessert*, a message is printed that I just like the dessert.
#     
# You can test as many conditions as you want in an if statement, as you will see in a little bit.

# [top](#)

# Logical Tests
# ===
# Every if statement evaluates to *True* or *False*. *True* and *False* are Python keywords, which have special meanings attached to them. You can test for the following conditions in your if statements:
# 
# - [equality](#equality) (==)
# - [inequality](#inequality) (!=)
# - [other inequalities](#other_inequalities)
#     - greater than (>)
#     - greater than or equal to (>=)
#     - less than (<)
#     - less than or equal to (<=)
# - [You can test if an item is **in** a list.](#in_list)
# 
# ### Whitespace
# There is a [section of PEP 8](http://www.python.org/dev/peps/pep-0008/#other-recommendations) that tells us it's a good idea to put a single space on either side of all of these comparison operators. If you're not sure what this means, just follow the style of the examples you see below.

# Equality
# ---
# Two items are *equal* if they have the same value. You can test for equality between numbers, strings, and a number of other objects which you will learn about later. Some of these results may be surprising, so take a careful look at the examples below.
# 
# In Python, as in many programming languages, two equals signs tests for equality.
# 
# **Watch out!** Be careful of accidentally using one equals sign, which can really throw things off because that one equals sign actually sets your item to the value you are testing for!

# In[3]:


5 == 5


# In[4]:


3 == 5 


# In[24]:


5 == 5.0


# In[8]:


'eric' == 'eric'


# In[9]:


'Eric' == 'eric'


# In[10]:


'Eric'.lower() == 'eric'.lower()


# In[11]:


'5' == 5


# In[12]:


'5' == str(5)


# [top](#)

# Inequality
# ---
# Two items are *inequal* if they do not have the same value. In Python, we test for inequality using the exclamation point and one equals sign.
# 
# Sometimes you want to test for equality and if that fails, assume inequality. Sometimes it makes more sense to test for inequality directly.

# In[13]:


3 != 5


# In[14]:


5 != 5


# In[18]:


'Eric' != 'eric'


# [top](#)

# Other Inequalities
# ---
# ### greater than

# In[16]:


5 > 3


# ### greater than or equal to

# In[19]:


5 >= 3


# In[20]:


3 >= 3


# ### less than

# In[21]:


3 < 5


# ### less than or equal to

# In[22]:


3 <= 5


# In[23]:


3 <= 3


# [top](#)

# Checking if an item is **in** a list
# ---
# You can check if an item is in a list using the **in** keyword.

# In[25]:


vowels = ['a', 'e', 'i', 'o', 'u']
'a' in vowels


# In[26]:


vowels = ['a', 'e', 'i', 'o', 'u']
'b' in vowels


# You can check if an item is *not* in a list using `not in`

# In[4]:


vowels = ['a', 'e', 'i', 'o', 'u']
'm' not in vowels


# [top](#)

# The if-elif...else chain
# ===
# You can test whatever series of conditions you want to, and you can test your conditions in any combination you want.

# Simple if statements
# ---
# The simplest test has a single **if** statement, and a single statement to execute if the condition is **True**.

# In[27]:


dogs = ['willie', 'hootz', 'peso', 'juno']

if len(dogs) > 3:
    print("Wow, we have a lot of dogs here!")


# In this situation, nothing happens if the test does not pass.

# In[28]:


dogs = ['willie', 'hootz']

if len(dogs) > 3:
    print("Wow, we have a lot of dogs here!")


# Notice that there are no errors. The condition `len(dogs) > 3` evaluates to False, and the program moves on to any lines after the **if** block.

# if-else statements
# ---
# Many times you will want to respond in two possible ways to a test. If the test evaluates to **True**, you will want to do one thing. If the test evaluates to **False**, you will want to do something else. The **if-else** structure lets you do that easily. Here's what it looks like:

# In[30]:


dogs = ['willie', 'hootz', 'peso', 'juno']

if len(dogs) > 3:
    print("Wow, we have a lot of dogs here!")
else:
    print("Okay, this is a reasonable number of dogs.")


# Our results have not changed in this case, because if the test evaluates to **True** only the statements under the **if** statement are executed. The statements under **else** area only executed if the test fails:

# In[31]:


dogs = ['willie', 'hootz']

if len(dogs) > 3:
    print("Wow, we have a lot of dogs here!")
else:
    print("Okay, this is a reasonable number of dogs.")


# The test evaluated to **False**, so only the statement under `else` is run.

# if-elif...else chains
# ---
# Many times, you will want to test a series of conditions, rather than just an either-or situation. You can do this with a series of if-elif-else statements
# 
# There is no limit to how many conditions you can test. You always need one if statement to start the chain, and you can never have more than one else statement. But you can have as many elif statements as you want.

# In[32]:


dogs = ['willie', 'hootz', 'peso', 'monty', 'juno', 'turkey']

if len(dogs) >= 5:
    print("Holy mackerel, we might as well start a dog hostel!")
elif len(dogs) >= 3:
    print("Wow, we have a lot of dogs here!")
else:
    print("Okay, this is a reasonable number of dogs.")


# It is important to note that in situations like this, only the first test is evaluated. In an if-elif-else chain, once a test passes the rest of the conditions are ignored.

# In[33]:


dogs = ['willie', 'hootz', 'peso', 'monty']

if len(dogs) >= 5:
    print("Holy mackerel, we might as well start a dog hostel!")
elif len(dogs) >= 3:
    print("Wow, we have a lot of dogs here!")
else:
    print("Okay, this is a reasonable number of dogs.")


# The first test failed, so Python evaluated the second test. That test passed, so the statement corresponding to `len(dogs) >= 3` is executed.

# In[34]:


dogs = ['willie', 'hootz']

if len(dogs) >= 5:
    print("Holy mackerel, we might as well start a dog hostel!")
elif len(dogs) >= 3:
    print("Wow, we have a lot of dogs here!")
else:
    print("Okay, this is a reasonable number of dogs.")


# In this situation, the first two tests fail, so the statement in the else clause is executed. Note that this statement would be executed even if there are no dogs at all:

# In[35]:


dogs = []

if len(dogs) >= 5:
    print("Holy mackerel, we might as well start a dog hostel!")
elif len(dogs) >= 3:
    print("Wow, we have a lot of dogs here!")
else:
    print("Okay, this is a reasonable number of dogs.")


# Note that you don't have to take any action at all when you start a series of if statements. You could simply do nothing in the situation that there are no dogs by replacing the `else` clause with another `elif` clause:

# In[36]:


dogs = []

if len(dogs) >= 5:
    print("Holy mackerel, we might as well start a dog hostel!")
elif len(dogs) >= 3:
    print("Wow, we have a lot of dogs here!")
elif len(dogs) >= 1:
    print("Okay, this is a reasonable number of dogs.")


# In this case, we only print a message if there is at least one dog present. Of course, you could add a new `else` clause to respond to the situation in which there are no dogs at all:

# In[37]:


dogs = []

if len(dogs) >= 5:
    print("Holy mackerel, we might as well start a dog hostel!")
elif len(dogs) >= 3:
    print("Wow, we have a lot of dogs here!")
elif len(dogs) >= 1:
    print("Okay, this is a reasonable number of dogs.")
else:
    print("I wish we had a dog here.")


# As you can see, the if-elif-else chain lets you respond in very specific ways to any given situation.

# [top](#)

# More than one passing test
# ===
# In all of the examples we have seen so far, only one test can pass. As soon as the first test passes, the rest of the tests are ignored. This is really good, because it allows our code to run more efficiently. Many times only one condition can be true, so testing every condition after one passes would be meaningless.
# 
# There are situations in which you want to run a series of tests, where every single test runs. These are situations where any or all of the tests could pass, and you want to respond to each passing test. Consider the following example, where we want to greet each dog that is present:

# In[38]:


dogs = ['willie', 'hootz']

if 'willie' in dogs:
    print("Hello, Willie!")
if 'hootz' in dogs:
    print("Hello, Hootz!")
if 'peso' in dogs:
    print("Hello, Peso!")
if 'monty' in dogs:
    print("Hello, Monty!")


# If we had done this using an if-elif-else chain, only the first dog that is present would be greeted:

# In[41]:


dogs = ['willie', 'hootz']

if 'willie' in dogs:
    print("Hello, Willie!")
elif 'hootz' in dogs:
    print("Hello, Hootz!")
elif 'peso' in dogs:
    print("Hello, Peso!")
elif 'monty' in dogs:
    print("Hello, Monty!")


# Of course, this could be written much more cleanly using lists and for loops. See if you can follow this code.

# In[1]:


dogs_we_know = ['willie', 'hootz', 'peso', 'monty', 'juno', 'turkey']
dogs_present = ['willie', 'hootz']

# Go through all the dogs that are present, and greet the dogs we know.
for dog in dogs_present:
    if dog in dogs_we_know:
        print "Hello", dog.title()


# This is the kind of code you should be aiming to write. It is fine to come up with code that is less efficient at first. When you notice yourself writing the same kind of code repeatedly in one program, look to see if you can use a loop or a function to make your code more efficient.

# [top](#)

# True and False values
# ===
# Every value can be evaluated as True or False. The general rule is that any non-zero or non-empty value will evaluate to True. If you are ever unsure, you can open a Python terminal and write two lines to find out if the value you are considering is True or False. Take a look at the following examples, keep them in mind, and test any value you are curious about. I am using a slightly longer test just to make sure something gets printed each time.

# In[60]:


if 0:
    print("This evaluates to True.")
else:
    print("This evaluates to False.")


# In[61]:


if 1:
    print("This evaluates to True.")
else:
    print("This evaluates to False.")


# In[62]:


# Arbitrary non-zero numbers evaluate to True.
if 1253756:
    print("This evaluates to True.")
else:
    print("This evaluates to False.")


# In[63]:


# Negative numbers are not zero, so they evaluate to True.
if -1:
    print("This evaluates to True.")
else:
    print("This evaluates to False.")


# In[64]:


# An empty string evaluates to False.
if '':
    print("This evaluates to True.")
else:
    print("This evaluates to False.")


# In[66]:


# Any other string, including a space, evaluates to True.
if ' ':
    print("This evaluates to True.")
else:
    print("This evaluates to False.")


# In[67]:


# Any other string, including a space, evaluates to True.
if 'hello':
    print("This evaluates to True.")
else:
    print("This evaluates to False.")


# In[68]:


# None is a special object in Python. It evaluates to False.
if None:
    print("This evaluates to True.")
else:
    print("This evaluates to False.")


# [top](#)
