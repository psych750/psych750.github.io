#!/usr/bin/env python
# coding: utf-8

# # Exercise 4: Modularizing your code + speech recognition!
# 
# [Accept the exercise](https://classroom.github.com/a/spMcCFUF).
# 
# For this exercise, you may either join a team (limited to 2 people) or work individually.
# 
# The purpose of this exercise is to get you more comfortable with the solution I posted for Exercise 3 and to further modularize it (Parts 1-3) and add a voice response option (Parts 4-5).  
# 
# 

# ## Part 1.
# Take the stimulus presentation & response collection code -- the stuff that sets colors, orientations, does win flips, & collects responses -- and place it into a `show_trial()` function. You'll need to decide what arguments this function should take (the fewer the better!) and what the function should return. If done correctly, you should not have any setText, setOri, setColor, core.wait, or win.flip commands outside of this function.

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
# For this part, avoid using this conditional (if/else statement) by creating and using an appropriate dictionary.

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
# Not only is this a lot of repetitive code, but it requires us to know which column is which. Improve this code by adding column names to the trial list so that you know which column is which. When you read the trials back in, read it in so that you can them by name, e.g., `cur_trial[text_color]` would access what the text color should be for the current trial. You can do this by using a Python dictionary (your trials would now be now be a list of dictionaries!) **OR** using a Pandas data-frame. You can see an example of iterating through rows of a Pandas dataframe [here](https://stackoverflow.com/questions/16476924/how-to-iterate-over-rows-in-a-dataframe-in-pandas). For more on how to access rows/columns of Pandas dataframes, see [here](https://pythonhow.com/python-tutorial/pandas/Accessing-pandas-dataframe-columns-rows-and-cells/).  Note that iterating through rows of a data-frame like this is not advised in contexts when you need to do something to every row, but it's fine here since we're just using the dataframe as a source of information telling us what we need to do on each trial.

# ## Part 4
# 
# In the original demonstration of the Stroop effect, participants responded by using their voices. The researcher used a stopwatch to time how long it took to read a block of incongruent trials and compared it to reading a block of congruent trials. We can do a bit better. In this part, we'll be using some out-of-the-box speech recognition to decode what word the participant is saying and scoring it as correct or incorrect. We'll also use a (somewhat imprecise) psychopy function to automatically compute the onset time of people's verbal responses. 
# 
# The `speech_recognition.py` file in your starter code has a minimal example of how to use OpenAI's free [whisper model](https://github.com/openai/whisper#setup). This file also imports a function to calculate onset times -- the time it took you to start speaking (like a reaction time for your voice). 
# 
# Follow the [installation instructions](https://github.com/openai/whisper#setup) to install whisper **and its dependencies**. You'll want to start by running 
# ```bash
# pip install git+https://github.com/openai/whisper.git 
# ```
# and install `ffmpeg` as instructed on the whisper github page. 
# 
# You should then be able to run the `speech_recognition.py` that's part of your starter code. After verifying that it runs, incorporate it into your main code to enable participants to respond using their voice. Ideally, you'll have a function like `transcribe_response()` which contains the relevant code so that your `show_trial()` code is free of any code specific to speech recognition.
# 
# Because speech recognition takes some time, you may need to lengthen the period of time in between trials to allow the response to process.
# 
# For the purposes of part 4 print the transcribed text and onset times to the console after each trial to a file called `speech_recognition.txt` and push it to the repository along with the rest of your part 4 code. 
# 
# :::{note}
# We've had some trouble with the speech recognition code when a headset is connected (it seems to get confused about which mic to use). So if the code is crashing with an `Abort trap` message that's probably what it is. Disconnect the headset and try again. Also, the speech recognition (whisper) library is quite robust to background noise. The speech onset detection algorithm, however, is not. If you're getting times close to 0 for speech onsets, try testing in a more quiet environment.
# :::
# 

# ## Part 5
# 
# Add `response_type` to the pop-up (GUI) box. The value of this variable can be either "voice" or "key". If it's key, proceed with the experiment as before. If it's voice, have it use the speech-recognition voice capability. `is_correct` should be 1 if the said word matched the text color (i.e., person said "green" and it was actually green), 0 if not, and 'NA' if there was some processing error. RT should reflect the measured speech onset or NA if it couldn't be measured. The results file should also include the response, as recognized. If a person said "green", it should record "green". The response_type variable should be added to the other runtime variables (like participant code) and stored in your output file. 
# 
# If the person is responding with voice, then the `resp` column should contain their (transcribed, lowercased) response, `is_correct` should (as before) indicate whether the response was correct or not and the `RT` column should contain the speech onset time.  
# 
# Please run yourself on 20 trials in the keyboard condition and 20 trials in the voice condition. **Make sure the value of `response_type` is included in the data file (so that someone looking at it later would know how the responses were collected).**
