#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc" style="margin-top: 1em;"><ul class="toc-item"><li><span><a href="#Psychopy-reference" data-toc-modified-id="Psychopy-reference-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Psychopy reference</a></span><ul class="toc-item"><li><span><a href="#A-simple-function-for-popping-up-an-error-using-a-gui-window" data-toc-modified-id="A-simple-function-for-popping-up-an-error-using-a-gui-window-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>A simple function for popping up an error using a gui window</a></span><ul class="toc-item"><li><span><a href="#Popping-up-a-box-to-get-user-input-e.g.,-to-specify-a-condition-name" data-toc-modified-id="Popping-up-a-box-to-get-user-input-e.g.,-to-specify-a-condition-name-1.1.1"><span class="toc-item-num">1.1.1&nbsp;&nbsp;</span>Popping up a box to get user input e.g., to specify a condition name</a></span></li><li><span><a href="#A-different-way-of-showing-a-text-box" data-toc-modified-id="A-different-way-of-showing-a-text-box-1.1.2"><span class="toc-item-num">1.1.2&nbsp;&nbsp;</span>A different way of showing a text box</a></span></li><li><span><a href="#Easy-way-to-get-runtime-variables" data-toc-modified-id="Easy-way-to-get-runtime-variables-1.1.3"><span class="toc-item-num">1.1.3&nbsp;&nbsp;</span>Easy way to get runtime variables</a></span></li></ul></li><li><span><a href="#How-do-I-have-people-respond-with-a-mouse?" data-toc-modified-id="How-do-I-have-people-respond-with-a-mouse?-1.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>How do I have people respond with a mouse?</a></span><ul class="toc-item"><li><span><a href="#Get-mouse-position-of-mouse-at-point-of-buttonpress" data-toc-modified-id="Get-mouse-position-of-mouse-at-point-of-buttonpress-1.2.1"><span class="toc-item-num">1.2.1&nbsp;&nbsp;</span>Get mouse position of mouse at point of buttonpress</a></span></li><li><span><a href="#Show-text-until-mouse-click" data-toc-modified-id="Show-text-until-mouse-click-1.2.2"><span class="toc-item-num">1.2.2&nbsp;&nbsp;</span>Show text until mouse click</a></span></li><li><span><a href="#Wait-for-click-on-a-picture" data-toc-modified-id="Wait-for-click-on-a-picture-1.2.3"><span class="toc-item-num">1.2.3&nbsp;&nbsp;</span>Wait for click on a picture</a></span></li></ul></li><li><span><a href="#How-do-I-keep-doing-something-while-waiting-for-a-response?" data-toc-modified-id="How-do-I-keep-doing-something-while-waiting-for-a-response?-1.3"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>How do I keep doing something while waiting for a response?</a></span><ul class="toc-item"><li><span><a href="#A-generic-function-for-collecting-responses" data-toc-modified-id="A-generic-function-for-collecting-responses-1.3.1"><span class="toc-item-num">1.3.1&nbsp;&nbsp;</span>A generic function for collecting responses</a></span></li><li><span><a href="#A-function-for-writing-a-string-(trial-info)-to-a-file." data-toc-modified-id="A-function-for-writing-a-string-(trial-info)-to-a-file.-1.3.2"><span class="toc-item-num">1.3.2&nbsp;&nbsp;</span>A function for writing a string (trial info) to a file.</a></span></li></ul></li><li><span><a href="#Convert-from-polar-to-rectangular-coordinates" data-toc-modified-id="Convert-from-polar-to-rectangular-coordinates-1.4"><span class="toc-item-num">1.4&nbsp;&nbsp;</span>Convert from polar to rectangular coordinates</a></span></li><li><span><a href="#Staircasing" data-toc-modified-id="Staircasing-1.5"><span class="toc-item-num">1.5&nbsp;&nbsp;</span>Staircasing</a></span></li><li><span><a href="#Preloading-image-and-audio-files" data-toc-modified-id="Preloading-image-and-audio-files-1.6"><span class="toc-item-num">1.6&nbsp;&nbsp;</span>Preloading image and audio files</a></span></li><li><span><a href="#A-sample-factorial-design-trial-list-generation-file-(generateTrials.py)" data-toc-modified-id="A-sample-factorial-design-trial-list-generation-file-(generateTrials.py)-1.7"><span class="toc-item-num">1.7&nbsp;&nbsp;</span>A sample factorial design trial list generation file (generateTrials.py)</a></span></li><li><span><a href="#Importing-a-trial-list" data-toc-modified-id="Importing-a-trial-list-1.8"><span class="toc-item-num">1.8&nbsp;&nbsp;</span>Importing a trial list</a></span></li><li><span><a href="#A-function-for-grabbing-screenshots" data-toc-modified-id="A-function-for-grabbing-screenshots-1.9"><span class="toc-item-num">1.9&nbsp;&nbsp;</span>A function for grabbing screenshots</a></span></li><li><span><a href="#Popping-up-a-web-based-survey-from-within-your-python-script" data-toc-modified-id="Popping-up-a-web-based-survey-from-within-your-python-script-1.10"><span class="toc-item-num">1.10&nbsp;&nbsp;</span>Popping up a web-based survey from within your python script</a></span><ul class="toc-item"><li><span><a href="#Google-form" data-toc-modified-id="Google-form-1.10.1"><span class="toc-item-num">1.10.1&nbsp;&nbsp;</span>Google form</a></span></li><li><span><a href="#Qualtrics-forms" data-toc-modified-id="Qualtrics-forms-1.10.2"><span class="toc-item-num">1.10.2&nbsp;&nbsp;</span>Qualtrics forms</a></span></li></ul></li><li><span><a href="#Using-a-webcam-in-psychopy" data-toc-modified-id="Using-a-webcam-in-psychopy-1.11"><span class="toc-item-num">1.11&nbsp;&nbsp;</span>Using a webcam in psychopy</a></span></li></ul></li></ul></div>

