#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc" style="margin-top: 1em;"><ul class="toc-item"><li><span><a href="#Classes" data-toc-modified-id="Classes-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Classes</a></span></li><li><span><a href="#What-are-classes?" data-toc-modified-id="What-are-classes?-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>What are classes?</a></span><ul class="toc-item"><li><span><a href="#Classes-in-Python-2.7" data-toc-modified-id="Classes-in-Python-2.7-2.1"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>Classes in Python 2.7</a></span></li></ul></li><li><span><a href="#Object-Oriented-terminology" data-toc-modified-id="Object-Oriented-terminology-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Object-Oriented terminology</a></span><ul class="toc-item"><li><span><a href="#General-terminology" data-toc-modified-id="General-terminology-3.1"><span class="toc-item-num">3.1&nbsp;&nbsp;</span>General terminology</a></span></li><li><span><a href="#A-closer-look-at-the-Rocket-class" data-toc-modified-id="A-closer-look-at-the-Rocket-class-3.2"><span class="toc-item-num">3.2&nbsp;&nbsp;</span>A closer look at the Rocket class</a></span></li><li><span><a href="#The-__init__()-method" data-toc-modified-id="The-__init__()-method-3.3"><span class="toc-item-num">3.3&nbsp;&nbsp;</span>The __init__() method</a></span></li><li><span><a href="#A-simple-method" data-toc-modified-id="A-simple-method-3.4"><span class="toc-item-num">3.4&nbsp;&nbsp;</span>A simple method</a></span></li><li><span><a href="#Making-multiple-objects-from-a-class" data-toc-modified-id="Making-multiple-objects-from-a-class-3.5"><span class="toc-item-num">3.5&nbsp;&nbsp;</span>Making multiple objects from a class</a></span></li><li><span><a href="#A-quick-check-in" data-toc-modified-id="A-quick-check-in-3.6"><span class="toc-item-num">3.6&nbsp;&nbsp;</span>A quick check-in</a></span></li></ul></li><li><span><a href="#Refining-the-Rocket-class" data-toc-modified-id="Refining-the-Rocket-class-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Refining the Rocket class</a></span><ul class="toc-item"><li><span><a href="#Accepting-parameters-for-the-__init__()-method" data-toc-modified-id="Accepting-parameters-for-the-__init__()-method-4.1"><span class="toc-item-num">4.1&nbsp;&nbsp;</span>Accepting parameters for the __init__() method</a></span></li><li><span><a href="#Accepting-parameters-in-a-method" data-toc-modified-id="Accepting-parameters-in-a-method-4.2"><span class="toc-item-num">4.2&nbsp;&nbsp;</span>Accepting parameters in a method</a></span></li><li><span><a href="#Adding-a-new-method" data-toc-modified-id="Adding-a-new-method-4.3"><span class="toc-item-num">4.3&nbsp;&nbsp;</span>Adding a new method</a></span></li></ul></li><li><span><a href="#Inheritance" data-toc-modified-id="Inheritance-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Inheritance</a></span><ul class="toc-item"><li><span><a href="#The-SpaceShuttle-class" data-toc-modified-id="The-SpaceShuttle-class-5.1"><span class="toc-item-num">5.1&nbsp;&nbsp;</span>The SpaceShuttle class</a></span></li><li><span><a href="#Inheritance-in-Python-2.7" data-toc-modified-id="Inheritance-in-Python-2.7-5.2"><span class="toc-item-num">5.2&nbsp;&nbsp;</span>Inheritance in Python 2.7</a></span></li></ul></li><li><span><a href="#Example-of-using-a-class-in-a-Psychopy-experiment" data-toc-modified-id="Example-of-using-a-class-in-a-Psychopy-experiment-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>Example of using a class in a Psychopy experiment</a></span><ul class="toc-item"><li><span><a href="#A-single-moving-circle" data-toc-modified-id="A-single-moving-circle-6.1"><span class="toc-item-num">6.1&nbsp;&nbsp;</span>A single moving circle</a></span></li></ul></li><li><span><a href="#Modules-and-classes" data-toc-modified-id="Modules-and-classes-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>Modules and classes</a></span><ul class="toc-item"><li><span><a href="#Storing-a-single-class-in-a-module" data-toc-modified-id="Storing-a-single-class-in-a-module-7.1"><span class="toc-item-num">7.1&nbsp;&nbsp;</span>Storing a single class in a module</a></span></li><li><span><a href="#Storing-multiple-classes-in-a-module" data-toc-modified-id="Storing-multiple-classes-in-a-module-7.2"><span class="toc-item-num">7.2&nbsp;&nbsp;</span>Storing multiple classes in a module</a></span></li><li><span><a href="#A-number-of-ways-to-import-modules-and-classes" data-toc-modified-id="A-number-of-ways-to-import-modules-and-classes-7.3"><span class="toc-item-num">7.3&nbsp;&nbsp;</span>A number of ways to import modules and classes</a></span><ul class="toc-item"><li><span><a href="#import-module_name" data-toc-modified-id="import-module_name-7.3.1"><span class="toc-item-num">7.3.1&nbsp;&nbsp;</span>import <em>module_name</em></a></span></li><li><span><a href="#import-module_name-as-local_module_name" data-toc-modified-id="import-module_name-as-local_module_name-7.3.2"><span class="toc-item-num">7.3.2&nbsp;&nbsp;</span>import <em>module_name</em> as <em>local_module_name</em></a></span></li><li><span><a href="#from-module_name-import-*" data-toc-modified-id="from-module_name-import-*-7.3.3"><span class="toc-item-num">7.3.3&nbsp;&nbsp;</span>from <em>module_name</em> import *</a></span></li></ul></li><li><span><a href="#A-module-of-functions" data-toc-modified-id="A-module-of-functions-7.4"><span class="toc-item-num">7.4&nbsp;&nbsp;</span>A module of functions</a></span></li></ul></li></ul></div>

# Classes
# ===
# So far you've learned about Python's core data types: strings, numbers, lists, tuples, and dictionaries. In this section you will learn about the last major data structure, classes. Classes are unlike other data types, in that they are much more flexible. Classes allow you to define the information and behavior that characterize anything you want to model in your program. This notebook is a short introduction to classes. The first part gives soem generic examples. The second part give some examples of using classes in a context of a psych experiment.
# 
# There is a lot of new language that comes into play when you start learning about classes. If you are familiar with object-oriented programming (OOP) from  another language, this will be a quick read about how Python approaches OOP. If you are new to programming in general, there will be a lot of new ideas here. Just start reading, try out the examples on your own machine, and trust that it will start to make more sense as you work your way through.

