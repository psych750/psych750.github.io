#!/usr/bin/env python
# coding: utf-8

# Dictionaries
# ===
# Lists allow us to store lists of values in a particular order and are always traversed in some order. **Dictionaries** (also known as hashes) allow us to store bits of information in *no* particular order. For example, you might store a subject id associated with their data, or response codes and their meaning in the context of your experiment.

# What are dictionaries?
# ===
# Dictionaries are a way to store information that is connected in some way. Dictionaries store information in *key-value* pairs (in analogy to a conventional dictionary where the key would be a word and the value its meaning). In a Python dictionary, `keys` are usually strings, integers, or floats. You cannot use a list or dictionary as a key. Values can be pretty much anything. So you can have a dictionary where keys are strings and values are strings, lists, other dictionaries, or even functions.
# 
# ```{note}
# **Python dictionaries do not store their information in any particular order, so never assume that you can access it in the order you put it in. Python does make available to you a data-structure called an [Ordered Dictionary](https://www.geeksforgeeks.org/ordereddict-in-python/), so if you want one, use it; don't reinvent the wheel. 
# ```

# General Syntax
# ---
# A general dictionary in Python looks something like this:

# ```Python
# dictionary_name = {key_1: value_1, key_2: value_2, key_3: value_3}
# ```

# Since the keys and values in dictionaries can be long, we often write just one key-value pair on a line. You might see key-value pairs in dictionaries specified like this (although most of the time you will be defining these dynamically in your program rather than hardcoding the assignments):

# In[ ]:


dictionary_name = {key_1: value_1,
                   key_2: value_2,
                   key_3: value_3,
                   }


# This is a bit easier to read, especially if the values are long.

# Example
# ---
# As our first example, let's use a dictionary that implements a glossary of a few Python terms.

# In[2]:


python_words = {'list': 'a collection of values that are not connected, but have an order.',
                'dictionary': 'a collection of key-value pairs.',
                'key': 'a named index in a dictionary',
                }


# We can get individual items out of the dictionary, by giving the dictionary's name, and the key in square brackets, much like accessing an element from a list:

# In[ ]:





# In[6]:


python_words = {'list': 'a collection of values that are not connected, but have an order.',
                'dictionary': 'a collection of key-value pairs.',
                'key': 'a named index in a dictionary',
                }

print(f"A list is {python_words['list']}")
print(f"A dictionary is {python_words['dictionary']}")


# This code looks pretty repetitive, and it is. As with lists, we can iterate through dictionaries, but since there are two kinds of information in dictionaries, the structure is a bit more complicated than it is for lists. Here is how to use a `for` loop with a dictionary:

# In[8]:


python_words = {'list': 'a collection of values that are not connected, but have an order.',
                'dictionary': 'a collection of key-value pairs.',
                'key': 'a named index in a dictionary',
                }

# Print out the items in the dictionary.
for word, meaning in python_words.items():
    print(f"A {word} is {meaning}")


# If we had 100 terms in our dictionary, we would still be able to print them out with just these two lines of code.
# 
# The only tricky part about using `for` loops with dictionaries is figuring out what to call those first two variables. The general syntax for this `for` loop is:

# ```Python
# for key, value in dictionary_name.items():
#     print(key) # The key is stored in whatever you called the first variable.
#     print(value) # The value associated with that key is stored in your second variable.
# ```

# Common operations with dictionaries
# ===
# There are a few common things you will want to do with dictionaries. These include *adding* new key-value pairs, *modifying* information in the dictionary, and (comparatively rarely), *removing* items from dictionaries.

# Adding new key-value pairs
# ---
# To add a new key-value pair, you give the dictionary name followed by the new key in square brackets, and set that equal to the new value. We will show this by starting with an empty dictionary, and re-creating the dictionary from the example above.

# In[9]:


# Create an empty dictionary.
python_words = {} #note that we define a new dictionary using curly braces, not square brackets.

# Fill the dictionary, pair by pair.
python_words = {'list': 'a collection of values that are not connected, but have an order.',
                'dictionary': 'a collection of key-value pairs.',
                'key': 'a named index in a dictionary',
                }