# # Psychopy reference
# 
# Please use the official [psychopy reference](http://www.psychopy.org/api/api.html) page for basic info.
# Below is some extra functionality that you will find useful.

# ## A simple function for popping up an error using a gui window

# ```python
# from psychopy import visual, gui
# 
# def popupError(text):
#     errorDlg = gui.Dlg(title="Error", pos=(200,400))
#     errorDlg.addText('Error: '+text, color='Red')
#     errorDlg.show()
# 
# popupError('There was an error!')
# ```

# ### Popping up a box to get user input e.g., to specify a condition name
# 
# Here's the simplest code:
# 
# ```python
# from psychopy import visual, gui
# 
# userVar = {'Name':'Enter your name'}
# dlg = gui.DlgFromDict(userVar)
# ```
# 
# You can now access the value of the 'Name' variable using the
# following syntax:
# 
# ```python
# userVar['Name']
# ```
# 
# For example, if I enter 'Gary' in the pop-up box. Then once I press
# enter and the box closes,
# 
# ```python
# userVar['Name']
# ```
# 
# will return the string 'Gary'
# 
# Note that when the box pops up it will be pre-filled with "Enter your
# name". To overwrite it, just hit tab until it's highlights. Or
# position your cursor inside it, hit command-A (ctrl-A on PC) which will
# highlight all the text, and then start typing. For a more elegant text
# box, see below.

# ### A different way of showing a text box
# 
# ```python
# myDlg = gui.Dlg()
# myDlg.addText('Enter your name')
# myDlg.addField('Name:')
# myDlg.show()
# #when the box closes, the data you want will be in myDlg.data
# #if you want to get a bit fancier, you can monitor the 'OK' or 'cancel' press:
# if myDlg.OK:  # then the user pressed OK
#     # this will print the list of passed in values in the order in which you added the fields above.
#     print myDlg.data 
# else:
#     print 'user cancelled'
# ```
# 
# Note that `myDlg.data` is a list, so you access the first element, you
# should index it: `myDlg.data[0]`
# 

