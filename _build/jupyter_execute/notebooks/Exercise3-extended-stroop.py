#!/usr/bin/env python
# coding: utf-8

# # Exercise 3: Extending the stroop effect - NOT DONE YET
# 
# [Accept the exercise](XXXX)
# 
# In this exercise we'll be extending the Stroop effect you coded for Exercise 2 into a more complete experiment that (1) uses external files for stimulus generation rather than building them in, (2) accept runtime variables such as a subject code and what condition they're in, and (3) use some out-of-the-box speech recognition to allow participants to respond with their voices (as the original Stroop task did).

# In[ ]:


## Generating a simple trial list. 

-- to be revised -- 

Suppose we are interested in finding out the efficacy of a particular kind of masking technique and want to examine if it's more effective in the left vs. right visual field. Let's code a basic trial list for an experiment in which we display an image on either the left or the right side of the screen. Both sides of the screen are then masked, and we are interested in measuring people's ability (e.g., accuracy, reaction time) in responding whether the image was on the right or left side of the screen, while comparing responses on masked vs. nonmasked trials. 

To do this, we need to generate a list of trials in which some proportion is masked and some is not masked. Within each condition, we want the image on the left side displayed with some proportion of the time, and on the right the remaining times. 

Let's begin by having 2/3 masked trials and 1/3 non-masked trials. Within each level of the masking factor, half of the targets should be on the left and half on the right. Let's have 5 blocks with each block having all the possible trial types. 

The code you write should output to the terminal output that looks just like this (that first number is the block number).

```Text
$ python generateTrials.py
1,masked,right
1,masked,left
1,masked,right
1,masked,left
1,nonmasked,right
1,nonmasked,left
2,masked,right
2,masked,left
2,masked,right
2,masked,left
2,nonmasked,right
2,nonmasked,left
3,masked,right
3,masked,left
3,masked,right
3,masked,left
3,nonmasked,right
3,nonmasked,left
4,masked,right
4,masked,left
4,masked,right
4,masked,left
4,nonmasked,right
4,nonmasked,left
5,masked,right
5,masked,left
5,masked,right
5,masked,left
5,nonmasked,right
5,nonmasked,left
```


# ## Exercise 3 parts
# 
# ```{admonition} Challenge!
# 1. Ensure that you can't run the same participant code twice. If you enter a participant code that's already been entered, PsychoPy should pop-up a warning box saying "Participant code already exists". This should prevent you from overwriting an existing data-file. 
# ```
# 
# 1.  Output the trial information and the user's response, one line per response. The file should look like this and should be called results.txt. Your submission should have at least 20 trials of data, i.e., the results.txt file that you push to the repo should have 20 lines.
# 
# |        |        |             |   |      |
# |--------|--------|-------------|---|------|
# | green  | green  | congruent   | 1 | 854  |
# | green  | yellow | incongruent | 1 | 1023 |
# | yellow | green  | incongruent | 0 | 912  |
# | yellow | yellow | congruent   | 1 | 810  |
# 
# 
# Col 1: The word shown
# 
# Col 2: The color of the word
# 
# Col 3: Trial type
# 
# COl 4: 1 for a correct response, 0 for incorrect
# 
# Col 5: The reaction time, in milliseconds.
# 
#  The columns should be separated with commas, i.e., the string containing the first line of the file with the data above would look like this:
#  `green,green,congruent,1,854`
# 
# As in Exercise 2, you should be writing to the file after every trial. Make sure your fine is named `subject-code_data.csv` where `subject-code` is the subject code entered at runtime.
# 
# 