# Print out the items in the dictionary.
for word, meaning in python_words.items():
    print(f"Word is {word}")
    print(f"Meaning {meaning}")
    print("\n")


# Modifying values in a dictionary
# ---
# At some point you may want to modify one of the values in your dictionary. Modifying a value in a dictionary is pretty similar to modifying an element in a list. You give the name of the dictionary and then the key in square brackets, and set that equal to the new value.

# In[16]:


python_words = {'list': 'a collection of values that are not connected, but have an order.',
                'dictionary': 'a collection of key-value pairs.',
                'key': 'a named index in a dictionary',
                }

print(python_words['dictionary']) #the original definition
    
# Clarify one of the meanings.
python_words['dictionary'] = 'a collection of key-value pairs. Each key can be used to access its corresponding value.'

print(python_words['dictionary']) #the clarified definition


# Removing key-value pairs
# ---
# You may want to remove some key-value pairs from one of your dictionaries at some point. You can do this using the same `del` command you learned to use with lists. To remove a key-value pair, you give the `del` command, followed by the name of the dictionary, with the key that you want to delete. This removes the key and the value as a pair.

# In[29]:


python_words = {'list': 'a collection of values that are not connected, but have an order.',
                'dictionary': 'a collection of key-value pairs.',
                'key': 'a named index in a dictionary',
                }

# Show the current set of words and meanings.
print("\n\nThese are some Python words I know:")
for word, meaning in python_words.items():
    print(f"Word: {word}")
    print(f"Meaning: {meaning}")
    
# Remove the word 'list' and its meaning.
del python_words['list']

# Show the current set of words and meanings.
print("\n\nThese are the Python words I know:")
for word, meaning in python_words.items():
    print(f"Word: {word}")
    print(f"Meaning: {meaning}")


# If you were going to work with this code, you would want to put the code for displaying the dictionary into a function. Let's see what this looks like:

# In[30]:


def show_words_meanings(python_words):
    # This function takes in a dictionary of python words and meanings,
    #  and prints out each word with its meaning.
    print("These are the Python words I know:")
    for word, meaning in python_words.items():
        print(f"Word {word} {meaning} \n")
        

python_words = {'list': 'a collection of values that are not connected, but have an order.',
                'dictionary': 'a collection of key-value pairs.',
                'key': 'a named index in a dictionary',
                }

show_words_meanings(python_words)
    
# Remove the word 'list' and its meaning.
del python_words['list']

show_words_meanings(python_words)


# Modifying keys in a dictionary
# ---
# Modifying a value in a dictionary was straightforward, because nothing else depends on the value. Modifying a key is a little harder, because each key is used to unlock a value. We can change a key in two steps:
# 
# - Make a new key, and copy the value to the new key.
# - Delete the old key, which also deletes the old value.
# 
# Here's what this looks like. We will use a dictionary with just one key-value pair, to keep things simple.

# In[21]:


# We have a spelling mistake!
python_words = {'lisst': 'A collection of values that are not connected, but have an order.'}

# Create a new, correct key, and connect it to the old value.
#  Then delete the old key.
python_words['list'] = python_words['lisst']
del python_words['lisst']

# Print the dictionary, to show that the key has changed.
print(python_words)


# Looping through a dictionary
# ===
# Since dictionaries are really about connecting bits of information, you will often use them in the ways described above, where you add key-value pairs whenever you receive some new information, and then you retrieve the key-value pairs that you care about. Sometimes, however, you will want to loop through the entire dictionary. There are several ways to do this:
# 
# - You can loop through all key-value pairs;
# - You can loop through the keys, and pull out the values for any keys that you care about;
# - You can loop through the values.

# Looping through all key-value pairs
# ---
# This is the kind of loop that was shown in the first example. Here's what this loop looks like, in a general format:

# In[36]:


my_dict = {'key_1': 'value_1',
    'key_2': 'value_2',
    'key_3': 'value_3',
    }

for key, value in my_dict.items():
    print(f"Key: {key}")
    print(f"Value: {value}")