# ### Easy way to get runtime variables
# 
# Runtime variables are variables you want to set at runtime -- the subject code, demographic info, the condition(s) the subject is assigned to, etc.
# 
# ```Python
# def getRunTimeVars(varsToGet,order,expVersion):
#     #Get run time variables, see http://www.psychopy.org/api/gui.html for explanation
#     infoDlg = gui.DlgFromDict(dictionary=varsToGet, title=expVersion, fixed=[expVersion],order=order)
#     if infoDlg.OK:
#         return varsToGet
#     else: 
#         print 'User Cancelled'
# ```
# 
# Sample usage:
# 
# ```Python
# order =  ['subjCode','seed','gender']
# runTimeVars = getRunTimeVars({'subjCode':'pGrouping_101', 'seed':10, 'gender':['Choose', 'male','female']}, order, 'ver1')
# ```
# 

# ## How do I have people respond with a mouse?
# 
# PsychoPy makes it very easy to collect mouse responses.
# 
# ### Get mouse position of mouse at point of buttonpress
# The following code shows you how you get the coordinates of the mouse at the point that a user presses a button.

# In[ ]:


from psychopy import core, visual, event

win = visual.Window([300,300],color="black", units='pix')
mouse = event.Mouse(win=win)

while True:
    if any(mouse.getPressed()): #if any mouse button is pressed
        mouse_pos = mouse.getPos() #get its position at time of button press
    break
print 'user clicked at', mouse_pos
    


# `getPressed()` returns a list of mouse button states, e.g., [0,0,0] which will always evaluate to `True`. The built-in function `any()` allows us to check if any of the values in the list are `True`

# ### Show text until mouse click
# 
# One difference between keyboards and mice is that `event.getKeys(['d'])` becomes false as soon as 'd' key is pressed (the 'd' is removed from the buffer and a single key-press corresponds to a single event). In contrast, `mouse.getPressed()` will be true as long as a mouse button is held. This means that if you have several text screens, it's easy to scroll through all of them real quick in the time that the user is holding down the mouse-button. Here's a simple function that allows you to show text and wait for either a keyboard or mouse response

# In[ ]:


def showText(win,text,color,mouse):
	visual.TextStim(win,text=text,color=color,height=30).draw()
	win.flip()
	if mouse:
		while True:
			while any(mouse.getPressed()):
				if not any(mouse.getPressed()):
					return
	else:
		event.waitKeys()
		return


# ### Wait for click on a picture
# The following code waits until a user clicks on one of the items (any visual objects) currently displayed

# In[ ]:


#.... mouse, window, pic1, pic2, pic3 initialization

	#check mouse until pressed in one of the pics
	while True:
		if mouse.isPressedIn(pic1) or mouse.isPressedIn(pic2) or mouse.isPressedIn(pic3):
			response = mouse.getPos()
			break

    #assuming pic1 is the correct response
	#check if response is correct
	if pic1.contains(response):
		correctFeedback.draw()
	else:
		incorrectFeedback.draw()
	win.flip()


# ## How do I keep doing something while waiting for a response?
# 
# 
# If you need to wait for a user's response and you don't need to change anything on the screen you should use `event.waitKeys()`. If, however, you need to update the screen while waiting for a response, use `event.getKeys()` inside a loop.
# 
# This loop will execute until a user presses the 'q' or spacebar.
# 
# ```python
# while not event.getKeys(keyList=['q','space']):
#     #do stuff here
# ```
# 
# To terminate based on *any* keypress, just use the getKeys() function
# without any arguments:
# 
# ```python
# while not event.getKeys():
#     #do stuff here
# ```
# 
# **Caution**: If you have a `win.flip()` inside a loop, that loop will execute at most every screen-refresh (or slower if you're doing something computationally intensive inside the loop). That means that if you have a `event.getKeys()` inside the loop, you will only be checking responses every screen-refresh. At 60Hz, that means that all your responses will be rounded up to the next 16.67 ms -- probably not what you want!
# 
# 

