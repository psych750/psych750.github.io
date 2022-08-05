#!/usr/bin/env python
# coding: utf-8

# # Exercise 4: Debugging practice
# 
# ## Practice 1
# Here's some broken code. When fixed, it should display wide and narrow
# rectangles, in random order, and play a bleep sound if you respond 'w'
# for wide or 'n' for narrow, and buzzing sound otherwise. It should
# also output the correctness of the response and the RT to standard
# output (i.e., the python screen). The .wav files it can be downloaded
# [here](http://sapir.psych.wisc.edu/classMaterials/psych711/buzzBleep.zip))

# In[ ]:


import time
import random
from psychopy import visual, core, event,sound
win = visual.Window([800,600],color="blak", units='pix')

rect = visual.Rect(win,fillColor="blue",size=size)
aspect = {'wide':[200,100], 'narrow':[100,200]}
validKeys = {'wide':'w', 'narrow':'n'}

bleep = sound.Sound('sounds/bleep.wav')
buzz = sound.Sound('sounds/buzz.wav')

for curIter in range(20)
	win.flip()
	core.wait(.5)
	curAspect  = random.choice(aspect.values())
	rect.setSize(aspect[curAspect])
	rect.draw()
	win.flip()
	timer = core.Timer()
	resp = event.waitKeys(keyList=validKeys.values())
	if resp==validKeys[aspect]:
		print 1, timer.getTime()
		bleep.play()
	else:
		print 0, timer.getTime()
		buzz.play()


# ## Practice 2
# Here's some more broken code. This program should prompt you with an expression category (Happy, Sad, etc.) and then show a face. If you categorize the face correctly, you should see a green CORRECT. Otherwise a red ERROR. The program should present you with 40 trials. Download the faces [here](http://sapir.psych.wisc.edu/classMaterials/psych711/faces.zip) and place them inside a `faces` folder in the same directory as the script below.

# In[1]:


import sys
from psychopy import visual, core, event

categories = {'Happy'='F', 'Angry'='W', 'Sad'='T'}
actors = ['001m', '001w', '002m', '002w', '003m', '003w', '004m', '004w', '005m', '005w']
suffix = '_90_60.jpg'
responseMapping = {'up':1,'down':0}
numTrials = 40


def randomButNot(l,toExclude):
	chosen = random.choice(l)
	while toExclude in chosen:
		chosen = random.choice(l)
	return chosen

def generateTrials(numTrials):
	trials=[]
	propMatch  = .6
	for i in range(numTrials):
		emotionPrompt = random.choice(categories.keys())
		shownActor = random.choice(actors)
		isMatch = int(random.random()<propMatch)

		if isMatch:
			shownCategory = emotionPrompt
			targetFaceImage = shownActor+categories[emotionPrompt]+suffix
		else:
			shownCategory = randomButNot(categories.keys(), emotionPrompt)
			targetFaceImage = shownActor+categories[shownCategory]+suffix

		trials.append({	'isMatch':isMatch,
						'emotionPrompt':emotionPrompt,
						'shownActor':shownActor,
						'shownCategory':shownCategory,
						'targetFaceImage':targetFaceImage
						})

		return trials

trials = generateTrials(numTrials)

win = visual.Window([800,600],color="black", units='pix')
prompt = visual.TextStim(win=win,text='',color="white",height=60)
correctFeedback = visual.TextStim(win=win,text='CORRECT',color="green",height=60)
incorrectFeedback = visual.TextStim(win=win,text='ERROR',color="red",height=60)
pic = visual.ImageStim(win=win, mask=None,interpolate=True)

for curTrial in trials:
	win.flip()
	core.wait(25)
	prompt.setText(curTrial['emotionPrompt']+'?')
	prompt.draw()
	win.flip()
	core.wait(.5)

	win.flip()
	core.wait(.1)
	pic.setImage('faces/'+curTrial['targetFaceImage'])
	pic.draw()
	win.flip()
	response = event.waitKeys(keyList=responseMapping.values())[0]
	if response==responseMapping[curTrial['isMatch']]:
		correctFeedback.draw()
	else:
		correctFeedback.draw()
	win.flip()
	core.wait(.5)