# This works because the method `.items()` pulls all key-value pairs from a dictionary into a list of tuples:

# In[37]:


my_dict = {'key_1': 'value_1',
    'key_2': 'value_2',
    'key_3': 'value_3',
    }

print(my_dict.items())


# The syntax `for key, value in my_dict.items():` does the work of looping through this list of tuples, and pulling the first and second item from each tuple for us.
# 
# There is nothing special about any of these variable names, so Python code that uses this syntax becomes really readable. Rather than create a new example of this loop, let's just look at the original example again to see this in a meaningful context:

# In[38]:


python_words = {'list': 'A collection of values that are not connected, but have an order.',
                'dictionary': 'A collection of key-value pairs.',
                'function': 'A named set of instructions that defines a set of actions in Python.',
                }

for word, meaning in python_words.items():
    print(f"Word: {word}")
    print(f"Meaning: {meaning} \n")


# Looping through all keys in a dictionary
# ---
# Python provides a clear syntax for looping through just the keys in a dictionary:

# In[39]:


my_dict = {'key_1': 'value_1',
    'key_2': 'value_2',
    'key_3': 'value_3',
    }

for key in my_dict.keys():
    print(f"Key: {key}")


# This is actually the default behavior of looping through the dictionary itself. So you can leave out the `.keys()` part, and get the exact same behavior:

# In[40]:


my_dict = {'key_1': 'value_1',
    'key_2': 'value_2',
    'key_3': 'value_3',
    }

for key in my_dict:
    print(f"Key: {key}")


# The only advantage of using the `.keys()` in the code is a little bit of clarity. But anyone who knows Python reasonably well is going to recognize what the second version does. In the rest of our code, we will leave out the `.keys()` when we want this behavior.
# 
# You can pull out the value of any key that you are interested in within your loop, using the standard notation for accessing a dictionary value from a key:

# In[51]:


my_dict = {'key_1': 'ham',
    'key_2': 'spam',
    'key_3': 'pam',
    }

for key in my_dict:
    print(f"Current key is: {key}") 
    if my_dict[key] == 'spam':
        print(f"  Got it! The value for {key} is {my_dict[key]}")


# Let's show how we might use this in our Python words program. This kind of loop provides a straightforward way to show only the words in the dictionary:

# In[49]:


python_words = {'list': 'A collection of values that are not connected, but have an order.',
                'dictionary': 'A collection of key-value pairs.',
                'function': 'A named set of instructions that defines a set of actions in Python.',
                }

# Show the words that are currently in the dictionary.
print("The following Python words have been defined:")
for word in python_words: # remember, the default behavios is to iterate through the keys.
    print(f" -  {word}")


# Looping through all values in a dictionary
# ---
# Python provides a straightforward syntax for looping through all the values in a dictionary, as well:

# In[52]:


my_dict = {'key_1': 'value_1',
    'key_2': 'value_2',
    'key_3': 'value_3',
    }

for value in my_dict.values():
    print(f"Current value is {value}")


# ```{note}
# All keys in a dictionary must be unique. If you try to create an entry in a dictionary with a key that already exists, you will just overwrite the previous key. Values need not be unique. What this means it that when you iterate through keys, you are assured that each element is unique. If you iterate over the values, as in the example above, there are no assurance about uniqueness. 
# ```

# Looping through a dictionary in order by keys
# ---
# Dictionaries are useful because they allow bits of information to be connected. When you print a dictionary, it may look like the keys are stored in a particular order. They are not and this order will vary from one run of the program to the next. Dictionaries are an *unordered* data-type. Sometimes you may want to sort the keys so that they do print (or are otherwise accessed) in a particular order. For alpha-numeric orders, there is a quick and easy way to do this.
# 

# In[30]:


python_words = {'list': 'a collection of values that are not connected, but have an order.',
                'dictionary': 'a collection of key-value pairs.',
                'key': 'a named index in a dictionary',
                }

for word in python_words.keys():
    print word 


# The resulting list is not in any particular order. The list of keys can be put in alpha-numeric order by passing the list into the *sorted()* function, in the line that initiates the for loop:

# In[29]:


python_words = {'list': 'a collection of values that are not connected, but have an order.',
                'dictionary': 'a collection of key-value pairs.',
                'key': 'a named index in a dictionary',
                }

for word in sorted(python_words.keys()):
    print word 


# In this example, the keys have been put into alphabetical order in the `for` loop only; Python has not changed the way the dictionary is stored at all. So the next time the dictionary is accessed, the keys could be returned in any order. There is no way to permanently specify an order for the items in an ordinary dictionary, but if you want to do this you can use the [OrderedDict](http://docs.python.org/3.3/library/collections.html#ordereddict-objects) structure.

# ```{tip}
# To sort in reverse order, give sorted() `reverse=True` as an argument 
# ```

# Looping through a dictionary in order by values
# ---
# Dictionaries are generally accessed by their keys. Sometimes, however, we need to do something like find the largest value or sort its values in a particular order. 
# 
# Finding the largest value is as simple as:

# In[53]:


my_dictionary = {'item1':3, 'item4':-4, 'item2':2, 'item3':8}
max(my_dictionary.values())


# Sorting by *values* has [various solutions](https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value). Here are two. One that uses only what you've already learned. Another is a more compact and preferred solution that uses the [`operator` Python module](https://docs.python.org/3/library/operator.html). The operator module allows you to use various operators as functions. 

# ### Sorting by values: the verbose and inefficient solution

# In[54]:


#this dictionary contains some words and the number of letters they have.
dict_for_sorting = {
 'Figure': 6,
 'Freestyle': 9,
 'Olympics': 8,
 'Pyeongchang,': 12,
 'Skating.': 8,
 'Skiing': 6,
 'Snowboarding': 12,
 'To': 2,
 'Winter': 6,
 'a': 1,
 'air.': 4,
 'and': 3,
 'body': 4,
 'corks': 5}

sorted_representation = []
temp = []
#iterate through dictionary and create a new list (of tuples) that reverses keys and values
for key,value in dict_for_sorting.items():
    sorted_representation.append((value,key))

#sort it
sorted_representation = sorted(sorted_representation)

#now get the key/value pairs to be as before: key-value instead of value-key
for key,value in sorted_representation:
    temp.append((value,key))
sorted_representation = temp
print(sorted_representation)


# ### Sorting by values: the compact and efficient solution

# In[18]:


import operator

dict_for_sorting = {
 'Figure': 6,
 'Freestyle': 9,
 'Olympics': 8,
 'Pyeongchang,': 12,
 'Skating.': 8,
 'Skiing': 6,
 'Snowboarding': 12,
 'To': 2,
 'Winter': 6,
 'a': 1,
 'air.': 4,
 'and': 3,
 'body': 4,
 'corks': 5}

print(f"Increasing order: {sorted(dict_for_sorting.items(), key=operator.itemgetter(1))}")
print('\n')
print(f"Decreasing order: {sorted(dict_for_sorting.items(), key=operator.itemgetter(1), reverse=True)}")


# ```{tip}
# Try setting key `operator.itemgetter(0)`. What does this do?
# ```

# Nesting data structures
# ===
# Nesting is one of the most powerful concepts we have come to so far. Nesting involves putting a list or dictionary inside another list or dictionary. We will look at two examples here, lists inside of a dictionary and dictionaries inside of a dictionary. With nesting, the kind of information we can model in our programs is expanded greatly.

# Lists in a dictionary
# ---
# A dictionary connects two pieces of information. Those two pieces of information can be any kind of data structure in Python. Let's keep using strings for our keys, but let's try giving a list as a value.
# 
# The first example will involve storing a number of people's favorite numbers. The keys consist of people's names, and the values are lists of each person's favorite numbers. In this first example, we will access each person's list one at a time.

# In[19]:


# This program stores people's favorite numbers, and displays them.
favorite_numbers = {'eric': [3, 11, 19, 23, 42],
                    'ever': [2, 4, 5],
                    'willie': [5, 35, 120],
                    }

# Display each person's favorite numbers.
print("Eric's favorite numbers are:")
print(favorite_numbers['eric'])

