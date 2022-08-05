#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc" style="margin-top: 1em;"><ul class="toc-item"><li><span><a href="#Lists---the-basics" data-toc-modified-id="Lists---the-basics-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Lists - the basics</a></span></li><li><span><a href="#Introducing-Lists" data-toc-modified-id="Introducing-Lists-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Introducing Lists</a></span><ul class="toc-item"><li><span><a href="#Example" data-toc-modified-id="Example-2.1"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>Example</a></span></li><li><span><a href="#Naming-and-defining-a-list" data-toc-modified-id="Naming-and-defining-a-list-2.2"><span class="toc-item-num">2.2&nbsp;&nbsp;</span>Naming and defining a list</a></span></li><li><span><a href="#Accessing-one-item-in-a-list" data-toc-modified-id="Accessing-one-item-in-a-list-2.3"><span class="toc-item-num">2.3&nbsp;&nbsp;</span>Accessing one item in a list</a></span><ul class="toc-item"><li><span><a href="#Accessing-the-last-items-in-a-list" data-toc-modified-id="Accessing-the-last-items-in-a-list-2.3.1"><span class="toc-item-num">2.3.1&nbsp;&nbsp;</span>Accessing the last items in a list</a></span></li></ul></li></ul></li><li><span><a href="#Lists-and-Looping" data-toc-modified-id="Lists-and-Looping-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Lists and Looping</a></span><ul class="toc-item"><li><span><a href="#Accessing-all-elements-in-a-list" data-toc-modified-id="Accessing-all-elements-in-a-list-3.1"><span class="toc-item-num">3.1&nbsp;&nbsp;</span>Accessing all elements in a list</a></span><ul class="toc-item"><li><span><a href="#Doing-more-with-each-item" data-toc-modified-id="Doing-more-with-each-item-3.1.1"><span class="toc-item-num">3.1.1&nbsp;&nbsp;</span>Doing more with each item</a></span></li><li><span><a href="#Inside-and-outside-the-loop" data-toc-modified-id="Inside-and-outside-the-loop-3.1.2"><span class="toc-item-num">3.1.2&nbsp;&nbsp;</span>Inside and outside the loop</a></span></li></ul></li><li><span><a href="#Enumerating-a-list" data-toc-modified-id="Enumerating-a-list-3.2"><span class="toc-item-num">3.2&nbsp;&nbsp;</span>Enumerating a list</a></span><ul class="toc-item"><li><span><a href="#A-common-looping-error" data-toc-modified-id="A-common-looping-error-3.2.1"><span class="toc-item-num">3.2.1&nbsp;&nbsp;</span>A common looping error</a></span></li></ul></li></ul></li><li><span><a href="#Common-List-Operations" data-toc-modified-id="Common-List-Operations-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Common List Operations</a></span><ul class="toc-item"><li><span><a href="#Modifying-elements-in-a-list" data-toc-modified-id="Modifying-elements-in-a-list-4.1"><span class="toc-item-num">4.1&nbsp;&nbsp;</span>Modifying elements in a list</a></span></li><li><span><a href="#Finding-an-element-in-a-list" data-toc-modified-id="Finding-an-element-in-a-list-4.2"><span class="toc-item-num">4.2&nbsp;&nbsp;</span>Finding an element in a list</a></span></li><li><span><a href="#Testing-whether-an-item-is-in-a-list" data-toc-modified-id="Testing-whether-an-item-is-in-a-list-4.3"><span class="toc-item-num">4.3&nbsp;&nbsp;</span>Testing whether an item is in a list</a></span></li><li><span><a href="#Adding-items-to-a-list" data-toc-modified-id="Adding-items-to-a-list-4.4"><span class="toc-item-num">4.4&nbsp;&nbsp;</span>Adding items to a list</a></span><ul class="toc-item"><li><span><a href="#Appending-items-to-the-end-of-a-list" data-toc-modified-id="Appending-items-to-the-end-of-a-list-4.4.1"><span class="toc-item-num">4.4.1&nbsp;&nbsp;</span>Appending items to the end of a list</a></span></li><li><span><a href="#Inserting-items-into-a-list" data-toc-modified-id="Inserting-items-into-a-list-4.4.2"><span class="toc-item-num">4.4.2&nbsp;&nbsp;</span>Inserting items into a list</a></span></li></ul></li><li><span><a href="#Creating-an-empty-list" data-toc-modified-id="Creating-an-empty-list-4.5"><span class="toc-item-num">4.5&nbsp;&nbsp;</span>Creating an empty list</a></span></li><li><span><a href="#Sorting-a-List" data-toc-modified-id="Sorting-a-List-4.6"><span class="toc-item-num">4.6&nbsp;&nbsp;</span>Sorting a List</a></span><ul class="toc-item"><li><span><a href="#sorted()-vs.-sort()" data-toc-modified-id="sorted()-vs.-sort()-4.6.1"><span class="toc-item-num">4.6.1&nbsp;&nbsp;</span><em>sorted()</em> vs. <em>sort()</em></a></span></li><li><span><a href="#Reversing-a-list" data-toc-modified-id="Reversing-a-list-4.6.2"><span class="toc-item-num">4.6.2&nbsp;&nbsp;</span>Reversing a list</a></span></li><li><span><a href="#Sorting-a-numerical-list" data-toc-modified-id="Sorting-a-numerical-list-4.6.3"><span class="toc-item-num">4.6.3&nbsp;&nbsp;</span>Sorting a numerical list</a></span></li></ul></li><li><span><a href="#Finding-the-length-of-a-list" data-toc-modified-id="Finding-the-length-of-a-list-4.7"><span class="toc-item-num">4.7&nbsp;&nbsp;</span>Finding the length of a list</a></span></li></ul></li><li><span><a href="#Removing-Items-from-a-List" data-toc-modified-id="Removing-Items-from-a-List-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Removing Items from a List</a></span><ul class="toc-item"><li><span><a href="#Removing-items-by-position" data-toc-modified-id="Removing-items-by-position-5.1"><span class="toc-item-num">5.1&nbsp;&nbsp;</span>Removing items by position</a></span></li><li><span><a href="#Removing-items-by-value" data-toc-modified-id="Removing-items-by-value-5.2"><span class="toc-item-num">5.2&nbsp;&nbsp;</span>Removing items by value</a></span></li><li><span><a href="#Popping-items-from-a-list" data-toc-modified-id="Popping-items-from-a-list-5.3"><span class="toc-item-num">5.3&nbsp;&nbsp;</span>Popping items from a list</a></span></li></ul></li></ul></div>

