#!/usr/bin/env python
# coding: utf-8

# While Loops and Input
# ===
# While loops are really useful because they let your program run until a user decides to quit the program. They set up an infinite loop that runs until the user does something to end the loop. This section also introduces the first way to get input from your program's users.

# [Previous: If Statements](http://nbviewer.ipython.org/urls/raw.github.com/ehmatthes/intro_programming/master/notebooks/if_statements.ipynb) | 
# [Home](http://nbviewer.ipython.org/urls/raw.github.com/ehmatthes/intro_programming/master/notebooks/index.ipynb) |
# [Next: Basic Terminal Apps](http://nbviewer.ipython.org/urls/raw.github.com/ehmatthes/intro_programming/master/notebooks/terminal_apps.ipynb)

# Contents
# ===
# - [What is a `while` loop?](#What-is-a-while-loop?)
#     - [General syntax](#General-syntax)
#     - [Example](#Example)
#     - [Exercises](#Exercises-while)
# - [Accepting user input](#Accepting-user-input)
#     - [General syntax](#General-syntax-input)
#     - [Example](#Example-input)
#     - [Accepting input in Python 2.7](#Accepting-input-in-Python-2.7)
#     - [Exercises](#Exercises-input)
# - [Using while loops to keep your programs running](#Using-while-loops-to-keep-your-programs-running)
#     - [Exercises](#Exercises-running)
# - [Using while loops to make menus](#Using-while-loops-to-make-menus)
# - [Using while loops to process items in a list](#Using-while-loops-to-process-items-in-a-list)
# - [Accidental Infinite loops](#Accidental-Infinite-loops)
#     - [Exercises](#Exercises-infinite)
# - [Overall Challenges](#Overall-Challenges)

# What is a while loop?
# ===
# A while loop tests an initial condition. If that condition is true, the loop starts executing. Every time the loop finishes, the condition is reevaluated. As long as the condition remains true, the loop keeps executing. As soon as the condition becomes false, the loop stops executing.

# General syntax
# ---

# In[ ]:


# Set an initial condition.
game_active = True

# Set up the while loop.
while game_active:
    # Run the game.
    # At some point, the game ends and game_active will be set to False.
    #   When that happens, the loop will stop executing.
    
# Do anything else you want done after the loop runs.


# - Every while loop needs an initial condition that starts out true.
# - The `while` statement includes a condition to test.
# - All of the code in the loop will run as long as the condition remains true.
# - As soon as something in the loop changes the condition such that the test no longer passes, the loop stops executing.
# - Any code that is defined after the loop will run at this point.

# Example
# ---
# Here is a simple example, showing how a game will stay active as long as the player has enough power.

# In[3]:


# The player's power starts out at 5.
power = 5

# The player is allowed to keep playing as long as their power is over 0.
while power > 0:
    print("You are still playing, because your power is %d." % power)
    # Your game code would go here, which includes challenges that make it
    #   possible to lose power.
    # We can represent that by just taking away from the power.
    power = power - 1
    
print("\nOh no, your power dropped to 0! Game Over.")


# [top](#)

# <a id="Exercises-while"></a>
# Exercises
# ---
# #### Growing Strength
# - Make a variable called strength, and set its initial value to 5.
# - Print a message reporting the player's strength.
# - Set up a while loop that runs until the player's strength increases to a value such as 10.
# - Inside the while loop, print a message that reports the player's current strength.
# - Inside the while loop, write a statement that increases the player's strength.
# - Outside the while loop, print a message reporting that the player has grown too strong, and that they have moved up to a new level of the game.
# - Bonus: Play around with different cutoff levels for the value of *strength*, and play around with different ways to increase the strength value within the while loop.

# [top](#)

# Accepting user input
# ===
# Almost all interesting programs accept input from the user at some point. You can start accepting user input in your programs by using the `input()` function. The input function displays a messaget to the user describing the kind of input you are looking for, and then it waits for the user to enter a value. When the user presses Enter, the value is passed to your variable.

# <a id="General-syntax-input"></a>
# General syntax
# ---
# The general case for accepting input looks something like this:

# In[ ]:


# Get some input from the user.
variable = input('Please enter a value: ')
# Do something with the value that was entered.


# You need a variable that will hold whatever value the user enters, and you need a message that will be displayed to the user.