print("\nEver's favorite numbers are:")
print(favorite_numbers['ever'])

print("\nWillie's favorite numbers are:")
print(favorite_numbers['willie'])


# We are really just working our way through each key in the dictionary, so let's use a for loop to go through the keys in the dictionary:

# In[20]:


# This program stores people's favorite numbers, and displays them.
favorite_numbers = {'eric': [3, 11, 19, 23, 42],
                    'ever': [2, 4, 5],
                    'willie': [5, 35, 120],
                    }

# Display each person's favorite numbers.
for name in favorite_numbers:
    print(f"{name.title()}'s favorite numbers are:")
    print(favorite_numbers[name])


# This structure is fairly complex, so don't worry if it takes a while for things to sink in. The dictionary itself probably makes sense; each person is connected to a list of their favorite numbers.
# 
# This works, but we'd rather not print raw Python in our output. Let's use a for loop to print the favorite numbers individually, rather than in a Python list.

# In[22]:


# This program stores people's favorite numbers, and displays them.
favorite_numbers = {'eric': [3, 11, 19, 23, 42],
                    'ever': [2, 4, 5],
                    'willie': [5, 35, 120],
                    }

# Display each person's favorite numbers.
for name in favorite_numbers:
    print(f"{name.title()}'s favorite numbers are:")
    # Each value is itself a list, so we need another for loop to unroll each list
    for favorite_number in favorite_numbers[name]:
        print(favorite_number)


# Things get a little more complicated inside the `for` loop. The value is a list of favorite numbers, so the `for` loop pulls each *favorite\_number* out of the list one at a time. If it makes more sense to you, you are free to store the list in a new variable, and use that to define your `for` loop:
# 

# In[56]:


# This program stores people's favorite numbers, and displays them.
favorite_numbers = {'eric': [3, 11, 19, 23, 42],
                    'ever': [2, 4, 5],
                    'willie': [5, 35, 120],
                    }

# Display each person's favorite numbers.
for name in favorite_numbers:
    print(f"{name.title()}'s favorite numbers are:")
    for favorite_number in favorite_numbers[name]:
        print(favorite_number)


# Dictionaries in a dictionary
# ---
# The most powerful nesting concept we will cover right now is nesting a dictionary inside of a dictionary.
# 
# To demonstrate this, let's make a dictionary of pets, with some information about each pet. The keys for this dictionary will consist of the pet's name. The values will include information such as the kind of animal, the owner, and whether the pet has been vaccinated.

# In[64]:


# This program stores information about pets. For each pet,
#   we store the kind of animal, the owner's name, and
#   the breed.
pets = {'willie': {'kind': 'dog', 'owner': 'eric', 'vaccinated': True},
        'walter': {'kind': 'cockroach', 'owner': 'eric', 'vaccinated': False},
        'peso': {'kind': 'dog', 'owner': 'chloe', 'vaccinated': True},
        }

# Let's show all the information for each pet.
print("Here is what I know about Willie:")
print(f"kind: {pets['willie']['kind']}")
print(f"owner: {pets['willie']['kind']}")
print(f"vaccinated: {pets['willie']['vaccinated']}")
print('\n')

print("Here is what I know about Walter:")
print(f"kind: {pets['walter']['kind']}")
print(f"owner: {pets['walter']['kind']}")
print(f"vaccinated: {pets['walter']['vaccinated']}")
print('\n')

print("Here is what I know about Peso:")
print(f"kind: {pets['peso']['kind']}")
print(f"owner: {pets['peso']['kind']}")
print(f"vaccinated: {pets['peso']['vaccinated']}")
print('\n')


# Clearly this is *really* repetitive code, but it shows exactly how we access information in a nested dictionary. In the first set of `print` statements, we use the name 'willie' to unlock the 'kind' of animal he is, the 'owner' he has, and whether or not he is 'vaccinated'. We have to wrap the vaccination value in the `str` function so that Python knows we want the words 'True' and 'False', not the values `True` and `False`. We then do the same thing for each animal.
# 
# Let's rewrite this program, using a `for` loop to go through the dictionary's keys:

# In[67]:


# This program stores information about pets. For each pet,
#   we store the kind of animal, the owner's name, and
#   the breed.
pets = {'willie': {'kind': 'dog', 'owner': 'eric', 'vaccinated': True},
        'walter': {'kind': 'cockroach', 'owner': 'eric', 'vaccinated': False},
        'peso': {'kind': 'dog', 'owner': 'chloe', 'vaccinated': True},
        }

# Let's show all the information for each pet.
for pet_name, pet_information in pets.items():
    print(f"Here is what I know about {pet_name.title()}")
    print(f"kind: {pet_information['kind']}")
    print(f"owner: {pet_information['owner']}")
    print(f"vaccinated: {pet_information['vaccinated']}")
    print('\n')


# This code is much shorter and easier to maintain. But even this code will not keep up with our dictionary. If we add more kinds of information to the dictionary (i.e., additional keys), we will have to update our print statements. Let's put a second `for` loop inside the first loop in order to run through all the information about each pet:

# In[71]:


# This program stores information about pets. For each pet,
#   we store the kind of animal, the owner's name, and
#   the breed.
pets = {'willie': {'kind': 'dog', 'owner': 'eric', 'vaccinated': True},
        'walter': {'kind': 'cockroach', 'owner': 'eric', 'vaccinated': False},
        'peso': {'kind': 'dog', 'owner': 'chloe', 'vaccinated': True},
        }

# Let's show all the information for each pet.
for pet_name, pet_information in pets.items():
    print(f"\nHere is what I know about {pet_name.title()}")
    # Each animal's dictionary is in 'information'
    for key in pet_information:
        print(f"{key} : {pet_information[key]}")


# This nested loop can look pretty complicated, so again, don't worry if it doesn't make sense at first. Let's go through it one bit at a time.
# 
# - The first loop gives us all the keys in the main dictionary, which consist of the name of each pet.
# - Each of these names can be used to 'unlock' the dictionary of each pet.
# - The inner loop goes through the dictionary for that individual pet, and pulls out all of the keys in that individual pet's dictionary.
# - We print the key, which tells us the kind of information we are about to see, and the value for that key.
# - You can see that we could improve the formatting in the output.
#     - We could capitalize the owner's name.
#     - We could print some special message about the vaccination status
#     
# Let's show one last version that uses some if statements to clean up our data for printing:

# In[68]:


# This program stores information about pets. For each pet,
#   we store the kind of animal, the owner's name, and
#   the breed.
pets = {'willie': {'kind': 'dog', 'owner': 'eric', 'vaccinated': True},
        'walter': {'kind': 'cockroach', 'owner': 'eric', 'vaccinated': False},
        'peso': {'kind': 'dog', 'owner': 'chloe', 'vaccinated': True},
        }

# Let's show all the information for each pet.
for pet_name, pet_information in pets.items():
    print(f"\nHere is what I know about {pet_name.title()}")
    # Each animal's dictionary is in pet_information
    for key in pet_information:
        if key == 'owner':
            # Capitalize the owner's name.
            print(f"{key}: {pet_information[key].title()}")
        elif key == 'vaccinated':
            # Print 'yes' for True, and 'no' for False.
            if pet_information['vaccinated']:
                print("is vaccinated!")
            else:
                print("is not vaccinated!")
        else:
            # No special formatting needed for this key.
            print(f"{key}: {pet_information[key]}")


# This code is a lot longer, and now we have nested if statements as well as nested for loops. But keep in mind, this structure would work if there were 1000 pets in our dictionary, and it would work if we were storing 1000 pieces of information about each pet. One level of nesting lets us model an incredible variety of information.

# An important note about nesting
# ---
# While one level of nesting is really useful, nesting much deeper than that gets quickly complicated. There are other structures such as classes which can be even more useful for modeling information. In addition to this, we can use Python to store information in a database, which is the proper tool for storing deeply nested information.
# 
# Oftentimes when you are storing information in a database you will pull a small set of that information out and put it into a dictionary, or a slightly nested structure, and then work with it. But you will rarely, if ever, work with Python data structures nested more than one level deep.