# ### A generic function for collecting responses
# 
# ```python
# from psychopy import event, core
# 
# def getKeyboardResponse(validResponses,duration=0):
#     """Returns keypress and RT. Specify a duration (in secs) if you want response collection to last that long. Unlike event.waitkeys(maxWait=..), this function will not exit until duration. Use waitKeys with a maxWait parameter if you want to have a response deadline, but exit as soon as a response is received."""
# 
#     event.clearEvents() 
#     #not strictly necessary here, but good practice - 
#     #will prevent buffer overruns if, for some reason there are too many responses in
#     #between auto-clears (e.g., from mouse, eye tracking data)
#     
#     responded = False
#     done = False
#     rt = '*'
#     responseTimer = core.Clock()
#     while True: 
#         if not responded:
#             responded = event.getKeys(validResponses, responseTimer) 
#         if duration>0:
#             if responseTimer.getTime() > duration:
#                 break
#         else: #end on response
#             if responded:
#                 break
#     if not responded:
#         return ['*','*']
#     else:
#         return responded[0] #only get the first resp
# ```

# ### A function for writing a string (trial info) to a file.
# 
# ```Python
# def writeToFile(fileHandle,trial,sync=True):
#     #Writes a trial (array of lists) to a file.
#     #File needs to be opened outside the function. Pass in the filehandle as an argument.
#     line = '\t'.join([str(i) for i in trial]) #TABify
#     line += '\n' #add a newline
#     fileHandle.write(line)
#     if sync:
#         fileHandle.flush()
#         os.fsync(fileHandle)
# 
# # Usage:
# subjDataFile = open('subj1.txt', 'w')
# trial = ['dog', 143.9, 0]
# writeToFile(subjDataFile, trial)
# ```

# ## Convert from polar to rectangular coordinates
# 
# You'll want to do this if you you're trying to display stimuli arranged in a
# circle. As it happens, psychopy provides a handy [set of functions](http://www.psychopy.org/api/tools/coordinatetools.html) for this.
# 
# Converting between polar and rectangular coordinates is simple trig and it's important to understand exactly what it's doing (not magic, just trig). Below is a function I've written for use in my pre-psychopy days. The function is a more general version of the
# built-in one, allowing you to pass in a list of angles:
# 
# ```python
# from math import *
# 
# def polarToRect(angleList,radius):
#     """Accepts a list of angles and a radius.  Outputs the x,y positions for the angles"""
#     coords=[]
#     for curAngle in angleList:
#         radAngle = (float(curAngle)*2.0*pi)/360.0
#         xCoord = round(float(radius)*cos(radAngle),0)
#         yCoord = round(float(radius)*sin(radAngle),0)
#         coords.append([xCoord,yCoord])
#     return coords
# 
# polarToRect([0,30,60,90],50) #generate the x,y coordinates for supplied angles with a radius of 50
# # [[50.0, 0.0], [43.0, 25.0], [25.0, 43.0], [0.0, 50.0]]
# ```
#  
# **Hint:** You can use list comprehension to make psychopy's built-in function work like the one above:
# 
# ```python
# from psychopy.tools import coordinatetools
# [coordinatetools.pol2cart(theta,50) for theta in (0,30,60,90)]
# ```
# 
# You can plug a `round()` in there to take care of the rounding. (Best not
# to set the position of your stimulus to something to the negative 15th power.)
# 
# ```python
# [((round(coords[0],0), round(coords[1],0))) for coords in [coordinatetools.pol2cart(theta,50) for theta in (0,30,60,90)]]
# ```

