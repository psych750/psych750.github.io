#!/usr/bin/env python
# coding: utf-8

# # Week by week schedule
# 
# Here's the schedule so far. The **In class** sections list the things we'll be doing in class that week. **At home** sections tell you what you should do at home *before* that week's class. For example, you should complete Exercise 1 at home prior to the Week 2 class.  
# 
# This schedule is subject to update. I will be staying ahead of you by at least 2 weeks, meaning if you want to get an early start on the next 1 or 2 assignments, you can do it without worrying that something will change while you are working on it. If there an error, I will correct it and alert the class through Slack.
# 

# 
# ## Prior to first class
# 
# - Sign up for the class Slack group. The link was sent to your @wisc email.
# 
# - Follow [“Download and Install” instructions](https://psych750.github.io/index.html) from the class site.
# 
# - If you’ve never used a Linux shell (or Mac terminal), watch [this video](https://www.youtube.com/watch?v=oxuRxtrO2Ag). Even if you've used a terminal before, go through this [basic linux commands notebook](https://psych750.github.io/notebooks/Shell_reference.html) as a refresher.
# 
# - Sign up for Github if you don’t already have an account (make sure you accept the invite to the class github site). We will be using the very basic capabilities of git: cloning, committing, checking out, and pushing.
# 
#      - If you’ve never used git and github, I recommend walking through two tutorials: [This one](https://githowto.com/setup) focuses on working with git locally. [This one](https://medium.com/@george.seif94/a-full-tutorial-on-how-to-use-github-88466bac7d42) describes pushing and pulling from remote repositories. Confused about the difference between git and github? See [here](https://www.geeksforgeeks.org/difference-between-git-and-github/). This [video walkthrough](https://www.youtube.com/watch?v=8JJ101D3knE) is also very nice.
# 
# - If you’re shaky on what a computer file is, how files are stored, how your operting system knows that sound.wav is a sound file and sound.txt is a text file, [watch this short video](https://www.youtube.com/watch?v=KN8YgJnShPM).
# 
# - Lastly, please look through the [very basics of Python notebook](https://psych750.github.io/notebooks/python_basics.html) to get you ready for the first class. If you don't understand something in that notebook, don't worry about it, but come prepared to ask questions.
# 
# 

# ## Week 1 (Sept 8): Getting oriented
# ### In class
# 
# 1. What do we do when we program?
# 1. How to run Python scripts.
# 1. Intro to Python and PsychoPy
# 1. Show a shape, make it do something, accept a response
# 1. An exercise in algorithmic thinking

# ## Week 2 (Sept 15): Programming basics
# 
# ### At home
# 1. Submit test assignment by Friday (Sept 9) at 9pm.
# 1. Read [Think Python Sections](https://greenteapress.com/wp/think-python-2e/) 1.1-1.8
# 1. Go through the **first three self study guides** on the class site (see the navigation pane on the left)
# 1. Read/skim [Think Python](https://greenteapress.com/wp/think-python-2e/) Sections 5.1-5.7, 7.1-7.8, 8.1-8.12, and 10.1-10.9
# 1. Finish Exercise 1 and push it to your github classroom repository
# 1. Sort out any remaining installation/environment issues. Work on customizing your coding environment
# 
# ### In class:
# 1. Code review of Exercise 1
#     - Special attention to variable names!!
# 2. Our first experiment! A Stroop task.
# 3. Reading and writing files
# 4. Begin Exercise 2
# 

# ## Week 3 (Sept 22)
# 
# ### At home
# 1. Go through **and understand** Review of Fundamentals A
# 2. Go through the *Dictionaries* and *Intro to functions* self-study guides.
# 3. Read about [reading and writing files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
# 4. Go through the *File Reading and Writing notebook* to test your understanding of basic file operations
# 5. Read through [writing readable code](https://testdriven.io/blog/clean-code-python/)
# 6. Finish Exercise 2 while heeding the advice in the previous step.
# ```{tip}
# You are encouraged to use the [Linting feature](https://code.visualstudio.com/docs/python/linting) of Visual Studio Code (I recommend pycodestyle) to help you write code that adheres to Python stylistic standards
# ```
# 
# ### In class
# 1. Exercise 2 Code Review
# 2. More about functions
# 3. Randomization and iteration exercise
# 4. Creating simple trial files
# 5. Extending Exercise 3 with out of the box speech recognition(!)
# 