# What are classes?
# ===
# Classes are a way of combining information and behavior. For example, think about what you'd need to do if you were creating a rocket ship in a game, or in a physics simulation. One of the first things you'd want to track are the x and y coordinates of the rocket. Here is what a simple rocket ship class looks like in code:

# In[11]:


class Rocket():
    # Rocket simulates a rocket ship for a game,
    #  or a physics simulation.
    
    def __init__(self):
        # Each rocket has an (x,y) position.
        self.x = 0
        self.y = 0


# One of the first things you do with a class is to define the **\__init\__()** method (`__` is a double underscore). The \_\_init\_\_() method sets the values for any parameters that need to be defined when an object is first created. The *self* part will be explained later; basically, it's a syntax that allows you to access a variable from anywhere else in the class.
# 
# The Rocket class stores two pieces of information so far, but it can't do anything. The first behavior to define is a core behavior of a rocket: moving up. Here is what that might look like in code:

# In[10]:


###highlight=[11,12,13]
class Rocket():
    # Rocket simulates a rocket ship for a game,
    #  or a physics simulation.
    
    def __init__(self):
        # Each rocket has an (x,y) position.
        self.x = 0
        self.y = 0
        
    def move_up(self):
        # Increment the y-position of the rocket.
        self.y += 1


# The Rocket class can now store some information, and it can do something. But this code has not actually created a rocket yet. Here is how you actually make a rocket:

# In[4]:


###highlight=[15,16, 17]
class Rocket():
    # Rocket simulates a rocket ship for a game,
    #  or a physics simulation.
    
    def __init__(self):
        # Each rocket has an (x,y) position.
        self.x = 0
        self.y = 0
        
    def move_up(self):
        # Increment the y-position of the rocket.
        self.y += 1

# Create a Rocket object.
my_rocket = Rocket()
print(my_rocket)


# To actually use a class, you create a variable such as *my\_rocket*. Then you set that equal to the name of the class, with an empty set of parentheses. Python creates an **object** from the class. An object is a single *instance* of the Rocket class; it has a copy of each of the class's variables, and it can do any action that is defined for the class. In this case, you can see that the variable my\_rocket is a Rocket object from the \_\_main\_\_ program file, which is stored at a particular location in memory. Each instance is independent of another. Normally, changes you make to one will not affect other instances you've created. 
# 
# Once you have a class, you can define an object and use its methods. Here is how you might define a rocket and have it start to move up:

# In[7]:


class Rocket():
    # Rocket simulates a rocket ship for a game,
    #  or a physics simulation.
    
    def __init__(self):
        # Each rocket has an (x,y) position.
        self.x = 0
        self.y = 0
        
    def move_up(self):
        # Increment the y-position of the rocket.
        self.y += 1

# Create a Rocket object, and have it start to move up.
my_rocket = Rocket()
print("Rocket altitude:", my_rocket.y)

my_rocket.move_up()
print("Rocket altitude:", my_rocket.y)

my_rocket.move_up()
print("Rocket altitude:", my_rocket.y)


# To access an object's variables or methods, you give the name of the object and then use *dot notation* to access the variables and methods. So to get the y-value of `my_rocket*` you use `my_rocket.y`. To use the move_up() method on my_rocket, you write `my_rocket.move_up()`.
# 
# 
# <div class="alert alert-block alert-info">
# You'll recognize this dot notation from things like random.shuffle() (shuffle is one of the methods possessed by objects instantiated by the Random class inside the random module contained in random.py). Whew..
# </div>
# 
# 
# Once you have a class defined, you can create as many objects from that class as you want. Each object is its own instance of that class, with its own separate variables. All of the objects are capable of the same behavior, but each object's particular actions do not affect any of the other objects. Here is how you might make a simple fleet of rockets:

# In[11]:


class Rocket():
    # Rocket simulates a rocket ship for a game,
    #  or a physics simulation.
    
    def __init__(self):
        # Each rocket has an (x,y) position.
        self.x = 0
        self.y = 0
        
    def move_up(self):
        # Increment the y-position of the rocket.
        self.y += 1
        
# Create a fleet of 5 rockets, and store them in a list.
my_rockets = []
for x in range(0,5):
    new_rocket = Rocket()
    my_rockets.append(new_rocket)

# Show that each rocket is a separate object.
for rocket in my_rockets:
    print(rocket)


# You can see that each rocket is at a separate place in memory. By the way, if you understand [list comprehensions](http://introtopython.org/lists_tuples.html#comprehensions), you can make the fleet of rockets in one line:

# In[12]:


###highlight=[16]
class Rocket():
    # Rocket simulates a rocket ship for a game,
    #  or a physics simulation.
    
    def __init__(self):
        # Each rocket has an (x,y) position.
        self.x = 0
        self.y = 0
        
    def move_up(self):
        # Increment the y-position of the rocket.
        self.y += 1
        
# Create a fleet of 5 rockets, and store them in a list.
my_rockets = [Rocket() for x in range(0,5)]

# Show that each rocket is a separate object.
for rocket in my_rockets:
    print(rocket)


# You can prove that each rocket has its own x and y values by moving just one of the rockets:

# In[15]:


###highlight=[18,19,20,21,22,23]
class Rocket():
    # Rocket simulates a rocket ship for a game,
    #  or a physics simulation.
    
    def __init__(self):
        # Each rocket has an (x,y) position.
        self.x = 0
        self.y = 0
        
    def move_up(self):
        # Increment the y-position of the rocket.
        self.y += 1
        
# Create a fleet of 5 rockets, and store them in a list.
my_rockets = [Rocket() for x in range(0,5)]

# Move the first rocket up.
my_rockets[0].move_up()

# Show that only the first rocket has moved.
for rocket in my_rockets:
    print("Rocket altitude:", rocket.y)


# The syntax for classes may not be very clear at this point, but consider for a moment how you might create a rocket without using classes. You might store the x and y values in a dictionary, but you would have to write a lot of ugly, hard-to-maintain code to manage even a small set of rockets. As more features become incorporated into the Rocket class, you will see how much more efficiently real-world objects can be modeled with classes than they could be using just lists and dictionaries.

# Classes in Python 2.7
# ---
# When you write a class in Python 2.7, you should always include the word `object` in parentheses when you define the class. This makes sure your Python 2.7 classes act like Python 3 classes, which will be helpful as your projects grow more complicated.
# 
# The simple version of the rocket class would look like this in Python 2.7:

# In[2]:


###highlight=[2]
class Rocket(object):
    # Rocket simulates a rocket ship for a game,
    #  or a physics simulation.
    
    def __init__(self):
        # Each rocket has an (x,y) position.
        self.x = 0
        self.y = 0


# This syntax will work in Python 3 as well.

# Object-Oriented terminology
# ===
# Classes are part of a programming paradigm called **object-oriented programming**. Object-oriented programming, or OOP for short, focuses on building reusable blocks of code called classes. When you want to use a class in one of your programs, you make an **object** from that class, which is where the phrase "object-oriented" comes from. Python itself is not tied to object-oriented programming, but you will be using objects in most or all of your Python projects. In order to understand classes, you have to understand some of the language that is used in OOP.

# General terminology
# ---
# A **class** is a body of code that defines the **attributes** and **behaviors** required to accurately model something you need for your program. You can model something from the real world, such as a rocket ship or a guitar string, or you can model something from a virtual world such as a rocket in a game, or a set of physical laws for a game engine.
# 
# An **attribute** is a piece of information. In code, an attribute is just a variable that is part of a class.
# 
# A **behavior** is an action that is defined within a class. These are made up of **methods**, which are just functions that are defined for the class.
# 
# An **object** is a particular instance of a class. An object has a certain set of values for all of the attributes (variables) in the class. You can have as many objects as you want for any one class.
# 
# There is much more to know, but these words will help you get started. They will make more sense as you see more examples, and start to use classes on your own.

# A closer look at the Rocket class
# ---
# Now that you have seen a simple example of a class, and have learned some basic OOP terminology, it will be helpful to take a closer look at the Rocket class.

# The \_\_init\_\_() method
# ---
# Here is the initial code block that defined the Rocket class:

# In[16]:


class Rocket():
    # Rocket simulates a rocket ship for a game,
    #  or a physics simulation.
    
    def __init__(self):
        # Each rocket has an (x,y) position.
        self.x = 0
        self.y = 0


# The first line shows how a class is created in Python. The keyword **class** tells Python that you are about to define a class. The rules for naming a class are the same rules you learned about [naming variables](var_string_num.html#naming_rules), but there is a strong convention among Python programmers that classes should be named using CamelCase. If you are unfamiliar with CamelCase, it is a convention where each letter that starts a word is capitalized, with no underscores in the name. The name of the class is followed by a set of parentheses. These parentheses will be empty for now, but later they may contain a class upon which the new class is based.
# 
# It is good practice to write a comment at the beginning of your class, describing the class. There is a [more formal syntax](http://www.python.org/dev/peps/pep-0257/) for documenting your classes, but you can wait a little bit to get that formal. For now, just write a comment at the beginning of your class summarizing what you intend the class to do. Writing more formal documentation for your classes will be easy later if you start by writing simple comments now.
# 
# Function names that start and end with two underscores are special built-in functions that Python uses in certain ways. The \_\_init()\_\_ method is one of these special functions. It is called automatically when you create an object from your class. The \_\_init()\_\_ method lets you make sure that all relevant attributes are set to their proper values when an object is created from the class, before the object is used. In this case, The \_\_init\_\_() method initializes the x and y values of the Rocket to 0.
# 
# The **self** keyword often takes people a little while to understand. The word "self" refers to the current object that you are working with. When you are writing a class, it lets you refer to certain attributes from any other part of the class. Basically, all methods in a class need the *self* object as their first argument, so they can access any attribute that is part of the class.
# 
# Now let's take a closer look at a **method**.

# A simple method
# ---
# Here is the method that was defined for the Rocket class:

# In[17]:


class Rocket():
    # Rocket simulates a rocket ship for a game,
    #  or a physics simulation.
    
    def __init__(self):
        # Each rocket has an (x,y) position.
        self.x = 0
        self.y = 0
        
    def move_up(self):
        # Increment the y-position of the rocket.
        self.y += 1


# A method is just a function that is part of a class. Since it is just a function, you can do anything with a method that you learned about with functions. You can accept [positional](more_functions.html#positional_arguments) arguments, [keyword](more_functions.html#keyword_arguments) arguments, an arbitrary [list of argument values](more_functions.html#arbitrary_sequence), an arbitrary [dictionary of arguments](more_functions.html#arbitrary_keyword_arguments), or any combination of these. Your arguments can return a value or a set of values if you want, or they can just do some work without returning any values.
# 
# Each method has to accept one argument by default, the value **self**. This is a reference to the particular object that is calling the method. This *self* argument gives you access to the calling object's attributes. In this example, the self argument is used to access a Rocket object's y-value. That value is increased by 1, every time the method move_up() is called by a particular Rocket object. This is probably still somewhat confusing, but it should start to make sense as you work through your own examples.
# 
# If you take a second look at what happens when a method is called, things might make a little more sense:

# In[18]:


class Rocket():
    # Rocket simulates a rocket ship for a game,
    #  or a physics simulation.
    
    def __init__(self):
        # Each rocket has an (x,y) position.
        self.x = 0
        self.y = 0
        
    def move_up(self):
        # Increment the y-position of the rocket.
        self.y += 1

# Create a Rocket object, and have it start to move up.
my_rocket = Rocket()
print("Rocket altitude:", my_rocket.y)

my_rocket.move_up()
print("Rocket altitude:", my_rocket.y)

my_rocket.move_up()
print("Rocket altitude:", my_rocket.y)


# In this example, a Rocket object is created and stored in the variable my_rocket. After this object is created, its y value is printed. The value of the attribute *y* is accessed using dot notation. The phrase *my\_rocket.y* asks Python to return "the value of the variable y attached to the object my_rocket".
# 
# After the object my_rocket is created and its initial y-value is printed, the method move_up() is called. This tells Python to apply the method move_up() to the object my_rocket. Python finds the y-value associated with my_rocket and adds 1 to that value. This process is repeated several times, and you can see from the output that the y-value is in fact increasing.

# <div class="alert alert-block alert-info">
# Want to remind yourself what methods are defined/available for use with an object? Use `help(your_object)`
# </div>
# 

# Making multiple objects from a class
# ---
# One of the goals of object-oriented programming is to create reusable code. Once you have written the code for a class, you can create as many objects from that class as you need. It is worth mentioning at this point that classes are usually saved in a separate file, and then imported into the program you are working on. So you can build a library of classes, and use those classes over and over again in different programs. Once you know a class works well, you can leave it alone and know that the objects you create in a new program are going to work as they always have.
# 
# You can see this "code reusability" already when the Rocket class is used to make more than one Rocket object. Here is the code that made a fleet of Rocket objects:

# In[19]:


###highlight=[15,16,17,18,19,20,21,22,23]
class Rocket():
    # Rocket simulates a rocket ship for a game,
    #  or a physics simulation.
    
    def __init__(self):
        # Each rocket has an (x,y) position.
        self.x = 0
        self.y = 0
        
    def move_up(self):
        # Increment the y-position of the rocket.
        self.y += 1
        
# Create a fleet of 5 rockets, and store them in a list.
my_rockets = []
for x in range(0,5):
    new_rocket = Rocket()
    my_rockets.append(new_rocket)

# Show that each rocket is a separate object.
for rocket in my_rockets:
    print(rocket)


# If you are comfortable using list comprehensions, go ahead and use those as much as you can. I'd rather not assume at this point that everyone is comfortable with comprehensions, so I will use the slightly longer approach of declaring an empty list, and then using a for loop to fill that list. That can be done slightly more efficiently than the previous example, by eliminating the temporary variable *new\_rocket*:

# In[20]:


class Rocket():
    # Rocket simulates a rocket ship for a game,
    #  or a physics simulation.
    
    def __init__(self):
        # Each rocket has an (x,y) position.
        self.x = 0
        self.y = 0
        
    def move_up(self):
        # Increment the y-position of the rocket.
        self.y += 1
        
# Create a fleet of 5 rockets, and store them in a list.
my_rockets = []
for x in range(0,5):
    my_rockets.append(Rocket())

# Show that each rocket is a separate object.
for rocket in my_rockets:
    print(rocket)


# What exactly happens in this for loop? The line *my\_rockets.append(Rocket())* is executed 5 times. Each time, a new Rocket object is created and then added to the list my\_rockets. The \_\_init\_\_() method is executed once for each of these objects, so each object gets its own x and y value. When a method is called on one of these objects, the *self* variable allows access to just that object's attributes, and ensures that modifying one object does not affect any of the other objecs that have been created from the class.
# 
# Each of these objects can be worked with individually. At this point we are ready to move on and see how to add more functionality to the Rocket class. We will work slowly, and give you the chance to start writing your own simple classes.

# A quick check-in
# ---
# If all of this makes sense, then the rest of your work with classes will involve learning a lot of details about how classes can be used in more flexible and powerful ways. If this does not make any sense, you could try a few different things:
# 
# - Reread the previous sections, and see if things start to make any more sense.
# - Type out these examples in your own editor, and run them. Try making some changes, and see what happens.
# - Try the next exercise, and see if it helps solidify some of the concepts you have been reading about.
# - Read on. The next sections are going to add more functionality to the Rocket class. These steps will involve rehashing some of what has already been covered, in a slightly different way.
# 
# Classes are a huge topic, and once you understand them you will probably use them for the rest of your life as a programmer. If you are brand new to this, be patient and trust that things will start to sink in.

# Refining the Rocket class
# ===
# The Rocket class so far is very simple. It can be made a little more interesting with some refinements to the \_\_init\_\_() method, and by the addition of some methods.

# Accepting parameters for the \_\_init\_\_() method
# ---
# The \_\_init\_\_() method is run automatically one time when you create a new object from a class. The \_\_init\_\_() method for the Rocket class so far is pretty simple:

# In[ ]:


class Rocket():
    # Rocket simulates a rocket ship for a game,
    #  or a physics simulation.
    
    def __init__(self):
        # Each rocket has an (x,y) position.
        self.x = 0
        self.y = 0
        
    def move_up(self):
        # Increment the y-position of the rocket.
        self.y += 1


# All the \_\_init\_\_() method does so far is set the x and y values for the rocket to 0. We can easily add a couple keyword arguments so that new rockets can be initialized at any position:

# In[ ]:


class Rocket():
    # Rocket simulates a rocket ship for a game,
    #  or a physics simulation.
    
    def __init__(self, x=0, y=0):
        # Each rocket has an (x,y) position.
        self.x = x
        self.y = y
        
    def move_up(self):
        # Increment the y-position of the rocket.
        self.y += 1


# Now when you create a new Rocket object you have the choice of passing in arbitrary initial values for x and y:

# In[22]:


class Rocket():
    # Rocket simulates a rocket ship for a game,
    #  or a physics simulation.
    
    def __init__(self, x=0, y=0):
        # Each rocket has an (x,y) position.
        self.x = x
        self.y = y
        
    def move_up(self):
        # Increment the y-position of the rocket.
        self.y += 1
        
# Make a series of rockets at different starting places.
rockets = []
rockets.append(Rocket())
rockets.append(Rocket(0,10))
rockets.append(Rocket(100,0))

# Show where each rocket is.
for index, rocket in enumerate(rockets):
    print("Rocket %d is at (%d, %d)." % (index, rocket.x, rocket.y))


# Accepting parameters in a method
# ---
# The \_\_init\_\_ method is just a special method that serves a particular purpose, which is to help create new objects from a class. Any method in a class can accept parameters of any kind. With this in mind, the move_up() method can be made much more flexible. By accepting keyword arguments, the move_up() method can be rewritten as a more general move_rocket() method. This new method will allow the rocket to be moved any amount, in any direction:

# In[23]:


###highlight=[11,12,13,14,15]
class Rocket():
    # Rocket simulates a rocket ship for a game,
    #  or a physics simulation.
    
    def __init__(self, x=0, y=0):
        # Each rocket has an (x,y) position.
        self.x = x
        self.y = y
        
    def move_rocket(self, x_increment=0, y_increment=1):
        # Move the rocket according to the paremeters given.
        #  Default behavior is to move the rocket up one unit.
        self.x += x_increment
        self.y += y_increment


# The paremeters for the move() method are named x_increment and y_increment rather than x and y. It's good to emphasize that these are changes in the x and y position, not new values for the actual position of the rocket. By carefully choosing the right default values, we can define a meaningful default behavior. If someone calls the method move_rocket() with no parameters, the rocket will simply move up one unit in the y-direciton. Note that this method can be given negative values to move the rocket left or right:

# In[25]:


class Rocket():
    # Rocket simulates a rocket ship for a game,
    #  or a physics simulation.
    
    def __init__(self, x=0, y=0):
        # Each rocket has an (x,y) position.
        self.x = x
        self.y = y
        
    def move_rocket(self, x_increment=0, y_increment=1):
        # Move the rocket according to the paremeters given.
        #  Default behavior is to move the rocket up one unit.
        self.x += x_increment
        self.y += y_increment
        
