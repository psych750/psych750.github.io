#!/usr/bin/env python
# coding: utf-8

# # Exercise 2: Display some text, take in responses, read from a file
# 
# In this exercise we'll put what you've learned about lists and conditionals to use. Plus we'll read and write files! By the end of today you will start to have almost all the pieces for building a full experiment!
# 
# Requirements: Make sure you have a names.txt file in your repo. If you're using this as a tutorial, [download this sample file](names.txt) 
# 

# In[ ]:


import time
import sys
import random
from psychopy import visual,event,core,gui


names = open('names.txt', 'r').readlines()
firstNames = [name.split(' ')[0] for name in names]

"""
the two line above are a more compact way of writing: 
names = open('names.txt', 'r').readlines()
firstNames=[]
for name in names:
    firstNames.append(name.split(' ')[0])
"""	

win = visual.Window([800,600],color="black", units='pix')
firstNameStim = visual.TextStim(win,text="", height=40, color="white",pos=[0,0])
while True:
    nameShown = random.choice(firstNames)
    firstNameStim.setText(nameShown)
    firstNameStim.draw()
    win.flip()
    core.wait(.75)
    win.flip()
    core.wait(.15)

    if event.getKeys(['q']):
        break


# Once you've successfully run this code and understand what all the lines do, proceed to the following exercises.

# 1.  Create a fixation cross using a TextStim object `visual.TextStim` set text to"+" and color to "white". Make the fixation cross appear for 500 ms before each name
#     and disappears right before the name comes up. 
#     
# 2.  Open names.txt to see what the names list looks like. Make the script
#     show last names instead of first names (don't change the names.txt
#     file). 
# 
# 3.  Make the program randomly alternate between first names and last
#     names.
# 
# 4.  On each presentation of a name, wait for a response ('f' for first
#     name, 'l' for last-name) and only proceed to the next name if the
#     response is correct. Hint: if you've done steps 2-3 properly, this
#     should be really easy. Refer to the psychopy documentation of
#     event.waitKeys() if you have trouble.
# 
# 6.  Now let's implement some feedback. Let's allow either a 'f' or
#     'l' response for each trial. If the response is correct, show a
#     green 'O' before the start of the next trial. If the response is
#     wrong, show a red 'X' (you can use textStim objects for feedback).
#     Show the feedback for 500 ms. Note: we have someone in a class whose
#     last name is a common first name. If this were an experiment, how
#     might this affect responses?
#     
# 7.  Now, instead of waiting for a response forever, let's implement a
#     timeout. Show accuracy feedback as before, but now also show a red
#     'X' if no response is received for 1 sec (and go on to the next
#     trial automatically following the feedback). ([Use psychopy timers](http://www.psychopy.org/api/core.html))
# 8. [Pop up a box](http://sapir.psych.wisc.edu/programming_for_psychologists/notebooks/Psychopy_reference.html#Popping-up-a-box-to-get-user-input-e.g.,-to-specify-a-condition-name) that accepts a first name, and check to make sure
#     that the name exists. If it doesn't, pop-up a ['Name does not exist'error](http://sapir.psych.wisc.edu/programming_for_psychologists/notebooks/Psychopy_reference.html#A-simple-function-for-popping-up-an-error-using-a-gui-window)
#     box
# 9.  Extend the task by requiring the subject to respond by pressing a
#     spacebar (the key is called 'space'), as quickly as possible anytime the name on the screen matches the name you entered into the box (so if I enter 'Gary' I
#     would have to press 'space' anytime the name 'Gary' shows up. If
#     the participant presses 'space' to the wrong name (false alarm),
#     or misses the name (a miss), show a red X.
# 10. See if you can figure out how to compute the response times,
#     measured from the onset of the name, to the response ([Use psychopy
#     timers](http://www.psychopy.org/api/core.html))
# 11. Output the response times (in ms, e.g., 453 for 453 ms) and accuracy
#     (1 for correct, 0 for incorrect) to a file output.txt. Output one
#     line per trial: each line should contain the accuracy (1 or 0) and
#     the response time (in milliseconds). See the [python
#     documentation](http://docs.python.org/tutorial/inputoutput.html#reading-and-writing-files)
#     for examples of how to write to a file. **Ask for help if you are
#     stuck.**
# 12. Do something new. Compare response times to first and last names, measure effect of font face, etc.
# 
# -   Bonus: You've probably noticed that the name you typed in only
#     appears rarely (in fact, it will appear 1/# of people in the class,
#     on average). Change the code so that the name you entered appears on
#     1/4 of the trials.

# In[ ]:




