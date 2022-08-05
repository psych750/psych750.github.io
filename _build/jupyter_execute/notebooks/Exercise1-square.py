#!/usr/bin/env python
# coding: utf-8

# # Exercise 1: Make a square and play with it

# The following bit of code will show a blue square for 500 ms and then exit out of the program.

# In[1]:


import time
import sys
from psychopy import visual,event,core
 
win = visual.Window([400,400],color="black", units='pix') #open a window
square = visual.Rect(win,lineColor="black",fillColor="blue",size=[100,100]) #make a blue square
square.draw() #draw the square to the buffer
win.flip() #make the buffer visible
core.wait(.5) #pause for 500 ms (half a second)
win.close() #close the window -- don't need this if you're running this as a separate file
sys.exit()


# ## Go through each line and understand what it does. Then...
# 
# 1. Make the square red instead of blue
# 
# 1. Make the square appear for 1.5 secs.
# 
# 1. Show a red square for 1 s, then switch it to blue and show it for 1 s
# 
# 1. Make the square appear for 1.5 secs, then show a blank screen for 1 sec, then flash the square 3 times for 30 ms each.
# 
# 1. Show the following sequence: blue, red, blue, red, blue, red (with each square appearing for 1 s with a 50 ms blank screen in the middle).
# 
# 1. Show a red square for 1 s then change its orientation by 45-deg
# 
#     <div class="alert alert-block alert-info">
#     To change the orientation by a certain degree-value use square.setOri(value) where `value` is the new orientation.
#     </div>
#     
# 1. Now make a square rotate continuously, one full revolution (360 degrees) per second
#     <div class="alert alert-block alert-info">
#     To increase orientation use `square.ori += value` where `value` is the value by which to increase the
#     orientation.
#     </div>
# 
# 1. Make a rotating square stop rotating when you press the 's' key
# 
#     <div class="alert alert-block alert-info">
#     To accept keyboard input you'll want to check it event.getKeys(['s']) is True. 
#     </div>
# 
# 1. Make a square stop rotating when you press 's' and then start rotating again when you press 'r'
# 
# 1. Display a blue square and increase its width (making it a rectangle) by 10 pixels whenever the user presses the left-arrow key. Decrease the width by 10 pixels when the user presses the right-arrow key
# 
#     <div class="alert alert-block alert-info">
#     The key codes for right and left arrows in PsychoPy are simply 'right' and 'left'
#     </div>
# 
#     <div class="alert alert-block alert-info">
#     To change the width use `square.size += [x,y]` where `x` and `y` are the values by which you want to change the 
#     size
#     </div>
# 
# 1. Make the rectangle decrease/increase its width by 10% of its current width with each keypress instead of 10 pixels
# 
# 1. Show *two* rotating squares simultaneously, one left of center rotating clockwise, the other right of center, rotating counterclockwise
# 
# 1. As time allows, do something that's not listed here (e.g., make it a pentagon instead of a square, make it pulsate, play a sound as it moves, bounce off walls.. be creative.
# 