# Create three rockets.
rockets = [Rocket() for x in range(0,3)]

# Move each rocket a different amount.
rockets[0].move_rocket()
rockets[1].move_rocket(10,10)
rockets[2].move_rocket(-10,0)
          
# Show where each rocket is.
for index, rocket in enumerate(rockets):
    print("Rocket %d is at (%d, %d)." % (index, rocket.x, rocket.y))


# [top](#)

# Adding a new method
# ---
# One of the strengths of object-oriented programming is the ability to closely model real-world phenomena by adding appropriate attributes and behaviors to classes. One of the jobs of a team piloting a rocket is to make sure the rocket does not get too close to any other rockets. Let's add a method that will report the distance from one rocket to any other rocket.
# 
# If you are not familiar with distance calculations, there is a fairly simple formula to tell the distance between two points if you know the x and y values of each point. This new method performs that calculation, and then returns the resulting distance.

# In[36]:


from math import sqrt

class Rocket():
    # Rocket simulates a rocket ship for a game,
    #  or a physics simulation.
    
    def __init__(self, x=0, y=0):
        # Each rocket has an (x,y) position.
        self.x = x
        self.y = y
        
    def move_rocket(self, x_increment=0, y_increment=1):
        # Move the rocket according to the paremeters given.
        #  Default behavior is to move the rocket up one unit.
        self.x += x_increment
        self.y += y_increment
        
    def get_distance(self, other_rocket):
        # Calculates the distance from this rocket to another rocket,
        #  and returns that value.
        distance = sqrt((self.x-other_rocket.x)**2+(self.y-other_rocket.y)**2)
        return distance
    
# Make two rockets, at different places.
rocket_0 = Rocket()
rocket_1 = Rocket(10,5)

# Show the distance between them.
distance = rocket_0.get_distance(rocket_1)
print("The rockets are %f units apart." % distance)


# Hopefully these short refinements show that you can extend a class' attributes and behavior to model the phenomena you are interested in as closely as you want. The rocket could have a name, a crew capacity, a payload, a certain amount of fuel, and any number of other attributes. You could define any behavior you want for the rocket, including interactions with other rockets and launch facilities, gravitational fields, and whatever you need it to! There are techniques for managing these more complex interactions, but what you have just seen is the core of object-oriented programming.
# 
# At this point you should try your hand at writing some classes of your own. After trying some exercises, we will look at object inheritance, and then you will be ready to move on for now.

# [top](#)

# [top](#)

# Inheritance
# ===
# One of the most important goals of the object-oriented approach to programming is the creation of stable, reliable, reusable code. If you had to create a new class for every kind of object you wanted to model, you would hardly have any reusable code. In Python and any other language that supports OOP, one class can **inherit** from another class. This means you can base a new class on an existing class; the new class *inherits* all of the attributes and behavior of the class it is based on. A new class can override any undesirable attributes or behavior of the class it inherits from, and it can add any new attributes or behavior that are appropriate. The original class is called the **parent** class, and the new class is a **child** of the parent class. The parent class is also called a **superclass**, and the child class is also called a **subclass**.
# 
# The child class inherits all attributes and behavior from the parent class, but any attributes that are defined in the child class are not available to the parent class. This may be obvious to many people, but it is worth stating. This also means a child class can override behavior of the parent class. If a child class defines a method that also appears in the parent class, objects of the child class will use the new method rather than the parent class method.
# 
# To better understand inheritance, let's look at an example of a class that can be based on the Rocket class.

# The SpaceShuttle class
# ---
# If you wanted to model a space shuttle, you could write an entirely new class. But a space shuttle is just a special kind of rocket. Instead of writing an entirely new class, you can inherit all of the attributes and behavior of a Rocket, and then add a few appropriate attributes and behavior for a Shuttle.
# 
# One of the most significant characteristics of a space shuttle is that it can be reused. So the only difference we will add at this point is to record the number of flights the shutttle has completed. Everything else you need to know about a shuttle has already been coded into the Rocket class.
# 
# Here is what the Shuttle class looks like:

# In[11]:


from math import sqrt

class Rocket():
    # Rocket simulates a rocket ship for a game,
    #  or a physics simulation.
    
    def __init__(self, x=0, y=0):
        # Each rocket has an (x,y) position.
        self.x = x
        self.y = y
        
    def move_rocket(self, x_increment=0, y_increment=1):
        # Move the rocket according to the paremeters given.
        #  Default behavior is to move the rocket up one unit.
        self.x += x_increment
        self.y += y_increment
        
    def get_distance(self, other_rocket):
        # Calculates the distance from this rocket to another rocket,
        #  and returns that value.
        distance = sqrt((self.x-other_rocket.x)**2+(self.y-other_rocket.y)**2)
        return distance
    
class Shuttle(Rocket):
    # Shuttle simulates a space shuttle, which is really
    #  just a reusable rocket.
    
    def __init__(self, x=0, y=0, flights_completed=0):
        super().__init__(x, y)
        self.flights_completed = flights_completed
        
shuttle = Shuttle(10,0,3)
print(shuttle)


# When a new class is based on an existing class, you write the name of the parent class in parentheses when you define the new class:
# 
#     

# In[ ]:


class NewClass(ParentClass):


# The \_\_init\_\_() function of the new class needs to call the \_\_init\_\_() function of the parent class. The \_\_init\_\_() function of the new class needs to accept all of the parameters required to build an object from the parent class, and these parameters need to be passed to the \_\_init\_\_() function of the parent class. The *super().\_\_init\_\_()* function takes care of this:

# In[ ]:


###highlight=[5]
class NewClass(ParentClass):
    
    def __init__(self, arguments_new_class, arguments_parent_class):
        super().__init__(arguments_parent_class)
        # Code for initializing an object of the new class.


# The *super()* function passes the *self* argument to the parent class automatically. You could also do this by explicitly naming the parent class when you call the \_\_init\_\_() function, but you then have to include the *self* argument manually:

# In[ ]:


class Shuttle(Rocket):
    # Shuttle simulates a space shuttle, which is really
    #  just a reusable rocket.
    
    def __init__(self, x=0, y=0, flights_completed=0):
        Rocket.__init__(self, x, y)
        self.flights_completed = flights_completed