# Using dictionaries in experiment design: some examples
# ===
# 
# What are some real-world examples of using dictionaries in your experiment?
# 
# Recall part 7-8 of [Exercise 2](http://sapir.psych.wisc.edu/programming_for_psychologists/notebooks/Exercise2-names.html). The information entered into the pop-up boxes is stored in... a dictionary! When you execute the statements 
# 
# ```Python
# userVar = {'Name':'Enter your name'}
# dlg = gui.DlgFromDict(userVar)
# ```
# 
# You are creating a dictionary named `userVar` and then setting the Name key in the dictionary with the value the user enters into the box. The userVar can have multiple keys, e.g.
# 
# ```Python
# userVar = {'Name':'Enter your name', 'Age':'Enter your age'}
# dlg = gui.DlgFromDict(userVar)
# ```
# 
# See [here](http://sapir.psych.wisc.edu/programming_for_psychologists/notebooks/Psychopy_reference.html#Easy-way-to-get-runtime-variables) for how to extend this general approach to a more real-world situation.
# 

# Here is another example in which we check whether the received response is equal to the correctResponse. Assume that correct_response is set to 'match' or 'mismatch'

# In[ ]:


response_mapping = {'z':'match', 'slash':'mismatch'}

if response_mapping[response_received] == correct_response:
    isRight=1
else:
    isRight=0


# Suppose we want to have a counterbalancing variable such that people assigned to the *matchLeft* condition response with 'z' as match and 'slash' as mismatch while people assigned to the *matchRight* condition have the response keys reversed. We could do if/else statements, but dictionaries provide a more elegant and more extendible solution:

# In[ ]:


response_mapping = {
                    'matchLeft': {'z':'match', 'slash':'mismatch'},
                    'matchRight': {'z':'mismatch', 'slash':'match'}}

whichMatch = 'matchLeft' #this would be ordinarily set at experiment runtime
response_received = event.waitKeys(keyList = response_mapping[whichMatch].keys())

if response_mapping[whichMatch][response_received] == correct_response:
    isRight=1
else:
    isRight=0Given the following dictionary, find the mean value of the keys that begin with a vowel.

```Python
a_dict = 
{'--': 2,
 'Air': 3,
 'At': 2,
 'Big': 3,
 'But': 3,
 'Figure': 6,
 'Freestyle': 9,
 'Olympics': 8,
 'Pyeongchang,': 12,
 'Skating.': 8,
 'Skiing': 6,
 'Snowboarding': 12,
 'To': 2,
 'Winter': 6,
 'a': 1,
 'air.': 4,
 'and': 3,
 'body': 4,
 'corks': 5,
 'do': 2,
 'four': 4,
 'got': 3,
 'have': 4,
 'in': 2,
 'jumps': 5,
 'less': 4,
 'limit': 5,
 'may': 3,
 'of': 2,
 'or': 2,
 'possible?': 9,
 'quad': 4,
 'quad,': 5,
 'reached': 7,
 'second': 6,
 'see': 3,
 "skater's": 8,
 'than': 4,
 'the': 3,
 'their': 5,
 'this': 4,
 'times': 5,
 'to': 2,
 'turn': 4,
 'twists': 6,
 'we': 2,
 "we'll": 5,
 "what's": 6,
 "year's": 6}
```

 Here's some code to help get you started:


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

# In[2]:


import numpy as np

def isVowel(letter):
    return letter in ['a','e','i','o','u']

def isVowelOnset(string):
    return isVowel(string[0])

#to find a mean of a list, use the mean() function from the numpy library
print np.mean(range(10))
#it is commonly imported as np so that you can type np.mean() instead of numpy.mean()


# <div class="alert alert-block alert-info">
# Note that by taking advantage of statements that already return True/False values, the code above avoids having to write constructions like: if X return True, else return Y.
# </div>

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

# In[4]:


letter_counts("Complete the implementation of the function. `letter_counts()` receives a string as input and returns a dictionary with (lowercase) letters and their respective counts. The keys are the letters and the counts are how many times a given letter occurred.")
```
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