# ## Week 4 (Sept 29)
# 
# ### At home
# 1. Go through the *List Comprehension* and *Randomization* self-study guides
# 1. Read about [Namespaces and variable scope](http://sebastianraschka.com/Articles/2014_python_scope_and_namespaces.html)
# 1. Complete Exercise 3
# 
# ### In class
# 1. Exercise 3 Code Review
#     1. Emphasis on refactoring using functions and modular code
# 2. Randomization and iteration exercises
# 3. Begin Exercise 4 - a Posner cueing task
# 

# <!-- 
# Week 3 (Sept 22): File access; basic randomization
# 
# 1. Watch [random number generators](https://www.youtube.com/watch?v=_tN2ev3hO14) and read through the [random module](https://docs.python.org/2/library/random.html) documentation.
# 
# 
#  At home: Finish and submit the names exercise. 
# 
# Week 4 (Sept 29): Dictionaries, namespaces, and readable code.
# 
#  At home: Finish Exercise 3, Dictionaries study guide, [Variable
#  scope](http://sebastianraschka.com/Articles/2014_python_scope_and_namespaces.html),
#  
# 
#  In class: Modularizing with functions, debugging, practice writing
#  more readable code, Coding a perceptual grouping task. Capturing
#  [mouse clicks](http://www.psychopy.org/api/event.html).
# 
# Week 5 (Oct 6): Randomization 2: seeds, blocks, combinations and
# permutations
# 
#  At home: [Trial generation
#  notebooks](http://sapir.psych.wisc.edu/programming_for_psychologists/notebooks/trial_generation.html),
#  [Itertools
#  documentation](https://docs.python.org/2/library/itertools.html)
# 
#  In class: Practice with more complex trial generation
# 
# Week 6 (Oct 13): Manipulating files, list comprehension
# 
#  At home: Go through Exercise 5b solution; run yourself; upload data to
#  dropbox
# 
#  In class: Auto loading external stimuli with glob. List comprehension
#  exercises. Project 1 planning
# 
# Week 7 (Oct 20). Numerical simulations; and more complex trial
# generation
# 
#  At home: Monty Python and Birthday Paradox (Exercise 6).
# 
#  In class: Go over Exercise 6; Finish trial generation for Proj 1.
# 
# Week 8 (Oct 27): Working through the hard parts of the projects.
# 
#  At home: Working on projects.
# 
#  In class: Working on projects; discussing problems
# 
# Week 9 (Nov 3): Staircasing, Designing Interactive experiments
# 
#  At home: Finish project 1; collect some data
# 
#  In class: Going over project. Intro to staircasing. Interactive
#  studies:
#  [tilt-illusion](http://sapir.psych.wisc.edu/programming_for_psychologists/notebooks/Exercise8-orientation.html),
#  [face-morph](http://sapir.psych.wisc.edu/programming_for_psychologists/notebooks/Exercise9-faceMorph.html),
#  [image-drag](http://sapir.psych.wisc.edu/programming_for_psychologists/notebooks/Exercise10-imageDrag.html).
# 
# Week 10 (Nov 10): Object oriented programming basics
# 
#  At home: Finish
#  [image-drag](http://sapir.psych.wisc.edu/programming_for_psychologists/notebooks/Exercise10-imageDrag.html)
#  (Exercise 10); [OOP
#  Tutorial](http://sapir.psych.wisc.edu/programming_for_psychologists/notebooks/classes.html);
#  [Review of Fundamentals
#  B](http://sapir.psych.wisc.edu/programming_for_psychologists/notebooks/review_of_fundamentals_b.html)
# 
#  In class: Implementing a finite state automaton for an
#  artificial-grammar learning task (Exercise 11)
# 
# Week 11 (Nov 17): Data Wrangling
# 
#  At home: Introduction to the tidyverse
# 
#  In class: \_\_\_\_
# 
# Week 12 (Dec 1): \_\_\_\_
# 
#  At home: Finish running mTurk HIT. Clone [this PANDAS tutorial
#  repository](https://github.com/jvns/pandas-cookbook) and go through
#  Chapters 1-3 using Jupyter Notebooks. Finally, look through the
#  [ImageMagick
#  Reference](http://sapir.psych.wisc.edu/programming_for_psychologists/notebooks/ImageMagick.html)
# 
#  In class: Data wrangling in R
# 
# Week 13 (Dec 8): Web scraping, using APIs
# 
#  At home: [Lynda webscraping
#  tutorial](https://www.lynda.com/Python-tutorials/Introduction-Beautiful-Soup/520233/601985-4.html);
#  [Tweepy API](http://docs.tweepy.org/en/v3.5.0/getting_started.html);
#  Exercise TBA
# 
#  In class: Using regular expressions in real life; Webscraping
#  exercise; Real-time sentiment analysis of tweets
# 
# Week 14 (May 3): Project presentations
# 
#  At home: Collect some data for Project 2
# 
#  In class: Project presentations (include some data) -->