# Lists - the basics
# ===
# In this notebook, you will learn about lists, a very important data structure, that allows you to store more than one value in a single variable. Lists (and arrays as they are also sometimes called) are one of the most powerful ideas in programming.

# Introducing Lists
# ===
# Example
# ---
# A list is a collection of items that is stored in a variable. The items should be related in some way, but there are no restrictions on what can be stored in a list. Here is a simple example of a list, and how we can quickly access each item in the list.
# 
# <div class="alert alert-block alert-info">
# Lists are called "arrays" in many languages. Python has a related data-structure called an array that is part of the `numpy` (numerical python) package. We will talk about differences between lists and arrays later on. 
# </div>
# 
# 

# Naming and defining a list
# ---
# Since lists are collection of objects, it is good practice to give them a plural name. If each item in your list is an image, call the list `images`. If each item is a trial, call it `trials`. This gives you a straightforward way to refer to the entire list ('images'), and to a single item in the list ('image').
# 
# In Python, lists are designated by square brackets. You can define an empty list like this:
# 

# In[8]:


images = []


# To define a list with some initial values, you include the values within the square brackets

# In[9]:


images = ['dog', 'cat', 'panda']


# Accessing one item in a list
# ---
# Items in a list are identified by their position in the list, starting with zero. This sometimes trips people up. 
# 
# To access the first element in a list, you give the name of the list, followed by a zero in parentheses.

# In[10]:


images = ['dog', 'cat', 'panda']

print images[0]


# The number in parentheses is called the **index** of the item. Because lists start at zero, the index of an item is always one less than its position in the list. So to get the second item in the list, we need to use an index of 1.

# In[11]:


images = ['dog', 'cat', 'panda']

print images[1]