# <a id="Example-input"></a>
# Example
# ---
# In the following example, we have a list of names. We ask the user for a name, and we add it to our list of names.

# In[7]:


# Start with a list containing several names.
names = ['guido', 'tim', 'jesse']

# Ask the user for a name.
new_name = input("Please tell me someone I should know: ")

# Add the new name to our list.
names.append(new_name)

# Show that the name has been added to the list.
print(names)


# Accepting input in Python 2.7
# ---
# In Python 3, you always use `input()`. In Python 2.7, you need to use `raw_input()`:

# In[8]:


# The same program, in Python 2.7

# Start with a list containing several names.
names = ['guido', 'tim', 'jesse']

# Ask the user for a name.
new_name = raw_input("Please tell me someone I should know: ")

# Add the new name to our list.
names.append(new_name)

# Show that the name has been added to the list.
print(names)


# The function `input()` will work in Python 2.7, but it's not good practice to use it. When you use the `input()` function in Python 2.7, Python runs the code that's entered. This is fine in controlled situations, but it's not a very safe practice overall.
# 
# If you're using Python 3, you have to use `input()`. If you're using Python 2.7, use `raw_input()`.

# <a id="Exercises-input"></a>
# Exercises
# ---
# #### Game Preferences
# - Make a list that includes 3 or 4 games that you like to play.
# - Print a statement that tells the user what games you like.
# - Ask the user to tell you a game they like, and store the game in a variable such as `new_game`.
# - Add the user's game to your list.
# - Print a new statement that lists all of the games that we like to play (*we* means you and your user).

# [top](#)

# Using while loops to keep your programs running
# ===
# Most of the programs we use every day run until we tell them to quit, and in the background this is often done with a while loop. Here is an example of how to let the user enter an arbitrary number of names.

# In[9]:


# Start with an empty list. You can 'seed' the list with
#  some predefined values if you like.
names = []

# Set new_name to something other than 'quit'.
new_name = ''

# Start a loop that will run until the user enters 'quit'.
while new_name != 'quit':
    # Ask the user for a name.
    new_name = input("Please tell me someone I should know, or enter 'quit': ")

    # Add the new name to our list.
    names.append(new_name)

# Show that the name has been added to the list.
print(names)


# That worked, except we ended up with the name 'quit' in our list. We can use a simple `if` test to eliminate this bug:

# In[10]:


###highlight=[15,16]
# Start with an empty list. You can 'seed' the list with
#  some predefined values if you like.
names = []

# Set new_name to something other than 'quit'.
new_name = ''

# Start a loop that will run until the user enters 'quit'.
while new_name != 'quit':
    # Ask the user for a name.
    new_name = input("Please tell me someone I should know, or enter 'quit': ")

    # Add the new name to our list.
    if new_name != 'quit':
        names.append(new_name)

# Show that the name has been added to the list.
print(names)


# This is pretty cool! We now have a way to accept input from users while our programs run, and we have a way to let our programs  run until our users are finished working.

# <a id="Exercises-running"></a>
# Exercises
# ---
# #### Many Games
# - Modify *[Game Preferences](#exercises_input)* so your user can add as many games as they like.

# [top](#)

# Using while loops to make menus
# ===
# You now have enough Python under your belt to offer users a set of choices, and then respond to those choices until they choose to quit. Let's look at a simple example, and then analyze the code:

# In[33]:


# Give the user some context.
print("\nWelcome to the nature center. What would you like to do?")

# Set an initial value for choice other than the value for 'quit'.
choice = ''

# Start a loop that runs until the user enters the value for 'quit'.
while choice != 'q':
    # Give all the choices in a series of print statements.
    print("\n[1] Enter 1 to take a bicycle ride.")
    print("[2] Enter 2 to go for a run.")
    print("[3] Enter 3 to climb a mountain.")
    print("[q] Enter q to quit.")
    
    # Ask for the user's choice.
    choice = input("\nWhat would you like to do? ")
    
    # Respond to the user's choice.
    if choice == '1':
        print("\nHere's a bicycle. Have fun!\n")
    elif choice == '2':
        print("\nHere are some running shoes. Run fast!\n")
    elif choice == '3':
        print("\nHere's a map. Can you leave a trip plan for us?\n")
    elif choice == 'q':
        print("\nThanks for playing. See you later.\n")
    else:
        print("\nI don't understand that choice, please try again.\n")
        
