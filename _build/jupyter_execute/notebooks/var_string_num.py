#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc" style="margin-top: 1em;"><ul class="toc-item"><li><span><a href="#Variables,-Strings,-and-Numbers" data-toc-modified-id="Variables,-Strings,-and-Numbers-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Variables, Strings, and Numbers</a></span></li><li><span><a href="#Variables" data-toc-modified-id="Variables-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Variables</a></span><ul class="toc-item"><li><span><a href="#Example" data-toc-modified-id="Example-2.1"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>Example</a></span></li><li><span><a href="#Naming-rules" data-toc-modified-id="Naming-rules-2.2"><span class="toc-item-num">2.2&nbsp;&nbsp;</span>Naming rules</a></span></li><li><span><a href="#NameError" data-toc-modified-id="NameError-2.3"><span class="toc-item-num">2.3&nbsp;&nbsp;</span>NameError</a></span></li></ul></li><li><span><a href="#Strings" data-toc-modified-id="Strings-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Strings</a></span><ul class="toc-item"><li><span><a href="#Single-and-double-quotes" data-toc-modified-id="Single-and-double-quotes-3.1"><span class="toc-item-num">3.1&nbsp;&nbsp;</span>Single and double quotes</a></span></li><li><span><a href="#Getting-a-string's-length-and-checking-for-character" data-toc-modified-id="Getting-a-string's-length-and-checking-for-character-3.2"><span class="toc-item-num">3.2&nbsp;&nbsp;</span>Getting a string's length and checking for character</a></span></li><li><span><a href="#Changing-case" data-toc-modified-id="Changing-case-3.3"><span class="toc-item-num">3.3&nbsp;&nbsp;</span>Changing case</a></span></li><li><span><a href="#Combining-strings-(concatenation)" data-toc-modified-id="Combining-strings-(concatenation)-3.4"><span class="toc-item-num">3.4&nbsp;&nbsp;</span>Combining strings (concatenation)</a></span></li><li><span><a href="#Whitespace" data-toc-modified-id="Whitespace-3.5"><span class="toc-item-num">3.5&nbsp;&nbsp;</span>Whitespace</a></span><ul class="toc-item"><li><span><a href="#Stripping-whitespace" data-toc-modified-id="Stripping-whitespace-3.5.1"><span class="toc-item-num">3.5.1&nbsp;&nbsp;</span>Stripping whitespace</a></span></li></ul></li></ul></li><li><span><a href="#Numbers" data-toc-modified-id="Numbers-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Numbers</a></span><ul class="toc-item"><li><span><a href="#Floating-Point-numbers" data-toc-modified-id="Floating-Point-numbers-4.1"><span class="toc-item-num">4.1&nbsp;&nbsp;</span>Floating-Point numbers</a></span></li><li><span><a href="#Integers-in-Python-2.7" data-toc-modified-id="Integers-in-Python-2.7-4.2"><span class="toc-item-num">4.2&nbsp;&nbsp;</span>Integers in Python 2.7</a></span><ul class="toc-item"><li><span><a href="#Division-in-Python-2.7" data-toc-modified-id="Division-in-Python-2.7-4.2.1"><span class="toc-item-num">4.2.1&nbsp;&nbsp;</span>Division in Python 2.7</a></span></li><li><span><a href="#Division-in-Python-3.3" data-toc-modified-id="Division-in-Python-3.3-4.2.2"><span class="toc-item-num">4.2.2&nbsp;&nbsp;</span>Division in Python 3.3</a></span></li></ul></li></ul></li><li><span><a href="#Comments" data-toc-modified-id="Comments-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Comments</a></span><ul class="toc-item"><li><span><a href="#What-makes-a-good-comment?" data-toc-modified-id="What-makes-a-good-comment?-5.1"><span class="toc-item-num">5.1&nbsp;&nbsp;</span>What makes a good comment?</a></span></li><li><span><a href="#When-should-you-write-comments?" data-toc-modified-id="When-should-you-write-comments?-5.2"><span class="toc-item-num">5.2&nbsp;&nbsp;</span>When should you write comments?</a></span></li></ul></li><li><span><a href="#Zen-of-Python" data-toc-modified-id="Zen-of-Python-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>Zen of Python</a></span></li></ul></div>