# ### Accessing the last items in a list
# You can probably see that to get the last item in this list, we would use an index of 2. This works, but it would only work because our list has exactly three items. Because it is so common for us to need the *last* value of the list, Python provides a simple way of doing it without needing to know how long the list is. To get the last item of the list, we use -1.

# In[12]:


images = ['dog', 'cat', 'panda']
print images[-1]


# This syntax also works for the second to last item, the third to last, and so forth.

# In[13]:


images = ['dog', 'cat', 'panda']
print images[-2]


# If you attemp to use a negative number larger than the length of the list you will get an IndexError:

# In[15]:


images = ['dog', 'cat', 'panda']
print images[-4]


# <div class="alert alert-block alert-info">
# If you are used to the syntax of some other languages, you may be tempted to get the last element in a list using syntax like `images[len(images)]`. This syntax will give you the same output as `images[-1]` but is more verbose, less clear, and thus dispreferred.
# </div>

# [top](#)

# Lists and Looping
# ===

# Accessing all elements in a list
# ---
# This is one of the most important concepts related to lists. You can have a list with a million items in it, and in three lines of code you can write a sentence for each of those million items. If you want to understand lists, and become a competent programmer, make sure you take the time to understand this section.
# 
# We use a loop to access all the elements in a list. A loop is a block of code that repeats itself until it runs out of items to work with, or until a certain condition is met. In this case, our loop will run once for every item in our list. With a list that is three items long, our loop will run three times.
# 
# Let's take a look at how we access all the items in a list, and then try to understand how it works.

# In[ ]:


images = ['dog', 'cat', 'red tailed raccoon']

for image in images:
    print image


# <div class="alert alert-block alert-info">
# If you want to see all the values in a list, e.g., for purposes of debugging, you you can simply print a list like so:
# `print images` to see all the values of the list. 
# </div>
#  

# In[ ]:


print images


# We have already seen how to create a list, so we are really just trying to understand how the last two lines work. These last two lines make up a loop, and the language here can help us see what is happening:
# 
#     for image in images:
# 
# - The keyword "for" tells Python to get ready to use a loop.
# - The variable "image", with no "s" on it, is a temporary placeholder variable. This is the variable that Python will place each item in the list into, one at a time. 
# 
# <div class="alert alert-block alert-info">
# This variable can be given any name, e.g., cur_image, or image_to__show but using a convention like image/images makes your code more understandable.
# </div>
#  
# - The first time through the loop, the value of "image" will be 'dog'.
# - The second time through the loop, the value of "image" will be 'cat'.
# - The third time through, "name" will be 'red tailed raccoon'.
# - After this, there are no more items in the list, and the loop will end.
# 
# <div class="alert alert-block alert-info">
# Notice that the last element in the list has several words. Despite containing multiple words, it is a single string. List values need not be strings. They can be any data-type including other lists, files, and functions. See [https://swcarpentry.github.io/python-novice-inflammation/03-lists/](these examples) for slightly more involved usages of lists.</div>
# 
# The site <a href="http://pythontutor.com/visualize.html#code=dogs+%3D+%5B'border+collie',+'australian+cattle+dog',+'labrador+retriever'%5D%0A%0Afor+dog+in+dogs%3A%0A++++print(dog)&mode=display&cumulative=false&heapPrimitives=false&drawParentPointers=false&textReferences=false&showOnlyOutputs=false&py=3&curInstr=0">pythontutor.com</a> allows you to run Python code one line at a time. As you run the code, there is also a visualization on the screen that shows you how the variable "dog" holds different values as the loop progresses. There is also an arrow that moves around your code, showing you how some lines are run just once, while other lines are run multiple tiimes. If you would like to see this in action, click the Forward button and watch the visualization, and the output as it is printed to the screen. Tools like this are incredibly valuable for seeing what Python is doing with your code.
# 
# ### Doing more with each item
# 
# We can do whatever we want with the value of "dog" inside the loop. In this case, we just print the name of the dog.
# 
#     print dog 
# 
# We are not limited to just printing the word dog. We can do whatever we want with this value, and this action will be carried out for every item in the list. Let's say something about each dog in our list.

# In[ ]:


dogs = ['border collie', 'australian cattle dog', 'labrador retriever']

for dog in dogs:
    print('I like ' + dog + 's.')


# Visualize this on <a href="http://pythontutor.com/visualize.html#code=dogs+%3D+%5B'border+collie',+'australian+cattle+dog',+'labrador+retriever'%5D%0A%0Afor+dog+in+dogs%3A%0A++++print('I+like+'+%2B+dog+%2B+'s.')&mode=display&cumulative=false&heapPrimitives=false&drawParentPointers=false&textReferences=false&showOnlyOutputs=false&py=3&curInstr=0">pythontutor</a>.
# 
# ### Inside and outside the loop
# 
# Python uses indentation to decide what is inside the loop and what is outside the loop. Code that is inside the loop will be run for every item in the list. Code that is not indented, which comes after the loop, will be run once just like regular code.

# In[ ]:


dogs = ['border collie', 'australian cattle dog', 'labrador retriever']

for dog in dogs:
    print('I like ' + dog + 's.')
    print('No, I really really like ' + dog +'s!\n')
    
print("\nThat's just how I feel about dogs.")


# Notice that the last line only runs once, after the loop is completed. Also notice the use of newlines ("\n") to make the output easier to read. Run this code on <a href="http://pythontutor.com/visualize.html#code=dogs+%3D+%5B'border+collie',+'australian+cattle+dog',+'labrador+retriever'%5D%0A%0Afor+dog+in+dogs%3A%0A++++print('I+like+'+%2B+dog+%2B+'s.')%0A++++print('No,+I+really+really+like+'+%2B+dog+%2B's!%5Cn')%0A++++%0Aprint(%22%5CnThat's+just+how+I+feel+about+dogs.%22)&mode=display&cumulative=false&heapPrimitives=false&drawParentPointers=false&textReferences=false&showOnlyOutputs=false&py=3&curInstr=0">pythontutor</a>.

# [top](#)

# Enumerating a list
# ---
# When you are looping through a list, you may sometimes not only want to access the current list element, but also want to know the index of the current item. The preferred (*Pythonic*) way of doing this is to use the `enumerate()` function which conveniently tracks the index of each item for you, as you loop through the list.

# To enumerate a list, you need to add an *index* variable to hold the current index. So instead of
# 
#     for dog in dogs:
#     
# You have
# 
#     for index, dog in enumerate(dogs)
#     
# The value in the variable *index* is always an integer. If you want to print it in a string, you have to turn the integer into a string:
# 
#     str(index)
#     
# The index always starts at 0, so in this example the value of *place* should actually be the current index, plus one:

# In[ ]:


people = ['Desia', 'Pablo', 'Matt', 'Vincent', 'Tamara', 'Mengguo', 'Ian', 'Rui', 'Yuvraj', 'Steven', 'Katharine', 'Sasha', 'Nathan', 'Kristina', 'Olivia']

for i, person in enumerate(sorted(people)):
    print "Person number " + str(i) + " in the class is " + person


# ### A common looping error
# One common looping error occurs when instead of using the single variable *dog* inside the loop, we accidentally use the variable that holds the entire list:

# In[ ]:


dogs = ['border collie', 'australian cattle dog', 'labrador retriever']

for dog in dogs:
    print(dogs)


# In this example, instead of printing each dog in the list, we print the entire list every time we go through the loop. Python puts each individual item in the list into the variable *dog*, but we never use that variable. Sometimes you will just get an error if you try to do this:

# In[ ]:


dogs = ['border collie', 'australian cattle dog', 'labrador retriever']

for dog in dogs:
    print('I like ' + dogs + 's.')


# [top](#)

# Common List Operations
# ===

# Modifying elements in a list
# ---
# You can change the value of any element in a list if you know the position of that item.

# In[ ]:


dogs = ['border collie', 'australian cattle dog', 'labrador retriever']

dogs[0] = 'australian shepherd'
print(dogs)


# Finding an element in a list
# ---
# If you want to find out the position of an element in a list, you can use the index() function.

# In[ ]:


dogs = ['border collie', 'australian cattle dog', 'labrador retriever']

print(dogs.index('australian cattle dog'))


# This method returns a ValueError if the requested item is not in the list.

# In[ ]:


dogs = ['border collie', 'australian cattle dog', 'labrador retriever']

print(dogs.index('poodle'))


# Testing whether an item is in a list
# ---
# You can test whether an item is in a list using the "in" keyword. This will become more useful after learning how to use if-else statements.