# ## Staircasing
# 
# PsychoPy has a staircasing feature that is useful if we are trying to find a threshold (e.g., what stimulus contrast leads to 80% performance?). It is also useful if we need to equalize performance in several conditions, e.g., if we want to show different pictures at different durations such that each is recognized with equivalent accuracy.  Staircasing is implemented by the Stairhandler object. It has [lots of attributes] (http://www.psychopy.org/api/data.html#psychopy.data.StairHandler). The example below shows one common way you might use it.
# 
# Note that I will use the term "intensity" when referring to the value of the staircasing parameter because staircasing is traditionally used to calibrate intensities, but this can be anything: duration of an object's presentation on the screen, the time between an object and a mask, the difference in orientation between two Gabors, etc.

# In[ ]:


from psychopy import data
import random

staircase = data.StairHandler(
    startVal=20.0,
    stepType='lin', #the type of step change can also be log or db
    stepSizes=[8, 4, 4, 2, 2, 1, 1],  # step sizes after each reversal
    minVal=0, maxVal=90, #the range of values we want the signal to take
    nUp=1, nDown=3,  # will home in on the 80% threshold
    nTrials=50) #max number of trials

'''
staircase is an iterator; you can get its next stat by calling 
staircase.next(), or having it in a loop:
'''
for curTrial in staircase:
    print curTrial
    #curTrial will contain the current intensity value, here, beginning with 20 
    staircase.addResponse(1) # 1 if response is correct; 0 if incorrect


# When you're done iterating, you of course have the final intensity value, and can get some additional information, e.g., 
# 
# `numpy.average(staircase.reversalIntensities[-6:]))` gives you the average of intensities of the last 6 reversals.
# 

# In addition to the basic StairHandler, PsychoPy implements [staircasing based on the  QUEST algorithm](http://www.psychopy.org/api/data.html#questhandler). It's used just like the stairhandler above, but the attributes are a bit different. The advantage of QUEST is that it allows for faster convergence.

# ## Preloading image and audio files
# A flexible routine for preloading image and audio files that meet particular conditions
# 
# ```python
# import os
# import glob
# from psychopy import visual
# 
# def loadFiles(directory,extension,fileType,win='',whichFiles='*',stimList=[]):
# 	""" Load all the pics and sounds. Uses pyo or pygame for the sound library (see prefs.general['audioLib'])"""
# 	path = os.getcwd() #set path to current directory
# 	if isinstance(extension,list):
# 		fileList = []
# 		for curExtension in extension:
# 			fileList.extend(glob.glob(os.path.join(path,directory,whichFiles+curExtension)))
# 	else:
# 		fileList = glob.glob(os.path.join(path,directory,whichFiles+extension))
# 	fileMatrix = {} #initialize fileMatrix  as a dict because it'll be accessed by file names (picture names, sound names)
# 	for num,curFile in enumerate(fileList):
# 		fullPath = curFile
# 		fullFileName = os.path.basename(fullPath)
# 		stimFile = os.path.splitext(fullFileName)[0]
# 		if fileType=="image":
# 			try:
# 				stim = visual.ImageStim(win, image=fullPath,mask=None,interpolate=True)
# 				(width,height) = (stim.size[0],stim.size[1])
# 				fileMatrix[stimFile] = {'stim':stim,'fullPath':fullPath,'filename':stimFile,'num':num,'width':width, 'height':height}
# 			except:
# 				print "Need to define window before loading stimuli"
# 		elif fileType=="sound":
# 			fileMatrix[stimFile] = {'stim':sound.Sound(fullPath), 'duration':sound.Sound(fullPath).getDuration()}
# 
# 	#optionally check a list of desired stimuli against those that've been loaded
# 	if stimList and set(fileMatrix.keys()).intersection(stimList) != set(stimList):
# 		popupError(str(set(stimList).difference(fileMatrix.keys())) + " does not exist in " + path+'\\'+directory) 
# 	return fileMatrix
# 
# 
# win = visual.Window([200,200],color="black", units='pix')
# fileMatrix = loadFiles('stimuli/visual','.png',fileType="image",win=win)
# 
# ```
# 
# Sample usage, assuming your stimuli are in stimuli subfolders:
# 
# ```python
# picStims = loadFiles('stimuli/pics','.jpg','image', win=win)
# soundStims = loadFiles('stimuli/sounds','.wav','sound', win=win)
# ```
# 
# You can optionally specify stimList (the list of stims you'll be using
# in the experiment). This is not necessary, but lets you check to make
# sure that all the stimuli you need are available.
# 
# Now you can display the image dog.jpg like so:
# 
# ```python
# picStims['dog']['stim'].draw()
# win.flip()
# ```
# 
# Get the full path of the image like this:
# 
# ```python
# picStims['dog']['fullPath']
# ```
# 
# You can play a sound like this
# 
# ```python
# soundStims['beep']['stim'].play()
# ```
# 
# And get its duration like this:
# 
# ```python
# soundStims['beep']['duration']
# ```