# This might seem a little easier to read, but it is preferable to use the *super()* syntax. When you use *super()*, you don't need to explicitly name the parent class, so your code is more resilient to later changes. As you learn more about classes, you will be able to write child classes that inherit from multiple parent classes, and the *super()* function will call the parent classes' \_\_init\_\_() functions for you, in one line. This explicit approach to calling the parent class' \_\_init\_\_() function is included so that you will be less confused if you see it in someone else's code.

# The output above shows that a new Shuttle object was created. This new Shuttle object can store the number of flights completed, but it also has all of the functionality of the Rocket class: it has a position that can be changed, and it can calculate the distance between itself and other rockets or shuttles. This can be demonstrated by creating several rockets and shuttles, and then finding the distance between one shuttle and all the other shuttles and rockets. This example uses a simple function called [randint](http://docs.python.org/2/library/random.html#random.randint), which generates a random integer between a lower and upper bound, to determine the position of each rocket and shuttle:

# In[13]:


from math import sqrt
from random import randint

class Rocket():
    # Rocket simulates a rocket ship for a game,
    #  or a physics simulation.
    
    def __init__(self, x=0, y=0):
        # Each rocket has an (x,y) position.
        self.x = x
        self.y = y
        
    def move_rocket(self, x_increment=0, y_increment=1):
        # Move the rocket according to the paremeters given.
        #  Default behavior is to move the rocket up one unit.
        self.x += x_increment
        self.y += y_increment
        
    def get_distance(self, other_rocket):
        # Calculates the distance from this rocket to another rocket,
        #  and returns that value.
        distance = sqrt((self.x-other_rocket.x)**2+(self.y-other_rocket.y)**2)
        return distance
    
class Shuttle(Rocket):
    # Shuttle simulates a space shuttle, which is really
    #  just a reusable rocket.
    
    def __init__(self, x=0, y=0, flights_completed=0):
        super().__init__(x, y)
        self.flights_completed = flights_completed
        
        
# Create several shuttles and rockets, with random positions.
#  Shuttles have a random number of flights completed.
shuttles = []
for x in range(0,3):
    x = randint(0,100)
    y = randint(1,100)
    flights_completed = randint(0,10)
    shuttles.append(Shuttle(x, y, flights_completed))

rockets = []
for x in range(0,3):
    x = randint(0,100)
    y = randint(1,100)
    rockets.append(Rocket(x, y))
    
# Show the number of flights completed for each shuttle.
for index, shuttle in enumerate(shuttles):
    print("Shuttle %d has completed %d flights." % (index, shuttle.flights_completed))
    
print("\n")    
# Show the distance from the first shuttle to all other shuttles.
first_shuttle = shuttles[0]
for index, shuttle in enumerate(shuttles):
    distance = first_shuttle.get_distance(shuttle)
    print("The first shuttle is %f units away from shuttle %d." % (distance, index))

print("\n")
# Show the distance from the first shuttle to all other rockets.
for index, rocket in enumerate(rockets):
    distance = first_shuttle.get_distance(rocket)
    print("The first shuttle is %f units away from rocket %d." % (distance, index))


# Inheritance is a powerful feature of object-oriented programming. Using just what you have seen so far about classes, you can model an incredible variety of real-world and virtual phenomena with a high degree of accuracy. The code you write has the potential to be stable and reusable in a variety of applications.

# [top](#)

# Inheritance in Python 2.7
# ---
# The *super()* method has a slightly different syntax in Python 2.7:

# In[ ]:


###highlight=[5]
class NewClass(ParentClass):
    
    def __init__(self, arguments_new_class, arguments_parent_class):
        super(NewClass, self).__init__(arguments_parent_class)
        # Code for initializing an object of the new class.


# Notice that you have to explicitly pass the arguments *NewClass* and *self* when you call *super()* in Python 2.7. The SpaceShuttle class would look like this:

# In[12]:


from math import sqrt

class Rocket(object):
    # Rocket simulates a rocket ship for a game,
    #  or a physics simulation.
    
    def __init__(self, x=0, y=0):
        # Each rocket has an (x,y) position.
        self.x = x
        self.y = y
        
    def move_rocket(self, x_increment=0, y_increment=1):
        # Move the rocket according to the paremeters given.
        #  Default behavior is to move the rocket up one unit.
        self.x += x_increment
        self.y += y_increment
        
    def get_distance(self, other_rocket):
        # Calculates the distance from this rocket to another rocket,
        #  and returns that value.
        distance = sqrt((self.x-other_rocket.x)**2+(self.y-other_rocket.y)**2)
        return distance
    
class Shuttle(Rocket):
    # Shuttle simulates a space shuttle, which is really
    #  just a reusable rocket.
    
    def __init__(self, x=0, y=0, flights_completed=0):
        super(Shuttle, self).__init__(x, y)
        self.flights_completed = flights_completed
        
shuttle1 = Shuttle(10,0,3)
shuttle2 = Shuttle(0,10,1)
print 'distance between shuttle1 and shuttle2 is', shuttle1.get_distance(shuttle2)


# This syntax works in Python 3 as well.

# # Example of using a class in a Psychopy experiment
# 
# This section goes through a more practical example of using a class in an experiment. Let's say we want to make a moving circle that wiggles its way across a window. Here's some basic code to make this happen.

# ## A single moving circle

# In[ ]:


import time
import random
import sys
import os
from math import *
from psychopy import visual, core, event

win = visual.Window([300,300],color="black", units='pix',allowGUI=True)
myMouse = event.Mouse(win=win)

target = visual.Circle(win,size=20,lineColor="black",fillColor=[1,1,1])
minAngle=-30;
maxAngle=30;
prevAngleToDeviate=0
newCurAngle=0.0
interStepInterval = 4.0

while True:
	core.wait(.02)
	target.draw()
	win.flip()

	curAngleToDeviate = prevAngleToDeviate + random.randint(minAngle,maxAngle); #calculate new angle
	curAngle = curAngleToDeviate*pi/180.0; #convert to radians
	
	newXPos = interStepInterval*cos(curAngle)	
	newYPos = interStepInterval*sin(curAngle)
	
	target.setPos((newXPos,newYPos),'+')
	hitBoundary=False
	if (abs(target.pos[0]) > 150 or abs(target.pos[1]) > 150):
		hitBoundary=True
		newXPos =  interStepInterval*cos(curAngle-pi)
		newYPos =  interStepInterval*sin(curAngle-pi)

	prevAngleToDeviate = curAngleToDeviate
	if hitBoundary:
		prevAngleToDeviate -= 180
		prevAngleToDeviate %= 360

	if event.getKeys(['space']):
		break


