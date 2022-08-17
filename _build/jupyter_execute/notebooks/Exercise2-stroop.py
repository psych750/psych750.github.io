#!/usr/bin/env python
# coding: utf-8

# # Exercise 2: The stroop effect
# 
# [Accept the exercise](https://classroom.github.com/a/WEYm669c)
# 
# 
# In this exercise we'll put some of what we've learned so far together into an simple experiment demonstrating the [The Stroop Effect](https://en.wikipedia.org/wiki/Stroop_effect). Then we'll gradually build this codebase out into a full experiment and implement some snazzy things like speech recognition.

# In[4]:


import time
import sys
import random
from psychopy import visual,event,core,gui

stimuli = ['red', 'orange', 'yellow', 'green', 'blue']

win = visual.Window([800,600],color="gray", units='pix')
placeholder = visual.Rect(win,width=180,height=80, fillColor="lightgray",lineColor="black", lineWidth=6,pos=[0,0])
word_stim = visual.TextStim(win,text="", height=40, color="black",pos=[0,0])
instruction = visual.TextStim(win,text="Press the first letter of the ink color", height=20, color="black",pos=[0,-200])
while True:
    cur_stim = random.choice(stimuli)
    word_stim.setText(cur_stim)
    word_stim.setColor(cur_stim)
    placeholder.draw()
    instruction.draw()
    word_stim.draw()
    win.flip()
    core.wait(1.0)
    placeholder.draw()
    instruction.draw()    
    win.flip()
    core.wait(.15)

    if event.getKeys(['q']):
        win.close()
        core.quit()


# Once you've successfully run this code and understand what all the lines do, proceed to the following exercises.

# 1.  Create a fixation cross using a TextStim object `visual.TextStim` set text to "+" and color to "black" and height to 15. Make the fixation cross appear for 500 ms before each color word, and disappear right before the color word appears.
# 
# 2. Rather than cycling throught the colors, use `event.waitKeys()` to wait for a response (e.g., "o" for "orange").  Your script should nly accept 'r', 'o', 'y', 'g', 'b', and 'q' for quit. 
#     ```{tip}
#     Make sure your code has just the functionality it needs, e.g., for part 2, you don't need `event.getKeys(['q'])`
#     ```
# 3. Compute the reaction times -- the time it takes to respond from when the color word appears, to when the user presses a key, in milleconds (e.g., .8 secs should show up as 800). Store these in a list called `RTs`. ([Use psychopy timers](http://www.psychopy.org/api/core.html))
#     ```{tip}
#     Append each reaction time to the RT list after every response
#     ```
# 1.  Now let's implement some feedback. If the user responded correctly, do nothing. If the user responded incorrectly, show "Incorrect" in black letters and add a 1s time delay before going on to the next trial.
#     
# 1.  Now, instead of waiting for a response forever, let's implement a timeout. Show accuracy feedback as before, show "Too slow" if the user takes more than 1.5 secs to respond.
# 
# 1. Introduce *incongruent* trials by showing words in the "wrong" color, e.g., "yellow" printed in green. To do this, define a function called `make_incongruent()` which takes in a color as an argument and returns one of the other colors in `stimuli` that's different from the one being passed in. Then set the color word's color to this new value, thereby creating an incongruent trial. 
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
# Col 2: The color of the word
# Col 3: Trial type
# COl 4: 1 for a correct response, 0 for incorrect
# Col 5: The reaction time, in milliseconds.
# 
#  The columns should be separated with commas, i.e., the string containing the first line of the file with the data above would look like this:
#  `green,green,congruent,1,854`
# 
# You should be writing to the file after every trial.
# 
# 
# 
# ```{tip}
#     See the [python
#     documentation](http://docs.python.org/tutorial/inputoutput.html#reading-and-writing-files)
#     for examples of how to write to a file. **Ask for help if you are
#     stuck.**
# ```
# 