# ## A basic factorial design trial list generation file (generateTrials.py)

# ```python
# import random
# 
# stims = ["cat", "car", "dog", "frog", "gun","motorcycle","rooster", "train", "cow", "whistle"] 
# primeTypes = ["label","sound","noPrime"]
# side = {'left':'right','right':'left'}
# isValid = ["0"]*1+["1"]*4
# separator = ","
# seed=10
# 
# headerCols = ['curStim', 'curPrimeType', 'curIsValid', 'curSoundFile', 'curTargetSide', 'curDistractorSide']
# header = separator.join(headerCols)
# 
# 
# def generateTrials(subjCode,seed):
#     trialList=[]
#     for curStim in stims:
#         for curPrimeType in primeTypes:
#             for curIsValid in isValid:
#                 for curTargetSide in side.keys():
#                     if curPrimeType=='noPrime':
#                         soundFile = 'noise'
#                         curIsValid = '*'
#                     else:
#                         if curIsValid=="1":
#                             curSoundFile = '_'.join([curStim,curPrimeType])
#                         elif curIsValid=="0":
#                             curSoundFile = '_'.join([randomButNot(stims,curStim),curPrimeType])
#                     curDistractorSide = side[curTargetSide]
#                     try:
#                         trial = separator.join(map(str,map(eval,headerCols)))
#                     except NameError:
#                         print 'column not defined.  check code'
#                     trialList.append(trial)
# 
#     random.seed(seed)
#     random.shuffle(trialList)
#     try:
#         trialFile = open('trialList_'+subjCode+'.csv','w')
#         trialFile.write(header+'\n')
#         [trialFile.write(curTrial+'\n') for curTrial in trialList]
#         return trialList
#     except:
#         return False
# 
# if __name__ == "__main__":
#     #for testing; this part is only executed if you run generateTrials.py from the terminal.
#     trialList = generateTrials('test',10)
#     print header
#     for curTrial in trialList:
#         print curTrial
# ```

# To use it inside your main experiment file, import it like so:
# 
# ```python
# from generateTrials import generateTrials
# ```
# 
# (this assumes that the code above is placed in a file called
# generateTrials.py) Now, you can create a trialList_subjCode.csv file by
# having a line like this in your main experiment file (making sure that
# subjCode and seed are contain the values entered at runtime:
# 
# ```python
# generateTrials(subjCode,seed)
# ```

# ## Importing a trial list
# A flexible routine for importing trial lists (of the kind generated by the generateTrials function) into a list of dictionaries, keyed by column name.

# ```python
# def importTrials(trialsFilename, colNames=None, separator='\t'):
#     trialsFile = open(trialsFilename, 'rb')
#  
#     if colNames is None:
#         # Assume the first row contains the column names
#         colNames = trialsFile.next().rstrip().split(separator)
#     trialsList = []
#     for trialStr in trialsFile:
#         trialList = trialStr.rstrip().split(separator)
#         assert len(trialList) == len(colNames)
#         trialDict = dict(zip(colNames, trialList))
#         trialsList.append(trialDict)
#     return trialsList
# ```
# 
# You can use it like so:
# 
# ```python
# trialList = importTrials('trialList.txt')
# for curTrial in trialList:
#     curTrial[colName] #to access a particular value (where colName is something like 'pictureType')
# ```
# 
# *Note: this functionality is actually built into PsychoPy using the
# importConditions function (see
# [here](http://www.psychopy.org/api/data.html#psychopy.data.importConditions))*
# 

