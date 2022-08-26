#!/usr/bin/env python
# coding: utf-8

# # Programming Environment for MacOS
# 
# Python is installed by default on Macs, but we will ***not*** be using the standard install. Instead we will be using the Anaconda environment which allows for easy installation of packages into a virtual environment which helps to eliminate software conflicts. 

# ## Install git
# [Download and install](https://sourceforge.net/projects/git-osx-installer/files/) the latest version of `git` 
# 
# Test it by typing 
# `git --version` 
# at the command prompt.
# 
# 

# ## Install the Anaconda Distribution of Python
# 
# ```{attention}
# The instructions are slightly different if you are using an Intel Mac or a newer M1/M2 mac. If you're not sure Click on the Apple icon on the top left corner and select `About this Mac`. If it says Intel XXX, then follow the Intel CPU instructions. If it says Apple M1 or similar, follow the Mac CPU instructions.
# ```
# 
# ### Intel CPU Instructions
# * Download and Install the **Python 3.8 64 bit** [Miniconda installer](https://conda.io/miniconda.html). If you are asked whether you want the installer to prepend Anaconda to your PATH, respond ***yes***.
# 
# 
# ### Mac CPU Instructions
# * Open up your `Finder` and click on `Applications`. Then navigate to `Utilities` folder and right click on the `Terminal` and select Duplicate. Rename the duplicate to `Rosetta-Terminal`. Then right click on the `Rosetta-Terminal` and select `Get Info`. Check the `Open with Rosetta` option.
# 
# * Download and Install the **Python 3.8 64 bit** [Miniconda installer](https://conda.io/miniconda.html). Make sure to select the `macOS Intel x86 64-bit` version. The `pkg` file is more user friendly and installs like any other programs. If you are asked whether you want the installer to prepend Anaconda to your PATH, respond ***yes***.
# 
# * From now on, use the `Rosetta-Terminal` instead of the original `Terminal`.
# 
# 

# 
# 
# ## Create a Virtual Environment
# 
# Next let's create a virtual environment for this course. At the command prompt type
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
# ### Test the Anaconda Python install
# 
# Activate your environment using `conda activate psych750` and then type `python` to start the Python interpreter
# ```bash
# $ python 
# Python 3.8.13 (default, Mar 28 2022, 06:16:26)
# [Clang 12.0.0 ] :: Anaconda, Inc. on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# ```
# 
# Now you can exit out of Python by typing:
# 
# ```bash
# exit()
# ```
# 
# 

# ## Install Homebrew and PortAudio
# 
# Next we need to install Homebrew and run some commands in order to install other packages. Follow the instructions [here](https://brew.sh) to install Homebrew.
# 
# Once Homebrew is installed, run the following command in Terminal:
# ```bash
# brew install portaudio
# ```
# This will install some libraries for doing some speech recognition magic

# 
# ## Installing the necessary Python packages
# Now let's install the packages we'll need. Paste in the lines below, one at at a time, into your terminal (not python interpreter). Make sure your new environment is activated first by using `conda activate`. Wait for everything to install before proceeding to the next line.
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
# ### Test PsychoPy
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
# Start the Python interpreter and type (copy/paste) the following:
# 
# ```python
# >>> from psychopy import visual
# >>> visual.Window((400,400),color="green")
# ```
# 
# When you hit enter after the second line, you should see a small green window appear. There may me some warnings displayed... You can safely ignore them. The window may be covered up by another program if you have a lot of things open, so look around.
# 
# ```{note}
# You won't be able to close the window like a regular Mac window.
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
# 
# 

# 
# ### Configure a few Psychopy settings
# 
# While we're here, let's also make sure the Psychopy settings are in order. Enter these lines in the python interpreter:
# ```python
# import psychopy
# psychopy.prefs.general['units']='pix'
# psychopy.prefs.hardware['audioLib'] = ['PTB', 'pyo','pygame']
# psychopy.prefs.saveUserPrefs()
# ```

# ## Install Visual Studio Code
# 
# Visual Studio Code is a very powerful and user-friendly code editor which we will use in this class to edit python/jupyter notebook scripts. Download Visual Studio Code [here](https://code.visualstudio.com) and install it.
# 
# Once it's installed, open up VS code and select File -> New Text File. At the top of the script, click select a language and select `python`. VS code will prompt you to install the Python extension. Once that is installed go back to your file and press `Command + Shift + P`, and type in `Python: Select Interpreter`. Select the `psych750` conda Python environment you created earlier. 
# 
# Look over keyboard shortcuts: `Help: Keyboard Shortcut Reference` Try to use them!
# 
# ### Create a shortcut to Visual Studio code
# 
# It is very useful to be able to quickly open up a file in the editor from the shell. You can do this like so:
# 
# Hit  `Command + Shift + P` and type `shell` 
# Press `enter` to `Install Code Command in PATH`
# 
# 
# Test the installation by launching a new terminal window and typing
# ```bash
# code some_file_name.txt
# ```
# 
# where `some_file_name.txt` is the file you want to open. 
# 
# It should open up in visual Studio Code
# 
# If you want to shorten it further, e.g., instead of having to type `code` you want to type `c`, add an `alias` to your shell configuration file (`.bash_profil), like so:
# 
# ```bash
# code ~/.bash_profile
# ```
# 
# Now add the line
# ```bash
# alias c="code"
# ```
# 
# Save the file and restart your shell. You should now be able to open files in Visual Code Studio by typing
# ```bash
# c some_file_name.txt
# ```

# ## Install R & RStudio Desktop
# 
# Next install R and RSudio Desktop by following the instructions [here](https://www.rstudio.com/products/rstudio/download/#download).
# 
# ### Install a few R packages
# 
# Once R and RStudio are installed, make sure you can open up RStudio successfully and then install these packages (we may include some additional ones later).
# 
# At the RStudio prompt, type
# 
# ```r
# install.packages(c("tidyverse", "ggplot2", "lme4", "psych", "psychTools"))
# ```
# 

# ## Adding R to Jupyter Notebook
# 
# It's handy to run R within jupyter notebook so you can have a markdown style document detailing what analyses and results you got. To install R and R kernel in jupyter, simply follow the steps below:
# 
# First you need to activate the psych750 environment in your Terminal:
# 
# ```bash
# conda activate psych750
# ```
# 
# Then enter the following command:
# ```bash
# conda install -c r r-irkernel
# ```
# 
# Once everything is installed, you can test it out by entering `jupyter notebook` in your Terminal window to start a new session. On the top right corner, select `new`, and it will prompt you to choose either the `python3` kernel or the `R` kernel.
# 
# You can also open these notebooks in Visual Studio Code. Open up an .ipynb file in Visual Studio Code, choose R as the Kernel and start running R code! The first time you do this, Visual Studio Code will prompt you to install some add-ons. Just click ok on the recommended extensions and you should be good to go.
