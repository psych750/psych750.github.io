#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc" style="margin-top: 1em;"><ul class="toc-item"><li><span><a href="#Programming-Environment:-Windows-10" data-toc-modified-id="Programming-Environment:-Windows-10-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Programming Environment: Windows 10</a></span></li><li><span><a href="#Installing-Cmder" data-toc-modified-id="Installing-Cmder-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Installing Cmder</a></span></li><li><span><a href="#Installing-the-Anaconda-Distribution-of-Python" data-toc-modified-id="Installing-the-Anaconda-Distribution-of-Python-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Installing the Anaconda Distribution of Python</a></span><ul class="toc-item"><li><span><a href="#Installing-the-packages" data-toc-modified-id="Installing-the-packages-3.1"><span class="toc-item-num">3.1&nbsp;&nbsp;</span>Installing the packages</a></span></li><li><span><a href="#Test-Anaconda-Python-Install" data-toc-modified-id="Test-Anaconda-Python-Install-3.2"><span class="toc-item-num">3.2&nbsp;&nbsp;</span>Test Anaconda Python Install</a></span></li><li><span><a href="#Test-PsychoPy" data-toc-modified-id="Test-PsychoPy-3.3"><span class="toc-item-num">3.3&nbsp;&nbsp;</span>Test PsychoPy</a></span></li><li><span><a href="#Test-spyder" data-toc-modified-id="Test-spyder-3.4"><span class="toc-item-num">3.4&nbsp;&nbsp;</span>Test spyder</a></span></li></ul></li><li><span><a href="#Installing-pyo" data-toc-modified-id="Installing-pyo-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Installing pyo</a></span><ul class="toc-item"><li><span><a href="#Test-pyo" data-toc-modified-id="Test-pyo-4.1"><span class="toc-item-num">4.1&nbsp;&nbsp;</span>Test pyo</a></span></li></ul></li><li><span><a href="#Installing-Sublime-Text" data-toc-modified-id="Installing-Sublime-Text-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Installing Sublime Text</a></span><ul class="toc-item"><li><span><a href="#Create-a-shortcut-to-Sublime-Text" data-toc-modified-id="Create-a-shortcut-to-Sublime-Text-5.1"><span class="toc-item-num">5.1&nbsp;&nbsp;</span>Create a shortcut to Sublime Text</a></span></li></ul></li><li><span><a href="#Optional:-Creating-a-virtual-environment" data-toc-modified-id="Optional:-Creating-a-virtual-environment-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>Optional: Creating a virtual environment</a></span></li></ul></div>

# Programming Environment: Windows 10
# ===
# We will be using the Anaconda distribution of Python (2.7). This section will guide you on installing Anaconda, PsychoPy, pyo, and Sublime Text. We will be using the Anaconda environment which is bundled with lots of packages for scientific computing, allows you to more easily install packages and create virtual environments, and comes with a handy IDE (Integrated Development Environment) called **Spyder**. 

# Installing Cmder
# ===
# 
# We'll be using various shell commands in the class. Windows terminal (`cmd`) is pretty crummy and although there is a Linux shell now available for Windows 10, the shell is not integrated with the Windows system making its use very inconvenient. As a solution we'll use `Cmder`.
# 
# * [Download Cmder](http://cmder.net/) -- full version -- and uncompress it into wherever you want to run it from (probably not your Downloads folder). 
# 
# Open it by double clicking on Cmder.exe. Pin it to the taskbar. Now start an Administrator shell like so:
# ![title](images/cmder_integrate.png)
# 
# Navigate to the directory containing Cmder using `cd`. You can verify by typing `ls` and making sure you see Cmder.exe in the list.
# 
# To integrate Cmder with Windows explorer type `.\cmder.exe /REGISTER ALL` in the Cmder prompt
# 
# <div class="alert alert-block alert-info">
# If you are getting errors make sure you are inside the directory containing Cmder.exe. Also make sure you are typing the commands exactly as they appear above. Spaces matter.
# </div>
# 
# 
# Now you can right click on any directory in Windows explorer and choose to open the contents with Cmder.
# 