# ## A function for grabbing screenshots
# 
# When executed, the function will write a png file containing the stuff
# currently shown on the screen. It will default to using 'win' as the
# variable for your psychopy window. If that is not what you've called
# it, you must pass it to the function explicitly. You also need to pass
# in the name of the file to which you want to write.
# 
# ```python
# def grabScreenshot(fileName, win):
#     """Outputs the current contents of the screen to fileName.png"""
#     win.getMovieFrame()
#     fileName=str(fileName)+'.png'
#     win.saveMovieFrames(fileName)
#     win.movieFrames=[]
# ```

# ## Popping up a web-based survey from within your python script
# 
# The simplest way to pop-up a web-page from your script is to use the
# webbrowser package:
# 
# ```python
# import webbrowser as web
# surveyURL = 'http://' #full URL goes here
# web.open(surveyURL) #put this line at whatever point you want to open up the webpage
# ```
# 
# It is often useful to pre-fill the survey with some information such as
# the subject code. Doing so will eliminate mismatches between the
# subject\'s code between the data and the survey. The easiest way to do
# this is to pass in the relevant info as part of the URL.
# 
# ### Google form
# 
# First, get the question codes to the questions you want to prefill by
# [following the instructions here](https://support.google.com/docs/answer/160000?hl=en).
# 
# Then, add the question codes to the survey URL, like so:
# 
# ```python
# surveyURL = 'https://docs.google.com/forms/d/1rg_sf55XnPOtv7ad4ESuxUpso1X5c_SvkbCL2B6hRzo/viewform'
# surveyURL += '?entry.900342216=%s&entry.142747125=%s' % (runTimeVars['subjCode'], runTimeVars['room'])
# web.open(surveyURL)
# ```
# 
# ![prefilled google form](images/Example_of_prefilled_google_form.png)
# 
# ### Qualtrics forms
# 
# The same logic applies to qualtrics forms except instead of pre-filling
# a question, you would include the subject-code, etc, as part of an
# embedded field. [See here for how to set embedded fields in
# qualtrics](http://www.qualtrics.com/university/researchsuite/advanced-building/survey-flow/embedded-data/).
# 

# ## Using a webcam in psychopy
# 
# This is tested to work with Mac's iSight camera and should work on
# integrated PC cameras. Not sure if it will work with external USB
# cameras. Requires the CV package which can be installed through the
# Anaconda package manager.

# ```python
# from psychopy import visual, event, core
# import Image, time, pylab, cv, numpy
# 
# win = visual.Window([800,600], monitor='testMonitor', color="black")
# 
# capture = cv.CaptureFromCAM(0)
# myStim = visual.ImageStim(win=win,image=None,flipHoriz=True)
# ori=0
# screenCapNum=0
# flipHoriz=0
# while True:
#     img = cv.QueryFrame(capture)
#     pi = Image.fromstring("RGB", cv.GetSize(img), img.tostring(), "raw", "BGR", 0, 1)
#     myStim.setImage(pi)
#     if event.getKeys('r'):
#         ori = (ori+180) % 360
#     if event.getKeys('f'):
#         flipHoriz = (flipHoriz+1) % 2
#     if event.getKeys('g'):
#         cv.SaveImage("grab_"+str(screenCapNum)+".jpg", img)
#         screenCapNum+=1
#     myStim.setOri(ori)
#     myStim.flipHoriz = bool(flipHoriz)
#     myStim.draw()
#     win.flip()
#     if event.getKeys('q'):
#         break
# ```