# Print a message that we are all finished.
print("Thanks again, bye now.")


# Our programs are getting rich enough now, that we could do many different things with them. Let's clean this up in one really useful way. There are three main choices here, so let's define a function for each of those items. This way, our menu code remains really simple even as we add more complicated code to the actions of riding a bicycle, going for a run, or climbing a mountain.

# In[34]:


###highlight=[2,3,4,5,6,7,8,9,10,30,31,32,33,34,35]
# Define the actions for each choice we want to offer.
def ride_bicycle():
    print("\nHere's a bicycle. Have fun!\n")
    
def go_running():
    print("\nHere are some running shoes. Run fast!\n")
    
def climb_mountain():
    print("\nHere's a map. Can you leave a trip plan for us?\n")

# Give the user some context.
print("\nWelcome to the nature center. What would you like to do?")

# Set an initial value for choice other than the value for 'quit'.
choice = ''

# Start a loop that runs until the user enters the value for 'quit'.
while choice != 'q':
    # Give all the choices in a series of print statements.
    print("\n[1] Enter 1 to take a bicycle ride.")
    print("[2] Enter 2 to go for a run.")
    print("[3] Enter 3 to climb a mountain.")
    print("[q] Enter q to quit.")
    
    # Ask for the user's choice.
    choice = input("\nWhat would you like to do? ")
    
    # Respond to the user's choice.
    if choice == '1':
        ride_bicycle()
    elif choice == '2':
        go_running()
    elif choice == '3':
        climb_mountain()
    elif choice == 'q':
        print("\nThanks for playing. See you later.\n")
    else:
        print("\nI don't understand that choice, please try again.\n")
        
# Print a message that we are all finished.
print("Thanks again, bye now.")


# This is much cleaner code, and it gives us space to separate the details of taking an action from the act of choosing that action.

# [top](#)

# Using while loops to process items in a list
# ===
# In the section on Lists, you saw that we can `pop()` items from a list. You can use a while list to pop items one at a time from one list, and work with them in whatever way you need. Let's look at an example where we process a list of unconfirmed users.

# In[21]:


# Start with a list of unconfirmed users, and an empty list of confirmed users.
unconfirmed_users = ['ada', 'billy', 'clarence', 'daria']
confirmed_users = []

# Work through the list, and confirm each user.
while len(unconfirmed_users) > 0:
    
    # Get the latest unconfirmed user, and process them.
    current_user = unconfirmed_users.pop()
    print("Confirming user %s...confirmed!" % current_user.title())
    
    # Move the current user to the list of confirmed users.
    confirmed_users.append(current_user)
    
# Prove that we have finished confirming all users.
print("\nUnconfirmed users:")
for user in unconfirmed_users:
    print('- ' + user.title())
    
print("\nConfirmed users:")
for user in confirmed_users:
    print('- ' + user.title())


# This works, but let's make one small improvement. The current program always works with the most recently added user. If users are joining faster than we can confirm them, we will leave some users behind. If we want to work on a 'first come, first served' model, or a 'first in first out' model, we can pop the first item in the list each time.

# In[22]:


###highlight=[10]
# Start with a list of unconfirmed users, and an empty list of confirmed users.
unconfirmed_users = ['ada', 'billy', 'clarence', 'daria']
confirmed_users = []

# Work through the list, and confirm each user.
while len(unconfirmed_users) > 0:
    
    # Get the latest unconfirmed user, and process them.
    current_user = unconfirmed_users.pop(0)
    print("Confirming user %s...confirmed!" % current_user.title())
    
    # Move the current user to the list of confirmed users.
    confirmed_users.append(current_user)
    
# Prove that we have finished confirming all users.
print("\nUnconfirmed users:")
for user in unconfirmed_users:
    print('- ' + user.title())
    
print("\nConfirmed users:")
for user in confirmed_users:
    print('- ' + user.title())


# This is a little nicer, because we are sure to get to everyone, even when our program is running under a heavy load. We also preserve the order of people as they join our project. Notice that this all came about by adding *one character* to our program!

# [top](#)

# Accidental Infinite loops
# ===
# Sometimes we want a while loop to run until a defined action is completed, such as emptying out a list. Sometimes we want a loop to run for an unknown period of time, for example when we are allowing users to give as much input as they want. What we rarely want, however, is a true 'runaway' infinite loop.
# 
# Take a look at the following example. Can you pick out why this loop will never stop?