# In[ ]:


dogs = ['border collie', 'australian cattle dog', 'labrador retriever']

print('australian cattle dog' in dogs)
print('poodle' in dogs)


# Adding items to a list
# ---
# ### Appending items to the end of a list
# We can add an item to a list using the append() method. This method adds the new item to the end of the list.

# In[ ]:


dogs = ['border collie', 'australian cattle dog', 'labrador retriever']
dogs.append('poodle')

for dog in dogs:
    print(dog.title() + "s are cool.")


# ### Inserting items into a list
# We can also insert items anywhere we want in a list, using the **insert()** function. We specify the position we want the item to have, and everything from that point on is shifted one position to the right. In other words, the index of every item after the new item is increased by one.

# In[ ]:


dogs = ['border collie', 'australian cattle dog', 'labrador retriever']
dogs.insert(1, 'poodle')

print(dogs)


# Note that you have to give the position of the new item first, and then the value of the new item. If you do it in the reverse order, you will get an error.

# Creating an empty list
# ---
# Now that we know how to add items to a list after it is created, we can use lists more dynamically. We are no longer stuck defining our entire list at once.
# 
# A common approach with lists is to define an empty list, and then let your program add items to the list as necessary. This approach works, for example, when starting to build an interactive web site. Your list of users might start out empty, and then as people register for the site it will grow. This is a simplified approach to how web sites actually work, but the idea is realistic.
# 
# Here is a brief example of how to start with an empty list, start to fill it up, and work with the items in the list. The only new thing here is the way we define an empty list, which is just an empty set of square brackets.

# In[ ]:


# Create an empty list to hold our users.
names = []

# Add some users.
names.append('Desia')
names.append('Pablo')
names.append('Matt')

# Greet everyone.
for name in names:
    print "Welcome, " + name + '!'


# If we don't change the order in our list, we can use the list to figure out who our oldest and newest users are.

# In[ ]:


# Create an empty list to hold our users.
names = []

# Add some users.
names.append('Desia')
names.append('Pablo')
names.append('Matt')

# Greet everyone.
for name in names:
    print "Welcome, " + name + '!'
    
# Recognize our first user, and welcome our newest user.
print("\nThank you for being our very first user, " + names[0].title() + '!')
print("And a warm welcome to our newest user, " + names[-1].title() + '!')


# Note that the code welcoming our newest user will always work, because we have used the index -1. If we had used the index 2 we would always get the third user, even as our list of users grows and grows.

# Sorting a List
# ---
# We can sort a list alphabetically, in either order.

# In[ ]:


students = ['bernice', 'aaron', 'cody']

# Put students in alphabetical order.
students.sort()

# Display the list in its current order.
print("Our students are currently in alphabetical order.")
for student in students:
    print(student.title())

#Put students in reverse alphabetical order.
students.sort(reverse=True)

# Display the list in its current order.
print("\nOur students are now in reverse alphabetical order.")
for student in students:
    print(student.title())


# ### *sorted()* vs. *sort()*
# Whenever you consider sorting a list, keep in mind that you can not recover the original order. If you want to display a list in sorted order, but preserve the original order, you can use the *sorted()* function. The *sorted()* function also accepts the optional *reverse=True* argument.

# In[ ]:


students = ['bernice', 'aaron', 'cody']

# Display students in alphabetical order, but keep the original order.
print("Here is the list in alphabetical order:")
for student in sorted(students):
    print(student.title())

# Display students in reverse alphabetical order, but keep the original order.
print("\nHere is the list in reverse alphabetical order:")
for student in sorted(students, reverse=True):
    print(student.title())

print("\nHere is the list in its original order:")
# Show that the list is still in its original order.
for student in students:
    print(student.title())


# ### Reversing a list
# We have seen three possible orders for a list:
# - The original order in which the list was created
# - Alphabetical order
# - Reverse alphabetical order
# 
# There is one more order we can use, and that is the reverse of the original order of the list. The *reverse()* function gives us this order.

# In[ ]:


students = ['bernice', 'aaron', 'cody']
students.reverse()

print(students)


# Note that reverse is permanent, although you could follow up with another call to *reverse()* and get back the original order of the list.

