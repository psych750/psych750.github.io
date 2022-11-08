#!/usr/bin/env python
# coding: utf-8

# # Exercise 9 - Object oriented programming practice
# 
# Accept the exercise (link coming soon)
# 
# 

# 
# ## Part 1: Make it red!
# 
# Add a method `turn_it_red()` such that when you click on a moving circle, it turns red. All the circles should continue moving. There should not be any pauses.
# 

# ## Part 2: Make them stop
# 
# Add a method `make_them_stop()` such that when you click on a moving circle, it keeps moving, but all the other circles stop moving.

# ## Part 3 Make it drop!
# 
# Add a method `make_it_drop()` such that when you click on a moving circle, it drops to the bottom and remains there. The drop should be gradual -- the circle should smoothly descend down. The other circles should keep moving while the one you clicked on is dropping to the ground.
# 
# ```{tip}
# Decrease the y position gradually until the bottom of the screen.
# ```
# 

# ## Part 4: Make it drop.... more naturally
# 
# When things drop here on Earth, they don't fall at a constant velocity. They accelerate because, you know... gravity! Extend your `make_it_drop()` method to accept a parameter `accelerate`. Its default value is False. When set to True, the circle should drop as in part 3, but it should accelerate downward according to:
# 
# ```python
# h = .5*g*t**2
# ```
# :::{note}
# In Python, as in many other programming languages `**` is exponentiation, i.e, `3**3=27`
# :::
# 
# If you remember your high school physics,`g` is the gravitational constant which is 9.8 m/s/s. In our case, the units can be pixels, so 9.8 pixels per second per second.
# 
# `h` is the distance travelled (in our case, the distance from the circle's starting position, and `t`, is, of course, time. Use seconds for time. Remember that if your laptop is refreshing at 60Hz, each frame lasts ~17 msecs, i.e., .017 seconds. Refresh the position of the circle on each frame so that it's nice and smooth. The other circles should keep moving as normal when the circle you clicked on drops down. 
# 
# 

# ## Bonus 
# 
# Coming soon.