# In[ ]:


current_number = 1

# Count up to 5, printing the number each time.
while current_number <= 5:
    print(current_number)


# In[ ]:


1
1
1
1
1
...


# I faked that output, because if I ran it the output would fill up the browser. You can try to run it on your computer, as long as you know how to interrupt runaway processes:
# 
# - On most systems, Ctrl-C will interrupt the currently running program.
# - If you are using Geany, your output is displayed in a popup terminal window. You can either press Ctrl-C, or you can use your pointer to close the terminal window.
# 
# The loop runs forever, because there is no way for the test condition to ever fail. The programmer probably meant to add a line that increments current_number by 1 each time through the loop:

# In[23]:


###highlight=[7]
current_number = 1

# Count up to 5, printing the number each time.
while current_number <= 5:
    print(current_number)
    current_number = current_number + 1


# You will certainly make some loops run infintely at some point. When you do, just interrupt the loop and figure out the logical error you made.
# 
# Infinite loops will not be a real problem until you have users who run your programs on their machines. You won't want infinite loops then, because your users would have to shut down your program, and they would consider it buggy and unreliable. Learn to spot infinite loops, and make sure they don't pop up in your polished programs later on.
# 
# Here is one more example of an accidental infinite loop:

# In[ ]:


current_number = 1

# Count up to 5, printing the number each time.
while current_number <= 5:
    print(current_number)
    current_number = current_number - 1


# In[ ]:


1
0
-1
-2
-3
...


# In this example, we accidentally started counting down. The value of `current_number` will always be less than 5, so the loop will run forever.

# <a name="Exercises-infinite"></a>
# Exercises
# ---
# #### Marveling at Infinity
# - Use one of the examples of a failed while loop to create an infinite loop.
# - Interrupt your output.
# - Marvel at the fact that if you had not interrupted your output, your computer would have kept doing what you told it to until it ran out of power, or memory, or until the universe went cold around it.

# [top](#)

# Overall Challenges
# ===
# #### Gaussian Addition
# This challenge is inspired by a story about the mathematician Carl Frederich Gauss. [As the story goes](http://mathforum.org/library/drmath/view/57919.html), when young Gauss was in grade school his teacher got mad at his class one day.
# 
# "I'll keep the lot of you busy for a while", the teacher said sternly to the group. "You are to add the numbers from 1 to 100, and you are not to say a word until you are done."
# 
# The teacher expected a good period of quiet time, but a moment later our mathematician-to-be raised his hand with the answer. "It's 5050!" Gauss had realized that if you list all the numbers from 1 to 100, you can always match the first and last numbers in the list and get a common answer:
# 
#     1, 2, 3, ..., 98, 99, 100
#     1 + 100 = 101
#     2 + 99 = 101
#     3 + 98 = 101
# 
# Gauss realized there were exactly 50 pairs of numbers in the range 1 to 100, so he did a quick calculation: 50 * 101 = 5050.
# 
# - Write a program that passes a list of numbers to a function.
#     - The function should use a while loop to keep popping the first and last numbers from the list and calculate the sum of those two numbers.
#     - The function should print out the current numbers that are being added, and print their partial sum.
#     - The function should keep track of how many partial sums there are.
#     - The function should then print out how many partial sums there were.
#     - The function should perform Gauss' multiplication, and report the final answer.
# - Prove that your function works, by passing in the range 1-100, and verifying that you get 5050.
#     - `gauss_addition(list(range(1,101)))`
# - Your function should work for any set of consecutive numbers, as long as that set has an even length.
#     - Bonus: Modify your function so that it works for any set of consecutive numbers, whether that set has an even or odd length.

# [top](#)

# - - -
# [Previous: If Statements](http://nbviewer.ipython.org/urls/raw.github.com/ehmatthes/intro_programming/master/notebooks/if_statements.ipynb) | 
# [Home](http://nbviewer.ipython.org/urls/raw.github.com/ehmatthes/intro_programming/master/notebooks/index.ipynb) |
# [Next: Basic Terminal Apps](http://nbviewer.ipython.org/urls/raw.github.com/ehmatthes/intro_programming/master/notebooks/terminal_apps.ipynb)