# ### Sorting a numerical list
# All of the sorting functions work for numerical lists as well.

# In[ ]:


numbers = [1, 3, 4, 2]

# sort() puts numbers in increasing order.
numbers.sort()
print(numbers)

# sort(reverse=True) puts numbers in decreasing order.
numbers.sort(reverse=True)
print(numbers)


# In[ ]:


numbers = [1, 3, 4, 2]

# sorted() preserves the original order of the list:
print(sorted(numbers))
print(numbers)


# In[ ]:


numbers = [1, 3, 4, 2]

# The reverse() function also works for numerical lists.
numbers.reverse()
print(numbers)


# Finding the length of a list
# ---
# You can find the length of a list using the *len()* function.

# In[ ]:


usernames = ['bernice', 'cody', 'aaron']
user_count = len(usernames)

print(user_count)


# There are many situations where you might want to know how many items in a list. If you have a list that stores your users, you can find the length of your list at any time, and know how many users you have.

# In[ ]:


# Create an empty list to hold our users.
usernames = []

# Add some users, and report on how many users we have.
usernames.append('bernice')
user_count = len(usernames)

print("We have " + str(user_count) + " user!")

usernames.append('cody')
usernames.append('aaron')
user_count = len(usernames)

print("We have " + str(user_count) + " users!")


# On a technical note, the *len()* function returns an integer, which can't be printed directly with strings. We use the *str()* function to turn the integer into a string so that it prints nicely:

# In[ ]:


usernames = ['bernice', 'cody', 'aaron']
user_count = len(usernames)

print("This will cause an error: " + user_count)


# In[ ]:


usernames = ['bernice', 'cody', 'aaron']
user_count = len(usernames)

print("This will work: " + str(user_count))


# [top](#)

# Removing Items from a List
# ===
# Hopefully you can see by now that lists are a dynamic structure. We can define an empty list and then fill it up as information comes into our program. To become really dynamic, we need some ways to remove items from a list when we no longer need them. You can remove items from a list through their position, or through their value.

# Removing items by position
# ---
# If you know the position of an item in a list, you can remove that item using the *del* command. To use this approach, give the command *del* and the name of your list, with the index of the item you want to move in square brackets:

# In[ ]:


dogs = ['border collie', 'australian cattle dog', 'labrador retriever']
# Remove the first dog from the list.
del dogs[0]

print(dogs)


# Removing items by value
# ---
# You can also remove an item from a list if you know its value. To do this, we use the *remove()* function. Give the name of the list, followed by the word remove with the value of the item you want to remove in parentheses. Python looks through your list, finds the first item with this value, and removes it.

# In[ ]:


dogs = ['border collie', 'australian cattle dog', 'labrador retriever']
# Remove australian cattle dog from the list.
dogs.remove('australian cattle dog')

print(dogs)


# Be careful to note, however, that *only* the first item with this value is removed. If you have multiple items with the same value, you will have some items with this value left in your list.

# In[ ]:


letters = ['a', 'b', 'c', 'a', 'b', 'c']
# Remove the letter a from the list.
letters.remove('a')

print(letters)


# Popping items from a list
# ---
# There is a cool concept in programming called "popping" items from a collection. Every programming language has some sort of data structure similar to Python's lists. All of these structures can be used as queues, and there are various ways of processing the items in a queue.
# 
# One simple approach is to start with an empty list, and then add items to that list. When you want to work with the items in the list, you always take the last item from the list, do something with it, and then remove that item. The *pop()* function makes this easy. It removes the last item from the list, and gives it to us so we can work with it. This is easier to show with an example:

# In[ ]:


dogs = ['border collie', 'australian cattle dog', 'labrador retriever']
last_dog = dogs.pop()

print(last_dog)
print(dogs)


# This is an example of a first-in, last-out approach. The first item in the list would be the last item processed if you kept using this approach. We will see a full implementation of this approach later on, when we learn about *while* loops.
# 
# You can actually pop any item you want from a list, by giving the index of the item you want to pop. So we could do a first-in, first-out approach by popping the first iem in the list:

# In[ ]:


dogs = ['border collie', 'australian cattle dog', 'labrador retriever']
first_dog = dogs.pop(0)

print(first_dog)
print(dogs)


# [top](#)