# Let's extend this code so that when we click on the circle, it gets dimmer and moves slower.

# In[ ]:


import time
import random
import sys
import os
from math import *
from psychopy import visual, core, event

win = visual.Window([300,300],color="black", units='pix',allowGUI=True)
myMouse = event.Mouse(win=win)

target = visual.Circle(win,size=20,lineColor="black",fillColor=[1,1,1])
minAngle=-30;
maxAngle=30;
prevAngleToDeviate=0
newCurAngle=0.0
interStepInterval = 4.0

while True:
	core.wait(.02)
	target.draw()
	win.flip()

	curAngleToDeviate = prevAngleToDeviate + random.randint(minAngle,maxAngle); #calculate new angle
	curAngle = curAngleToDeviate*pi/180.0; #convert to radians
	
	newXPos = interStepInterval*cos(curAngle)	
	newYPos = interStepInterval*sin(curAngle)

	if myMouse.isPressedIn(target):
		interStepInterval *= .8
		target.opacity *= .9
	
	target.setPos((newXPos,newYPos),'+')
	hitBoundary=False
	if (abs(target.pos[0]) > 150 or abs(target.pos[1]) > 150):
		hitBoundary=True
		newXPos =  interStepInterval*cos(curAngle-pi)
		newYPos =  interStepInterval*sin(curAngle-pi)

	prevAngleToDeviate = curAngleToDeviate
	if hitBoundary:
		prevAngleToDeviate -= 180
		prevAngleToDeviate %= 360

	if event.getKeys(['space']):
		break


# ## More circles!
# But now suppose we want to have lots of moving circles that move independently of one another such that we can set some to move faster, have them be different colors, allow people to click on them independently, etc. This is the kind of situation where classes shine. 
# 
# The code below implements a `movingCircle` class. We then use it to make a bunch of individual circles and allow the user to click on them individually. Notice that it's not much longer than the code above. And if we want 10 circles, we just need to change `numCircles = 4` to `numCircles = 5`. Wizardry!

# In[ ]:


import time
import random
import sys
import os
from math import sin, cos, pi
from psychopy import visual, core, event

win = visual.Window([300,300],color="black", units='pix',allowGUI=True)
myMouse = event.Mouse(win=win)
numCircles = 4

class movingCircle():
	
	def __init__(self,win):

		self.minAngle=-30;
		self.maxAngle=30;
		self.prevAngleToDeviate=0
		self.angleMovingDegrees=0.0
		self.interStepInterval = 2.0
		self.target = visual.Circle(win,size=20,lineColor="black",fillColor=[1,1,1])

	def change_speed(self,delta_speed):
		self.interStepInterval *= delta_speed

	def make_dimmer(self,percent):
		self.target.opacity *= percent

	def get_pos(self):
		return self.target.pos

	def target(self):
		return self.target

	def move_it(self):
		"gets new position and set target to that position"
		curAngleToDeviate = self.prevAngleToDeviate + random.randint(self.minAngle,self.maxAngle); #calculate new angle
		curAngle = curAngleToDeviate*pi/180.0; #convert to radians
		
		newXPos = self.interStepInterval*cos(curAngle)	
		newYPos = self.interStepInterval*sin(curAngle)
		
		self.target.setPos((newXPos,newYPos),'+')
		hitBoundary=False
		if (abs(self.target.pos[0]) > 150 or abs(self.target.pos[1]) > 150):
			hitBoundary=True
			newXPos =  self.interStepInterval*cos(curAngle-pi)
			newYPos =  self.interStepInterval*sin(curAngle-pi)

		self.prevAngleToDeviate = curAngleToDeviate
		if hitBoundary:
			self.prevAngleToDeviate -= 180
			self.prevAngleToDeviate %= 360


circles = [movingCircle(win) for _ in range(numCircles)]
while True:
	for curCircle in circles:
		curCircle.target.draw()
		if myMouse.isPressedIn(curCircle.target):
			print 'clicked on a circle!' 
			curCircle.change_speed(.8)
			curCircle.make_dimmer(.9)

		curCircle.move_it()
	core.wait(.05)
	win.flip()

	if event.getKeys(['space']):
		break


# Make sure you understand what's happening here. Play around with the code. If you're confused, message on Slack.

# Modules and classes
# ===
# Now that you are starting to work with classes, your files are going to grow longer. This is good, because it means your programs are probably doing more interesting things. But it is bad, because longer files can be more difficult to work with. Python allows you to save your classes in another file and then import them into the program you are working on. This has the added advantage of isolating your classes into files that can be used in any number of different programs. As you use your classes repeatedly, the classes become more reliable and complete overall.

# Storing a single class in a module
# ---
# 
# When you save a class into a separate file, that file is called a **module**. You can have any number of classes in a single module. There are a number of ways you can then import the class you are interested in.
# 
# Start out by saving just the Rocket class into a file called *rocket.py*. Notice the naming convention being used here: the module is saved with a lowercase name, and the class starts with an uppercase letter. This convention is pretty important for a number of reasons, and it is a really good idea to follow the convention.

# In[48]:


###highlight=[2]
# Save as rocket.py
from math import sqrt

class Rocket():
    # Rocket simulates a rocket ship for a game,
    #  or a physics simulation.
    
    def __init__(self, x=0, y=0):
        # Each rocket has an (x,y) position.
        self.x = x
        self.y = y
        
    def move_rocket(self, x_increment=0, y_increment=1):
        # Move the rocket according to the paremeters given.
        #  Default behavior is to move the rocket up one unit.
        self.x += x_increment
        self.y += y_increment
        
    def get_distance(self, other_rocket):
        # Calculates the distance from this rocket to another rocket,
        #  and returns that value.
        distance = sqrt((self.x-other_rocket.x)**2+(self.y-other_rocket.y)**2)
        return distance


# Make a separate file called *rocket_game.py*. If you are more interested in science than games, feel free to call this file something like *rocket_simulation.py*. Again, to use standard naming conventions, make sure you are using a lowercase_underscore name for this file.

# In[55]:


# Save as rocket_game.py
from rocket import Rocket

rocket = Rocket()
print("The rocket is at (%d, %d)." % (rocket.x, rocket.y))


