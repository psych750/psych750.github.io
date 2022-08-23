#!/usr/bin/env python
# coding: utf-8

# # Exercise 3: Extending the Stroop effect
# 
# [Accept the exercise](https://classroom.github.com/a/ld0o1bOq). Please note that this exercise is more involved than Exercise 2 and will require more time. To this end, we'll make it a group exercise. Each of you has been paired with another student in the class. You can collaborate in person, through Slack, or by using [live code editing feature of VSC](https://code.visualstudio.com/learn/collaboration/live-share)
# 
# In this exercise we'll be extending the Stroop effect task you coded for Exercise 2 into a more complete experiment that (1) generates stimulus lists that are then read in by the main script, (3) accept runtime variables to assign participants to conditions and record participant codes, and (3) use some out-of-the-box speech recognition to allow participants to respond by using their voice.
# 
# We'll use the all same stimuli, but introduce several variations: 
# 
# a. We'll vary the proportion of trials that are incongruent (i.e., when the color of the font does not match the word).
# 
# b. We'll introduce an orientation manipulation so that on 50% of trials the word is presented upside down (what effect do you think this will have on response times?)
# 
# c. Lastly, we'll introduce a speech to-text feature so that participants can respond using their voice rather than by pressing a key. 
# 
# In this exercise we'll also substantially modularize the code so that one part of it is responsibl for generating the trials, another for reading in the trial list, another for showing the stimuli, and another for writing the participant's responses to a file.
# 

# ## Exercise 3 parts

# ## Part 1.
# Complete the `generate_trials()` function below so that it writes a file with all the trials to be presented to the participant.

# In[9]:


def generate_trials(subj_code, prop_incongruent, num_trials=100):
    '''
    Writes a file named {subj_code_}trials.csv, one line per trial. Creates a trials subdirectory if one does not exist
    subj_code: a string corresponding to a participant's unique subject code
    prop_incongruent: float [0-1] corresponding to the proportion of trials that are incongruent
    num_trials: integer specifying total number of trials (default 100)
    '''
    import os
    import random
    
    try:
        os.mkdir('trials')
    except FileExistsError:
        print('Trials directory exists; proceeding to open file')
    f= open(f"trials/{subj_code}_trials.csv","w")
    
    pass


# :::{tip}
# The text at the start of the function explaining what it does and its arguments is called a ["docstring"](https://classroom.github.com/classrooms/110263119-psych750-fa22). This is the proper way to document what a function does. Unlike comments, which are completely ignored by the Python interpreter, docstrings are part of the function and can be accessed like so: `print(generateTrials.__doc__)`. 
# :::
# 
# The produced file should be a CSV and have the following format:
# 
# Col 1: subject code
# 
# Col 2: trial number (1,2,3,etc.) from 1 for the first line to num_trials for the second
# 
# Col 3: proportion of incongruent trials
# 
# Col 4: the word to be shown
# 
# Col 5: the color of the word
# 
# Col 6: whether the trial is 'congruent' or 'incongruent'
# 
# Col 7: The orientation of the word, "upright", or "upside_down". Please ensure that 50% of the congruent trials are upright (and the remaining are upside-down). Same thing for incongruent trials -- 50% should be upright and the remainder upside-down. What this means is that if there are 100 total trials and 25% are incongruent, then 75/2 of the congruent trials (rounded to the nearest integer = 38) should be upright and 25/2 of the incongruent trials (rounded = 13 trials) should be upright.
# 
# 

# ## Part 2
# 
# Extend the script you wrote for Exercise 2 (or use the provided solution if you like) to accept these 2 runtime variables [using a GUI box](https://psych750.github.io/notebooks/Psychopy_reference.html#a-simple-function-for-popping-up-an-error-using-a-gui-window):
# 
# - subject code (any string, but conventionally somthing like stroop_101, stroop_102, etc.)
# - proportion of incongruent trials (drop down box of 25%, 50%, and 75%)
# 
# The entered values should be stored in a dictionary called `runTimeVars`. After the values are collected, the dictionary might look like this:
# 
# ```python
# runTimeVars = {'subj_code':'stroop_101', 'prop_incongruent':25}
# ```
# 
# ```{note}
# This dictionary must be populated dynamically. You should not be hard-coding any of these values
# ``` 
# 

# ## Part 3
# 
# Define a `write_data()` function in your code that is called after every response and writes all the trial information **and** responses to a file. 
# 
#  As in Exercise 2, you should be writing to the file after every trial. Make sure your data is written to `data/subject-code_data.csv` where `subject-code` is the subject code entered at runtime and `data/` is a subdirectory that will contain all the data files. Your code should record one line per response and record responses as they come in. If a user quits after trial 50, the data file should have recorded those 50 responses.  Here's an example of what your output file should look like (note that the first line contains column names.
# 
# | subj_code  | trial_num | prop_incongruent | word   | color | congruence  | orientation | resp | is_correct | RT  |
# |------------|-----------|------------------|--------|-------|-------------|-------------|------|------------|-----|
# | stroop_101 | 1         | .5               | green  | blue  | incongruent | upright     | b    | 1          | 898 |
# | stroop_101 | 2         | .5               | green  | green | congruent   | upright     | g    | 1          | 754 |
# | stroop_101 | 3         | .5               | yellow | red   | incongruent | upside_down | y    | 0          | 902 |
# 
# ```{note}
# Use a CSV format as before: fields are separated by commas
# ```  
# 
# ```{admonition} Challenge!
# Ensure that you can't run the same participant code twice. If you enter a participant code that's already been entered before, PsychoPy should pop-up a warning box saying "Participant code already exists". This should prevent you from overwriting an existing data-file. If you take up this challenge, tag it as e3_4_challenge
# ```

# ## Part 4
# 
# Microphone response
# ....stay tuned for starter code.....
