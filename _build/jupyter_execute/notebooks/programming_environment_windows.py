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
# ## Install Visual Studio Code
# 
# Visual Studio Code is a very powerful and user-friendly code editor which we will use in this class to edit python/jupyter notebook scripts. Download Visual Studio Code [here](https://code.visualstudio.com) and install it.
# 
# Once installed, open up VS code and select File -> New Text File. At the top of the script, click select a language and select `python`. VS code will prompt you to install the Python extension. Once that is installed. Go back to your file and press `Ctrl + Shift + P`, and type in `Python: Select Interpreter`. Select the `psych750` python environment you created earlier. 
# 
# 
# ### Create a shortcut to Visual Studio code
# 
# It is very useful to be able to quickly access your editor from the shell.
# 
# ...

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
# Lastly, you will want to download and install [CDMer](https://github.com/cmderdev/cmder/releases/). CMDer implements a mini BASH shell on your Windows machine and we'll use it to run various shell commands to give you experience with working in a shell. 
# 
# Extract all the files to your preferred location and run the `cmder.exe` software. Create a shortcut for it so you can access it easily.
# 
# ```{warning}
# CMDer developers recommend NOT extracting the files into C:\Program Files
# ```
