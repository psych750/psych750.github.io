#!/usr/bin/env python
# coding: utf-8

# # Programming Environment for Windows
# 
# Python is not installed by default on Windows. We will be using the Anaconda environment which allows for easy installation of packages into a virtual environment which helps to eliminate software conflicts. 

# # Install git
# [Download and install](https://gitforwindows.org) the latest version of `git` 
# 
# Test it by typing 
# `git --version` 
# at the command prompt.
# 
# 
# # Install the Anaconda Distribution of Python
# 
# 
# * Download and Install the **Python 3.8 64 bit** [Miniconda installer](https://conda.io/miniconda.html). If you are asked whether you want the installer to prepend Anaconda to your PATH, respond ***yes***.
# 
# 
# * Next let's create a virtual environment for this course. At the command prompt type
# 
# ```bash
# conda create -n psych750 python=3.8 pip
# ```
# 
# Once it's created, you can activate it by typing
# ```
# conda activate psych750
# ```
# 
# 
# ## Test the Anaconda Python install
# 
# Activate your environment using `conda activate psych750` and then type `python` to start the Python interpreter
# ```bash
# $ python 
# Python 3.8.13 (default, Mar 28 2022, 06:16:26)
# [Clang 12.0.0 ] :: Anaconda, Inc. on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# ```
# 
# ## Installing the necessary Python packages
# * Now let's install the packages we'll need. Paste in the lines below, one at at a time, into your terminal (make sure your new environment is activated first). Wait for everything to install before proceeding to the next line.
# 
# ```bash
# conda install jupyter jupyterlab
# conda install pyaudio
# pip install psychopy
# ```
# 
# ```{warning}
# If you run into any install errors, please make note of the precise errors and post them to the #installation_problems Slack channel.
# ```
# 
# ## Test PsychoPy
# ====
# * Now let's test that `PsychoPy` installed correctly. Start the python interpreter and then import the psychopy package:
# 
# ```python
# >>> import psychopy
# >>> psychopy.__version__
# '2022.2.2'
# ```
# 
# If you see the verison number, the PsychoPy library probably installed correctly. Let's do some more tests
# 
# * Let's test if PsychoPy can successfully open a new window.
# 
# ```python
# >>> from psychopy import visual
# >>> visual.Window((400,400),color="green")
# ```
# 
# When you hit enter after the second line, you should see a small green window appear. There may me some warnings displayed... You can safely ignore them.
# 
# ```{note}
# You won't be able to close the window like a regular window.
# Click on the terminal and enter `exit()` to quit the session and close the window.
# ```
# 
# * Finally let's test whether Psychopy can open pop-up boxes without issues
# 
# ```python
# >>> from psychopy import visual, gui
# ```
# 
# Now copy/paste this little function:
# ```python
# def popupError(text):
#     errorDlg = gui.Dlg(title="Error", pos=(400,400))
#     errorDlg.addText('Error: '+text, color='Red')
#     errorDlg.show()
# ```
# 
# And lastly, execute it like so:
# 
# ```python
# popupError('Pop up test!')
# ```
# 
# If you saw a little pop-up window, all's good. If it doesn't immediately appear, check that it's not behind your active window.
# 
# ## Configure a few Psychopy settings
# 
# While we're here, let's also make sure the Psychopy settings are in order. Enter these lines in the python interpreter:
# ```python
# import psychopy
# psychopy.prefs.general['units']='pix'
# psychopy.prefs.hardware['audioLib'] = ['PTB', 'pyo','pygame']
# psychopy.prefs.saveUserPrefs()
# ```
# 

# # Installing Sublime Text
# 
# 
# Sublime Text is a popular text editor with a very large collection of plugins and themes that allow you to make it anything you want it to be. It is not free, but has a generous trial-use policy. If you like it, please purchase a license.
# 
# To install Sublime Text, go to the [Downloads](http://www.sublimetext.com/download) page, and download/install the Windows version. 
# 
# To use it efficiently, you'll want to learn some [keyboard shortcuts](http://sweetme.at/2013/08/08/sublime-text-keyboard-shortcuts/). 
# 
# There are lots of handy packages for Sublime Text. To install them, you'll want to first install [Package Control](https://packagecontrol.io/installation) which allows you to browse and install packages directly from within Sublime Text. Some useful ones are [Origami](https://packagecontrol.io/packages/Origami), [SublimeREPL](https://packagecontrol.io/packages/SublimeREPL), [AdvancedCSV](https://packagecontrol.io/packages/Advanced%20CSV), and [Terminal](https://packagecontrol.io/packages/Terminal).
# 
# ## Create a shortcut to Sublime Text
# 
# * It's very handy to be able to quickly open text files with Sublime Text from the terminal. The easiest way to do this is with a `doskey`.
# 
# From the command prompt enter the following command:
# 
# ```bash
# doskey s="C:\Program Files\Sublime Text\subl.exe"
# ```
# 
# ```{note}
# Make sure to change the directory to where you installed Sublime Text!
# ```
# 
# Now you should be able to open any file using Sublime Text by using `s`. For example, `s my_file.txt` should open `my_file.txt` (or create it if it doesn't exist). 
# 
# ```{warning}
# In Windows, directory separators are backslashes. Make sure not to use the wrong one!
# ```

# # Install R & RStudio Desktop
# 
# Next install R and RSudio Desktop by following the instructions [here](https://www.rstudio.com/products/rstudio/download/#download). Make sure to install Rtools as well when you download R.
# 
# ## Install a few R packages
# 
# Once R and RStudio are installed, make sure you can open up RStudio successfully and then install these packages (we may include some additional ones later).
# 
# At the RStudio prompt, type
# 
# ```r
# install.packages(c("tidyverse", "ggplot2", "lme4", "psych", "psychTools"))
# ```
# 

# # Download CMDer
# 
# Lastly, you will want to download and install [CDMer](https://github.com/cmderdev/cmder/releases/) on your computer to run BASH commands.
# 
# Extract all the files to your preferred location and run the `cmder.exe` software. 
# 
# ```{warning}
# CMDer developers recommend NOT extracting the files into C:\Program Files
# ```
