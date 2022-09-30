#!/usr/bin/env python
# coding: utf-8

# # A couple trial-generation activities
# 
# Before you type anything, think about how to go about solving these. Try to think of two ways. Which one is easier? Do the easy one!

# ## Exercise 1
# Write code to create a **qusi-random** sequence of these animals
# ```python
# animals = ['dog','cat','cow','pig','mouse']
# ```
# 
# Your code should accept a variable specifying how long the sequence should be (`min = len(animals)`, `max = 50`)
# 
# Now comes the tricky part. The sequence you generate should be randomized, but not have any animal repeating back to back.
# 
# So:
# ```python
# ['cat','dog','pig','cow','mouse','mouse','dog'] 
# ```
# is not ok because mouse repeated twice in a row, but
# ```python
# ['dog','cat','cow','pig','mouse','dog','mouse'] 
# ```
# is ok.
# 

# ## Exercise 2
# 
# Now let's try the opposite. Ensure that in your sequence, 20% of items (give or take a percent or so) is a back to back repeat. 