# This is a really clean and uncluttered file. A rocket is now something you can define in your programs, without the details of the rocket's implementation cluttering up your file. You don't have to include all the class code for a rocket in each of your files that deals with rockets; the code defining rocket attributes and behavior lives in one file, and can be used anywhere.
# 
# The first line tells Python to look for a file called *rocket.py*. It looks for that file in the same directory as your current program. You can put your classes in other directories, but we will get to that convention a bit later. Notice that you do not
# 
# When Python finds the file *rocket.py*, it looks for a class called *Rocket*. When it finds that class, it imports that code into the current file, without you ever seeing that code. You are then free to use the class Rocket as you have seen it used in previous examples.

# [top](#)

# Storing multiple classes in a module
# ---
# 
# A module is simply a file that contains one or more classes or functions, so the Shuttle class actually belongs in the rocket module as well:

# In[ ]:


# Save as rocket.py
from math import sqrt

class Rocket():
    # Rocket simulates a rocket ship for a game,
    #  or a physics simulation.
    
    def __init__(self, x=0, y=0):
        # Each rocket has an (x,y) position.
        self.x = x
        self.y = y
        
    def move_rocket(self, x_increment=0, y_increment=1):
        # Move the rocket according to the paremeters given.
        #  Default behavior is to move the rocket up one unit.
        self.x += x_increment
        self.y += y_increment
        
    def get_distance(self, other_rocket):
        # Calculates the distance from this rocket to another rocket,
        #  and returns that value.
        distance = sqrt((self.x-other_rocket.x)**2+(self.y-other_rocket.y)**2)
        return distance
    

class Shuttle(Rocket):
    # Shuttle simulates a space shuttle, which is really
    #  just a reusable rocket.
    
    def __init__(self, x=0, y=0, flights_completed=0):
        super().__init__(x, y)
        self.flights_completed = flights_completed


# Now you can import the Rocket and the Shuttle class, and use them both in a clean uncluttered program file:

# In[14]:


###highlight=[3,8,9,10]
# Save as rocket_game.py
from rocket import Rocket, Shuttle

rocket = Rocket()
print("The rocket is at (%d, %d)." % (rocket.x, rocket.y))

shuttle = Shuttle()
print("\nThe shuttle is at (%d, %d)." % (shuttle.x, shuttle.y))
print("The shuttle has completed %d flights." % shuttle.flights_completed)


# The first line tells Python to import both the *Rocket* and the *Shuttle* classes from the *rocket* module. You don't have to import every class in a module; you can pick and choose the classes you care to use, and Python will only spend time processing those particular classes.

# A number of ways to import modules and classes
# ---
# There are several ways to import modules and classes, and each has its own merits.

# ### import *module_name*
# 
# The syntax for importing classes that was just shown:

# In[ ]:


from module_name import ClassName


# is straightforward, and is used quite commonly. It allows you to use the class names directly in your program, so you have very clean and readable code. This can be a problem, however, if the names of the classes you are importing conflict with names that have already been used in the program you are working on. This is unlikely to happen in the short programs you have been seeing here, but if you were working on a larger program it is quite possible that the class you want to import from someone else's work would happen to have a name you have already used in your program. In this case, you can use simply import the module itself:

# In[3]:


# Save as rocket_game.py
import rocket

rocket_0 = rocket.Rocket()
print("The rocket is at (%d, %d)." % (rocket_0.x, rocket_0.y))

shuttle_0 = rocket.Shuttle()
print("\nThe shuttle is at (%d, %d)." % (shuttle_0.x, shuttle_0.y))
print("The shuttle has completed %d flights." % shuttle_0.flights_completed)


# The general syntax for this kind of import is:
# 
#     

# In[ ]:


import module_name


# After this, classes are accessed using dot notation:

# In[ ]:


module_name.ClassName


# This prevents some name conflicts. If you were reading carefully however, you might have noticed that the variable name *rocket* in the previous example had to be changed because it has the same name as the module itself. This is not good, because in a longer program that could mean a lot of renaming.

# ### import *module_name* as *local_module_name*
# 
# There is another syntax for imports that is quite useful:

# In[ ]:


import module_name as local_module_name


# When you are importing a module into one of your projects, you are free to choose any name you want for the module in your project. So the last example could be rewritten in a way that the variable name *rocket* would not need to be changed:

# In[5]:


# Save as rocket_game.py
import rocket as rocket_module

rocket = rocket_module.Rocket()
print("The rocket is at (%d, %d)." % (rocket.x, rocket.y))

shuttle = rocket_module.Shuttle()
print("\nThe shuttle is at (%d, %d)." % (shuttle.x, shuttle.y))
print("The shuttle has completed %d flights." % shuttle.flights_completed)


# This approach is often used to shorten the name of the module, so you don't have to type a long module name before each class name that you want to use. But it is easy to shorten a name so much that you force people reading your code to scroll to the top of your file and see what the shortened name stands for. In this example,

# In[ ]:


import rocket as rocket_module


# leads to much more readable code than something like:

# In[ ]:


import rocket as r


# ### from *module_name* import *
# There is one more import syntax that you should be aware of, but you should probably avoid using. This syntax imports all of the available classes and functions in a module:

# In[ ]:


from module_name import *


# This is not recommended, for a couple reasons. First of all, you may have no idea what all the names of the classes and functions in a module are. If you accidentally give one of your variables the same name as a name from the module, you will have naming conflicts. Also, you may be importing way more code into your program than you need.
# 
# If you really need all the functions and classes from a module, just import the module and use the `module_name.ClassName` syntax in your program.

# You will get a sense of how to write your imports as you read more Python code, and as you write and share some of your own code.

# [top](#)

# A module of functions
# ---
# You can use modules to store a set of functions you want available in different programs as well, even if those functions are not attached to any one class. To do this, you save the functions into a file, and then import that file just as you saw in the last section. Here is a really simple example; save this is *multiplying.py*:

# In[2]:


# Save as multiplying.py
def double(x):
    return 2*x

def triple(x):
    return 3*x

def quadruple(x):
    return 4*x


# Now you can import the file *multiplying.py*, and use these functions. Using the `from module_name import function_name` syntax:

# In[3]:


from multiplying import double, triple, quadruple

print(double(5))
print(triple(5))
print(quadruple(5))


# Using the `import module_name` syntax:

# In[4]:


import multiplying

print(multiplying.double(5))
print(multiplying.triple(5))
print(multiplying.quadruple(5))


# Using the `import module_name as local_module_name` syntax:

# In[5]:


import multiplying as m

print(m.double(5))
print(m.triple(5))
print(m.quadruple(5))


# Using the `from module_name import *` syntax:

# In[7]:


from multiplying import *

print(double(5))
print(triple(5))
print(quadruple(5))

