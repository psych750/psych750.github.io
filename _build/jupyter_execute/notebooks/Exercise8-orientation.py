#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc" style="margin-top: 1em;"><ul class="toc-item"><li><span><a href="#Exercise-8---Interactive-tilt-adjustment" data-toc-modified-id="Exercise-8---Interactive-tilt-adjustment-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Exercise 8 - Interactive tilt adjustment</a></span><ul class="toc-item"><li><span><a href="#Improving-the-design" data-toc-modified-id="Improving-the-design-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Improving the design</a></span></li></ul></li></ul></div>

# # Exercise 8 - Interactive tilt adjustment
# 
# Inside the exercise 8 repo is a 1-page article by [Whitaker and McGraw
# (2000)](http://www.nature.com/neuro/journal/v3/n1/full/nn0100_13.html) who report a curious tilt illusion that I have recreated for you below.

# <img src="images/digitalclocks.png" width="460">

# Believe it or not, the degree of tilt of the numbers in the two alarm clocks is exactly the same. More curious still is that the illusion largely goes away if the stimuli are not plausible numbers (though depending on the conditions, it can be elicited with letters as well). See for yourselves!

# <img src="images/digitalclocks_reversed.png" width="460">

# If we are going to figure out what causes this illusion, we need to start by measuring its strength. How do we do this? Here is how.
# 
# On each trial, the participant will view one of the "standard" images -- numbers or letters presented in the normal or reversed orientation and tilting to the left or right.
# 
# The participants' goal is to adjust the orientation of a small gabor stimulus positioned below the clock display such that it matches the orientation of the standard image. 
# Participants orientation of the gabor using the mouse wheel. 
# 
# Your task is to fill in `do_adjustment()` with the code necessary to display the stimuli, update the orientation of `adjustingStim` and print some data. 
# 
# Since you all know how to write proper data files already, for this exercise, just have the output to print to the terminal in the following way:
# 
# ```
# stimType base orientation angle direction response
# letters ycyc inverted 2 left 3
# letters ycyc upright 5 right 3
# numbers 7-44 upright 12 left 2
# numbers 7-44 inverted 12 left -10
# ```

# Here is the code for getting mouse wheel movements (which are equivalent to scrolling on a
# trackpad, normally a two finger vertical swipe).

# In[ ]:


from psychopy import core, visual, prefs, event
win = visual.Window([800,600],color="white", units='pix')

myMouse = event.Mouse()
myMouse.setVisible(0)

numWheelTurnsDown=numWheelTurnsUp=0
while True:
    wheelRel = myMouse.getWheelRel()[1]
    if wheelRel>0.0:
        numWheelTurnsDown+=1
        print 'wheel down', numWheelTurnsUp, numWheelTurnsDown
    elif wheelRel<0.0:
        numWheelTurnsUp+=1
        print 'wheel up', numWheelTurnsUp, numWheelTurnsDown
        


# And here's your starter code

# In[ ]:


from psychopy import core, visual, prefs, event
from useful_functions import *
win = visual.Window([800,600],color="black", units='pix')
myMouse = event.Mouse()
myMouse.setVisible(0)

pics =  loadFiles('stimuli/','.png','image', win=win)
adjustStim = visual.GratingStim(win=win,tex='sin', mask='gauss',interpolate=True, size=[8,96], pos=[0,-150], color="white")


def do_adjustment(pic):
	numWheelTurnsDown=numWheelTurnsUp=0
	responded=False
	while not responded:
		pics[pic]['stim'].draw()
		adjustStim.draw()

		#insert your code here

		if myMouse.getPressed()[0]==1:
			responded=True
		win.flip()
	

for i in range(10):
	do_adjustment(random.choice(pics.keys()))


# <div class="alert alert-block alert-info">
# Hint: Make sure to print a test message each time you register a response so you can make sure your response collection is working as it should.
# </div>

# ## Improving the design
# 
# What are some things you can add to this experiment to improve the procedure?