# Variables, Strings, and Numbers
# ===
# In this section, you will learn to store information in variables. You will learn about three types of data: strings, which are lists of characters, integers, which are numbers like 2 and 3,  and floats, which are numbers like 2.0 and 2.5.

# Variables
# ===
# A variable holds a value.

# Example
# ---

# In[16]:


message = "Hello world!"
print(message)


# A variable holds a value. You can change the value of a variable at any point. When you do, the original value is overwritten.

# In[2]:


message = "Hello world!"
print(message)

message = "I'm learning to program"
print(message)


# Naming rules
# ---
# - Variable names can only have letters, numbers, and underscores. Variable names can start with a letter or an underscore, but cannot start with a number.
# - Spaces are not allowed in variable names, so we use underscores instead of spaces. For example, use student_name instead of "student name".
# - You cannot use [Python keywords](http://docs.python.org/2/reference/lexical_analysis.html#keywords) as variable names.
# - Variable names should be descriptive, without being too long. For example, `cur_trial` is better than just `trial`, and `my_current_trial`.
# - Be careful about using the lowercase letter l and the uppercase letter O in places where they could be confused with the numbers 1 and 0.
# - Python conventions dictate separating naming clauses with underscores (e.g., `cur_trial`). An alternate naming convention, and one that I will use in the class because of old habits is *mixed case* (e.g., `curTrial`)

# NameError
# ---
# There is one common error when using variables, that you will almost certainly encounter at some point. Take a look at this code, and see if you can figure out why it causes an error.

# In[12]:


message = "Thank you for sharing Python with the world, Guido!"
print(mesage)


# Let's look through this error message. First, we see it is a NameError. Then we see the file that caused the error, and a green arrow shows us what line in that file caused the error. Then we get some more specific feedback, that "name 'mesage' is not defined".
# 
# You may have already spotted the source of the error. We spelled message two different ways. Python does not care whether we use the variable name "message" or "mesage". Python only cares that the spellings of our variable names match every time we use them.
# 
# This is pretty important, because it allows us to have a variable "name" with a single name in it, and then another variable "names" with a bunch of names in it.
# 
# We can fix NameErrors by making sure all of our variable names are spelled consistently.
# 
# <div class="alert alert-block alert-info">
# Nearly in every case, capitalization matters! The variable names `message`, `Message`, and `messagE` are -- to Python -- as different from one another as `message` and `rhinoceros` Of course to *humans* `message` and `Message` are quite similar and liable to get confused, which is a reason to not use variable names that differ only in capitalization!</div>
# 
# 

# In[1]:


message = "Thank you for making Python, Guido!"
print(message)


# [Guido](http://en.wikipedia.org/wiki/Guido_van_Rossum) [van Rossum](http://www.python.org/~guido/) created the Python language over 20 years ago, and he is considered Python's [Benevolent Dictator for Life](http://en.wikipedia.org/wiki/Benevolent_Dictator_for_Life). Guido still signs off on all major changes to the core Python language.

# [top](#)

# Strings
# ===
# Strings are lists of characters. Let's look at some examples.

# Single and double quotes
# ---
# Strings are contained by either single or double quotes.

# In[ ]:


my_string = "This is a double-quoted string."
my_string = 'This is a single-quoted string.'


# This lets us make strings that contain quotations.

# In[ ]:


quote = "Linus Torvalds once said, 'Any program is only as good as it is useful.'"


# What if we want to have a string with both single and double quotes in it? The following won't work. Can you see why?

# In[3]:


my_string = "Here's a string with a "quote in it""
print my_string


# To make it work we have to "escape" the quotes that would otherwise tell the Python interpreter that ths string is to be terminated.

# In[4]:


my_string = "Here's a string with a \"quote in it\""
print my_string


# Getting a string's length and checking if something exists
# ---
# Remember how we said that strings are lists of characters? We'll learn more about lists in the next section, but for now, just note that because they're lists, you can do the following:

# In[1]:


print "There are",len('aeiou'), "vowels in English"


# In[4]:


if 'e' in 'aeiou':
    print "yep, there's an e"


# We'll cover more complex string searches later in the semester.

# In[ ]:


print 'f' in 'aeiou'


# Changing case
# ---
# You can easily change the case of a string, to present it the way you want it to look.

# In[4]:


first_name = 'eric'

print(first_name)
print(first_name.title())


# It is often good to store data in lower case, and then change the case as you want to for presentation. This catches some TYpos. It also makes sure that 'eric', 'Eric', and 'ERIC' are not considered three different people.
# 
# Some of the most common cases are lower, title, and upper.

# In[6]:


first_name = 'eric'

print(first_name)
print(first_name.title())
print(first_name.upper())

first_name = 'Eric'
print(first_name.lower())


# You will see this syntax quite often, where a variable name is followed by a dot and then the name of an action, followed by a set of parentheses. The parentheses may be empty, or they may contain some values.
# 
# variable_name.action()
# 
# In this example, the word "action" is the name of a method. A method is something that can be done to a variable. The methods 'lower', 'title', and 'upper' are all functions that have been written into the Python language, which do something to strings. Later on, you will learn to write your own methods.

# Combining strings (concatenation)
# ---
# It is often very useful to be able to combine strings into a message or page element that we want to display. Again, this is easier to understand through an example.

# In[8]:


first_name = 'ada'
last_name = 'lovelace'

full_name = first_name + ' ' + last_name

print(full_name.title())


# The plus sign combines two strings into one, which is called "concatenation". You can use as many plus signs as you want in composing messages. In fact, many web pages are written as giant strings which are put together through a long series of string concatenations.

# In[9]:


first_name = 'ada'
last_name = 'lovelace'
full_name = first_name + ' ' + last_name

message = full_name.title() + ' ' + "was considered the world's first computer programmer."

print(message)


# If you don't know who Ada Lovelace is, you might want to go read what [Wikipedia](http://en.wikipedia.org/wiki/Ada_Lovelace) or the [Computer History Museum](http://www.computerhistory.org/babbage/adalovelace/) have to say about her. Her life and her work are also the inspiration for the [Ada Initiative](http://adainitiative.org/faq/about-ada-lovelace/).

# Whitespace
# ---
# The term "whitespace" refers to characters that the computer is aware of, but are invisible to readers. The most common whitespace characters are spaces, tabs, and newlines.
# 
# Spaces are easy to create, because you have been using them as long as you have been using computers. Tabs and newlines are represented by special character combinations.
# 
# The two-character combination "\t" makes a tab appear in a string. Tabs can be used anywhere you like in a string.

# In[17]:


print("Hello everyone!")


# In[18]:


print("\tHello everyone!")


# In[19]:


print("Hello \teveryone!")


# The combination "\n" makes a newline appear in a string. You can use newlines anywhere you like in a string.

# In[21]:


print("Hello everyone!")


# In[22]:


print("\nHello everyone!")


# In[23]:


print("Hello \neveryone!")


# In[24]:


print("\n\n\nHello everyone!")


# We'll talk again about newlines when we talk about writing to files.

# ### Stripping whitespace
# 
# Sometimes you'll wnat to get rid of whitespace characters (spaces, tabs, and newlines) that precede or follow the string (for example, when reading from files or when accepting free-response from users). 
# 
# You can strip whitespace from the left side, the right side, or both sides of a string.

# In[10]:


name = ' eric '

print(name.lstrip())
print(name.rstrip())
print(name.strip())


# It's hard to see exactly what is happening, so maybe the following will make it a little more clear:

# In[11]:


name = ' eric '

print('-' + name.lstrip() + '-')
print('-' + name.rstrip() + '-')
print('-' + name.strip() + '-')


# [top](#)

# Numbers
# ===

# Integers
# ---
# You can do all of the basic operations with integers, and everything should behave as you expect. Addition and subtraction use the standard plus and minus symbols. Multiplication uses the asterisk, and division uses a forward slash. Exponents use two asterisks.

# In[ ]:


print 3+2


# In[ ]:


print 3-2


# In[ ]:


print 3**2


# In[5]:


print 3 % 2


# This last one (`%`) is a modulus operator. It returns the remainder after division: 3 mod 2 is 1 because when we divide 3 by 2, the remainder is 1. Remember this. It comes in handy!

# You can use parenthesis to modify the standard order of operations.

# In[4]:


standard_order = 2+3*4
print(standard_order)


# In[5]:


my_order = (2+3)*4
print(my_order)


# Floating-Point numbers
# ---
# Floating-point numbers refer to any number with a decimal point. Most of the time, you can think of floating point numbers as decimals, and they will behave as you expect them to.

# In[6]:


print(0.1+0.1)


# However, sometimes you will get an answer with an unexpectly long decimal part:

# In[7]:


print(0.1+0.2)


# This happens because of the way computers represent numbers internally; this has nothing to do with Python itself. Basically, we are used to working in powers of ten, where one tenth plus two tenths is just three tenths. But computers work in powers of two. So your computer has to represent 0.1 in a power of two, and then 0.2 as a power of two, and express their sum as a power of two. There is no exact representation for 0.3 in powers of two, and we see that in the answer to 0.1+0.2.
# 
# Python tries to hide this kind of stuff when possible. Don't worry about it much for now; just don't be surprised by it, and know that we will learn to clean up our results a little later on.
# 
# You can also get the same kind of result with other operations.

# In[8]:


print(3*0.1)


# Integers in Python 2.7
# ---
# There are a couple differences in the way Python 2 and Python 3 handle numbers. In Python 2, dividing two integers always results in an integer, while Python 3 always returns a float. This is fine when the result of your integer division is an integer, but it leads to quite different results when the answer is a decimal.

# ### Division in Python 2.7

# In[2]:


# Python 2.7
print 4/2


# In[5]:


# Python 2.7
print 3/2


# You can force Python 2 to use decimal-point (float) division by having one or both of the divisors be a float. Both of these methods work 

# In[6]:


print 3.0/2


# In[9]:


print float(3)/2


# ### Division in Python 3.3

# Python 3 does float division by default:

# In[11]:


# Python 3.3
print(4/2)


# In[12]:


# Python 3.3
print(3/2)


# If you are getting numerical results that you don't expect, or that don't make sense, check if the version of Python you are using is treating integers differently than you expect.

# # Combining data-types

# Python is a typed language meaning that every variable has a defined type. You can check its type like this:

# In[ ]:


type(4)


# In[ ]:


type(3.0)


# In[ ]:


type('asd')


# In[ ]:


type(False)


# If you want to combine types, you need to convert them appopriately. Sometimes the conversions happen behind the scenes:

# In[7]:


a=3
b='s'
print a,b


# Other times they don't':

# In[8]:


a=3
b='s'
print a+b


# Some of Python's operators are "overloaded" meaning that what they do depends on the type of the variables the operator is working with:

# In[10]:


a=3
b=5
print a*b


# In[12]:


a='q'
b=3
print a*b


# In[14]:


a='q'
b='m'
print a*b


# In[15]:


a='q'
b='m'
print a+b