# Installing the Anaconda Distribution of Python
# ===
# 
# * Download and Install the **Python 2.7 32 bit** [Miniconda installer](https://conda.io/miniconda.html). During installation you will be prompted to add Anaconda to the PATH. Select to do that (even though it will tell you it's not the recommended option).
# 
# For simplicity, we'll install all the Python packages we'll need into the `root` environment of Anaconda. If you want a separate environment for `PsychoPy`, see [Creating a virtual environment](#Optional:-Creating-a-virtual-environment). If you don't know what virtual environments are and want to learn, see [here](https://conda.io/docs/user-guide/tasks/manage-environments.html)
# 
# ## Installing the packages
# * Once Miniconda is installed, go to `Cmder` and paste in the following commands, press `enter` and wait for everything to install:
# 
# ``` bash
# conda install spyder jupyter psutil
# pip install numpy scipy matplotlib pandas pyopengl pyglet==1.2.4 pillow moviepy lxml 
# pip install openpyxl configobj future json_tricks wxpython pypiwin32
# pip install psychopy
# ```
# 
# <div class="alert alert-block alert-info">
# If you have install errors, note them and let me know via the #installation_problems Slack sub-channel.
# </div>
# 
# ## Test Anaconda Python Install
# ====
# * In Cmder, enter `python`, now instead of the Mac-bundled Python, you should see something like:
# ```bash
# $ python 
# Python 2.7.14 |Anaconda, Inc.| (default, Nov  8 2017, 13:40:13) [MSC v.1500 32 bit (Intel)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# ```
# 
# ## Test PsychoPy
# ====
# * Now let's test that `PsychoPy` installed correctly. At the python prompt type:
# 
# ```python
# >>> import psychopy
# >>> psychopy.__version__
# '1.85.3'
# ```
# 
# If you see this, you know that the PsychoPy library installed correctly. 
# 
# * Let's test that PsychoPy can successfully open a new window
# 
# ```python
# >>>from psychopy import visual
# >>>visual.Window((400,400),color="green")
# ```
# 
# When you hit enter after the second line, you should see a small green window. 
# <div class="alert alert-block alert-info">
# Click on Cmder and enter exit() to quit (you won't be able to close the window like a regular Windows window)
# </div>
# 
# 
# 
# ## Test spyder
# ===
# * Now let's test the spyder graphical IDE. In CMDer type `spyder`. You should see something like this:
# ![title](images/spyder.png)
# 
# If that looks a like RStudio, that's because all these IDEs are descended from a common ancestor. 
# 

# Installing pyo
# ===
# 
# * The last thing we need to do is install the `pyo` package which `PsychoPy` uses to play audio files with low(er) latencies. There are other alternatives for playing sounds, but in my testing, `pyo` consistently produces more robust performance.
# 
# Download and install PYO from [here](http://ajaxsoundstudio.com/downloads/pyo_0.8.0_py2.7_setup.exe). 
# 
# ## Test pyo
# ===
# * In Cmder, enter `python`, then:
# ``` python
#     >>>import pyo
#     pyo version 0.8.0 (uses single precision)
# ```
# 
# If you see this, all is good.
# 

# Installing Sublime Text
# ===
# Sublime Text is a popular text editor with a very large collection of plugins and themes that allow you to make it anything you want it to be. It is not free, but has a generous trial-use policy. If you like it, please purchase a license.
# 
# To install Sublime Text, go to the [Downloads](http://www.sublimetext.com/3) page, and click on the Windows installer. 
# 
# To use it efficiently, you'll want to learn some [keyboard shortcuts](https://www.shortcutfoo.com/app/dojos/sublime-text-3-win/cheatsheet). 
# 
# There are lots of handy packages for Sublime Text. To install them, you'll want to first install [Package Control](https://packagecontrol.io/installation) which allows you to browse and install packages directly from within Sublime Text. Some especially handy ones are [Origami](https://packagecontrol.io/packages/Origami), [SublimeREPL](https://packagecontrol.io/packages/SublimeREPL), [AdvancedCSV](https://packagecontrol.io/packages/Advanced%20CSV), and [Terminal](https://packagecontrol.io/packages/Terminal).
# 
# ## Create a shortcut to Sublime Text
# 
# * It's very handy to be able to open a file with sublime text from the terminal. The easiest way to do this is with an `alias`. 
# 
# Using Sublime Text, open the `user-aliases.cmd` file inside `cmder\config` (cmder is inside whatever directory you're using it from). 
# 
# Add an alias to Sublime Text by adding the following line into `user-aliases.cmd`.
# 
# ```bash
# s="C:\Program Files\Sublime Text 3\sublime_text.exe" $1  
# ```
# 
# Save the file and restart Cmder. Now you should be able to open any file inside Sublime Text using `s`, e.g., `s my_file.txt` 

# # Optional: Creating a virtual environment
# ===
# 
# If you already have a Anaconda environment that you're happy with, and don't want to mess with, or you want to create a separate Python environment for this class, execute the following two lines at the Terminal ***before*** following the [package installation instructions](#Installing-the-packages):
# 
# ```bash
# conda create -n psychopy pip 
# source activate psychopy
# ```
# 

# [top](#)

# - - -
# [Previous: Programming Environment](http://nbviewer.ipython.org/urls/raw.github.com/ehmatthes/intro_programming/master/notebooks/programming_environment.ipynb) | 
# [Home](http://nbviewer.ipython.org/urls/raw.github.com/ehmatthes/intro_programming/master/notebooks/index.ipynb) | 
# [Next: Hello World](http://nbviewer.ipython.org/urls/raw.github.com/ehmatthes/intro_programming/master/notebooks/hello_world.ipynb)
