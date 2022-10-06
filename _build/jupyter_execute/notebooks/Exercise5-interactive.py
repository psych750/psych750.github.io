#!/usr/bin/env python
# coding: utf-8

# # Exercise 5 - Interactive experiments
# 
# [Accept the exercise](https://classroom.github.com/a/bxyDH5Uq)
# 
# Inside the exercise 5 repository is a 1-page article by [Whitaker and McGraw
# (2000)](http://www.nature.com/neuro/journal/v3/n1/full/nn0100_13.html) who report a curious tilt illusion that I have recreated for you below.

# ```{image} images/digitalclocks.png
# :alt: Digital Clock
# :width: 460px
# :align: center
# ```
# 
# 
# 
# 
# 

# Believe it or not, while the numbers in the two alarm clocks are tilted in opposite directions, they are tilted to the exact same degree. More curious still is that the illusion largely goes away if the stimuli are not plausible numbers (though depending on the conditions, it can be elicited with letters as well). See for yourselves!

# ```{image} images/digitalclocks_reversed.png
# :alt: Digital Clock Reversed
# :width: 460px
# :align: center
# ```

# If we are going to figure out what causes this illusion, we need to start by measuring its strength. The exercise has two purposes. First, it serves as an example of a simple interactive experiment and is designed to help you cement some coding patterns we've been working on (loading in external files) while also teaching you some new things (how to use the mouse for responding). Second, it's a nice illustration of how we go about measuring the strength of an illusion. 
# 

# 
# On each trial, the participant will view one of the "standard" images -- numbers or letters presented in the normal or reversed orientation and tilting to the left or right.
# 
# The participants' goal is to adjust the orientation of a small line positioned below the clock display such that it matches the orientation of the standard image. The extent 
# Participants orientation of the gabor using the mouse wheel. 
# 
# Your task is to fill in `do_adjustment()` with the code necessary to display the stimuli, update the orientation of `adjusting_stim` and write some data to a CSV file for later analysis.
# 

# Here is the code for getting mouse wheel movements (which are equivalent to scrolling on a
# trackpad, normally a two finger vertical swipe).

# In[2]:


from psychopy import core, visual, prefs, event
win = visual.Window([800,600],color="white", units='pix')

myMouse = event.Mouse()
myMouse.setVisible(0)

num_wheel_turns_down=num_wheel_turns_up=0
while True:
    wheelRel = myMouse.getWheelRel()[1]
    if wheelRel>0.0:
        num_wheel_turns_down+=1
        print('wheel down: ', num_wheel_turns_up, num_wheel_turns_down)
    elif wheelRel<0.0:
        num_wheel_turns_up+=1
        print('wheel up', num_wheel_turns_up, num_wheel_turns_down)
        


# Your starter code has this code wrapped in a `do_adjustment()` function. We'll go over it in class.

# ## Part 1
# 
# Grab a set of runtime variables using a GUI box as we did previously. You should have an error check built-in so you don't overwrite an existing data file. Also use the saving state trick I showed you to load in the previous values you used, so if you ran subject tilt_103, that's the value that comes up in the GUI box the next time you run.
# 
# 
# For the runtime variables, just use these:
# 
# * Subject code
# * Random seed (controls the pseudo-random order)
# * Number of blocks (an integer -- one controls how many times we go through the stimulus list)
# 

# ## Part 2
# 
# Pass these runtime variables to generate_trials() so that it generates a subjCode_trials.csv trial file with the correct properties. This one's very simple -- just iterate through all the image files number of blocks times, in pseudo-random order (determined by the seed). The starter code for `generate_trials()` uses `os.glob()` to get a list of filenames inside the `stimuli` directory. Notice that the starter code for `generate_trials()` breaks up the fiename into its fields. Write these into appropriate columns in your trials file so that you can read them in and use them in your main script.

# ## Part 3
# 
# Read in the trial file -- use column headers! --  show the appropriate trial and collect the response. For this part, just print the response (the angle of the adjustable bar), to the console. No need to write to a data-file just yet. 

# ## Part 4
# 
# Write the result to a data-file: subj_code_data.csv placed inside a data subfolder. The data-file should be in the following format. *Please make sure your format is exactly this -- these columns in this order, separated by commas*
# 
# ```
# Col 1: trial_number (beginning with 1)
# Col 2: subject_code
# Col 3: random_seed
# Col 4: number_of_blocks (defaulting to 1 for this exercise)
# Col 5: displayed_string
# Col 6: orientation
# Col 7: true_angle
# Col 8: tilt_direction
# Col 9: matched_angle -- participnt's response (vertical = 0)
# Col 10: signed_error (positive means the adjusted stimulus leans too much to the right; negative = too much to the left, 0 = perfectly correct)
# Col 11: absolute error (absolute difference between true_angle and matched_angle -- make sure you are mindful of the tilt direction difference b/w left 7 and right 7 is 14)
# Col 12: RT - reaction time from stimulus onset to response, in milliseconds, rounded to the nearest millisecond
# ```
# 
# The first line of your file should be the column names, i.e,
# 
# ```
# trial_number,subject_code,random_seed,number_of_blocks,displayed_string,orientation,true_angle,tilt_direction,matched_angle,signed_error,absolute_error,RT
# ```
# 