# The '+' operator is overloaded: when given integers or floats, it does normal addition (that's what you would expect). Adding a string and an integer throws a `TypeError` because it doesn't make sense... how would you add a number to a string? *Multiplying* a string by an integer *does* have a sensible and unambiguous interpretation (to programmers anyway): just repeat the string that number of times (note that multiplying a string by a <float> will *not* work. Finally, multiplying two strings isn't defined (what's 's' times 'q'??). But *adding* two strings does have an unambiguous interpretation: concatenation! 

# Commenting your code
# ===
# As you begin to write more complicated code, you will have to spend more time thinking about how to code solutions to the problems you want to solve. Once you come up with an idea, you will spend a fair amount of time troubleshooting your code, and revising your overall approach.
# 
# Comments allow you to write in English, within your program. In Python, any line that starts with a pound (#) symbol is ignored by the Python interpreter.

# In[1]:


# This line is a comment.
print("This line is not a comment, it is code.")


# For multi-line comments (e.g., for explaining what a function does), you can use a triple single quote `'''` but this is generally reserved for documenting code rather than writing simple comments. The triple quote can be  useful for *temporarily* commenting out a chunk of your code during debugging.

#     '''
#     for i in range(10):
#         print "blah"
#     '''

# <div class="alert alert-block alert-info">
# In Sublime Text, you can highlight code you want to comment and press ⌘-/ to prefix it with the `#` character thereby commenting it out</div>
# 

# What makes a good comment?
# ---
# - It is short and to the point, but a complete thought. Most comments should be written in complete sentences.
# - It explains your thinking, so that when you return to the code later you will understand how you were approaching the problem.
# - It explains your thinking, so that others who work with your code will understand your overall approach to a problem.
# - It explains particularly difficult sections of code in detail.
# 
# When should you write comments?
# ---
# - When you have to think about code before writing it.
# - When you are likely to forget later exactly how you were approaching a problem.
# - When there is more than one way to solve a problem.
# - When others are unlikely to anticipate your way of thinking about a problem.
# 
# Writing good comments is one of the clear signs of a good programmer. If you have any real interest in taking programming seriously, start using comments now. You will see them throughout the examples in these notebooks.

# [top](#)

# Zen of Python
# ===
# The Python community is incredibly large and diverse. People are using Python in science, in medicine, in robotics, on the internet, and in any other field you can imagine. This diverse group of thinkers has developed a collective mindset about how programs should be written. If you want to understand Python and the community of Python programmers, it is a good idea to learn the ways Python programmers think.
# 
# A set of guiding principles that is written right into the language:

# In[2]:


import this


# There is a lot here. Let's just take a few lines, and see what they mean for you as a new programmer.
# 
#     Beautiful is better than ugly.
# 
# Python programmers recognize that good code can actually be beautiful. If you come up with a particularly elegant or efficient way to solve a problem, especially a difficult problem, other Python programmers will respect your work and may even call it beautiful. There is beauty in high-level technical work.
# 
#     Explicit is better than implicit.
# 
# It is better to be clear about what you are doing, than come up with some shorter way to do something that is difficult to understand.
# 
#     Simple is better than complex.
#     Complex is better than complicated.
# 
# Keep your code simple whenever possible, but recognize that we sometimes take on really difficult problems for which there are no easy solutions. In those cases, accept the complexity but avoid complication.
# 
#     Readability counts.
# 
# There are very few interesting and useful programs these days that are written and maintained entirely by one person. Write your code in a way that others can read it as easily as possible, and in a way that you will be able to read and understand it 6 months from now. This includes writing good comments in your code.
# 
#     There should be one-- and preferably only one --obvious way to do it.
# 
# There are many ways to solve most problems that come up in programming. However, most problems have a standard, well-established approach. Save complexity for when it is needed, and solve problems in the most straightforward way possible.
# 
#     Now is better than never.
# 
# No one ever writes perfect code. If you have an idea you want to implement it, write some code that works. Release it, let it be used by others, and then steadily improve it.

# [top](#)
