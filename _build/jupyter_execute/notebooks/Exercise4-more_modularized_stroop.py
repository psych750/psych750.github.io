#!/usr/bin/env python
# coding: utf-8

# # Exercise 4: Modularizing and Error Checking 
# 
# [Accept the exercise](https://classroom.github.com/a/dUrj9P3_).
# 
# As promised, we will be slowing down and so rather than having a brand new exercise, we'll stick with the previous one and work on further improvements which should be mirroring the improvements in your mental model of how the various pieces are fitting together. 
# 
# For this exercise, you may either join a team (limited to 2 people) or work individually. If you want to join a team and there isn't an existing one to join, please create a new one with `your_name_team`. If you'd like to work alone, create a team just called `your_name`.
# 
# The purpose of this exercise is to get you more comfortable with the solution I posted for Exercise 3 and to further modularize it (Parts 1-5) and error-proof it (Part 5).  
# 
# 

# ## Exercise 4 parts

# ## Part 1.
# Collect the stimulus presentation & response collection code -- setting colors, orientations, doing win.flips, collecting responses -- and place it into a `show_trial()` function. You'll need to decide what arguments this function should take (the fewer the better! Keep it as extendable as possible!) and what it should return. If done correctly, you should not have any setText, setOri, setColor, core.wait, or win.flip commands outside of this function.

# ## Part 2
# 
# From exercise_3 solution (mirrored in Exercise 4 starter code):
# ```python
#     #can we avoid this if statement by using a dictionary?
#     if cur_orientation=='upside_down':
#         word_stim.setOri(180)
#     else:
#         word_stim.setOri(0)
# 
# ```
# Avoid it by using a dictionary!

# ## Part 3
# 
# Recall this part:
# ```python
#     subj_code = cur_trial[0]
#     prop_incongruent = cur_trial[1]
#     cur_word = cur_trial[2]
#     cur_color = cur_trial[3]
#     cur_trial_type = cur_trial[4]
#     cur_orientation = cur_trial[5]
# ```
# Not only is this a lot of repetitive code, but it requires us to know which column is which. Improve this code by adding column names to the trial list so that you know which column is which. When you read the trials back in, use Pandas as demonstrated in class to access the trial data from the pandas data-frame
# 
# 

# ## Part 4
# 
# Add `response_type` to the pop-up (GUI) box. The value of this variable can be either "voice" or "key". If it's key, proceed with the experiment as before. If it's voice, have it use the speech-recognition voice capability. `is_correct` should be 1 if the said word matched the text color (i.e., person said "green" and it was actually green), 0 if not, and 'NA' if there was some processing error. RT should reflect the measured speech onset or NA if it couldn't be measured. The results file should also include the response, as recognized. If a person said "green", it should record "green".  
# 
# Make sure the value of `response_type` is included in the data file (so that someone looking at it later would know how the responses were collected).
# 

# ## Part 5
# Exercise 3 allowed us to reuse a subject code which would result in overwriting the existing data file if it existed. Implement error checking to prevent the user from reusing a subject code. If they attempt to use it, pop up an error saying "Subject code already exists" and give them an opportunity to enter another subject code until they enter one that does not have an associated data file. The results files should be stored in a `data` subdirectory just as the trial lists are stored in a `trials` subdirectory.
# 
# ```{tip}
# Use [os.path.exists](https://docs.python.org/3/library/os.path.html#os.path.exists)!
# ```