# <!--
# # Week 5 (Oct 6): Randomization 2: seeds, blocks, combinations and
# # permutations
# # 
# #  At home: [Trial generation
# #  notebooks](http://sapir.psych.wisc.edu/programming_for_psychologists/notebooks/trial_generation.html),
# #  [Itertools
# #  documentation](https://docs.python.org/2/library/itertools.html)
# # 
# #  In class: Practice with more complex trial generation
# # 
# # Week 6 (Oct 13): Manipulating files, list comprehension
# # 
# #  At home: Go through Exercise 5b solution; run yourself; upload data to
# #  dropbox
# # 
# #  In class: Auto loading external stimuli with glob. List comprehension
# #  exercises. Project 1 planning
# # 
# # Week 7 (Oct 20). Numerical simulations; and more complex trial
# # generation
# # 
# #  At home: Monty Python and Birthday Paradox (Exercise 6).
# # 
# #  In class: Go over Exercise 6; Finish trial generation for Proj 1.
# # 
# # Week 8 (Oct 27): Working through the hard parts of the projects.
# # 
# #  At home: Working on projects.
# # 
# #  In class: Working on projects; discussing problems
# # 
# # Week 9 (Nov 3): Staircasing, Designing Interactive experiments
# # 
# #  At home: Finish project 1; collect some data
# # 
# #  In class: Going over project. Intro to staircasing. Interactive
# #  studies:
# #  [tilt-illusion](http://sapir.psych.wisc.edu/programming_for_psychologists/notebooks/Exercise8-orientation.html),
# #  [face-morph](http://sapir.psych.wisc.edu/programming_for_psychologists/notebooks/Exercise9-faceMorph.html),
# #  [image-drag](http://sapir.psych.wisc.edu/programming_for_psychologists/notebooks/Exercise10-imageDrag.html).
# # 
# # Week 10 (Nov 10): Object oriented programming basics
# # 
# #  At home: Finish
# #  [image-drag](http://sapir.psych.wisc.edu/programming_for_psychologists/notebooks/Exercise10-imageDrag.html)
# #  (Exercise 10); [OOP
# #  Tutorial](http://sapir.psych.wisc.edu/programming_for_psychologists/notebooks/classes.html);
# #  [Review of Fundamentals
# #  B](http://sapir.psych.wisc.edu/programming_for_psychologists/notebooks/review_of_fundamentals_b.html)
# # 
# #  In class: Implementing a finite state automaton for an
# #  artificial-grammar learning task (Exercise 11)
# # 
# # Week 11 (Nov 17): Data Wrangling
# # 
# #  At home: Introduction to the tidyverse
# # 
# #  In class: \_\_\_\_
# # 
# # Week 12 (Dec 1): \_\_\_\_
# # 
# #  At home: Finish running mTurk HIT. Clone [this PANDAS tutorial
# #  repository](https://github.com/jvns/pandas-cookbook) and go through
# #  Chapters 1-3 using Jupyter Notebooks. Finally, look through the
# #  [ImageMagick
# #  Reference](http://sapir.psych.wisc.edu/programming_for_psychologists/notebooks/ImageMagick.html)
# # 
# #  In class: Data wrangling in R
# # 
# # Week 13 (Dec 8): Web scraping, using APIs
# # 
# #  At home: [Lynda webscraping
# #  tutorial](https://www.lynda.com/Python-tutorials/Introduction-Beautiful-Soup/520233/601985-4.html);
# #  [Tweepy API](http://docs.tweepy.org/en/v3.5.0/getting_started.html);
# #  Exercise TBA
# # 
# #  In class: Using regular expressions in real life; Webscraping
# #  exercise; Real-time sentiment analysis of tweets
# # 
# # Week 14 (May 3): Project presentations
# # 
# #  At home: Collect some data for Project 2
# # 
# #  In class: Project presentations (include some data) -->
