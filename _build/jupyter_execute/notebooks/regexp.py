#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc" style="margin-top: 1em;"><ul class="toc-item"><li><span><a href="#Regular-expressions" data-toc-modified-id="Regular-expressions-1">Regular expressions</a></span><ul class="toc-item"><li><span><a href="#Use-as-a-filter" data-toc-modified-id="Use-as-a-filter-1.1">Use as a filter</a></span></li><li><span><a href="#Use-in-place-of-conditionals" data-toc-modified-id="Use-in-place-of-conditionals-1.2">Use in place of conditionals</a></span></li><li><span><a href="#Search-and-replace" data-toc-modified-id="Search-and-replace-1.3">Search and replace</a></span></li><li><span><a href="#Renaming-files" data-toc-modified-id="Renaming-files-1.4">Renaming files</a></span></li></ul></li></ul></div>

# # Regular expressions
# 
# Regular expressions are an immensely powerful tool built into most modern computer languages. They are a type of formal grammar that allow you to match strings that match or mismatch a particular rule. [http://www.rexegg.com/regex-uses.html](Common uses) include checking if user input conforms to a desired pattern (e.g., 3 numbers followed by two numbers, followed by 3 numbers), do all sorts of complicated search-replace operations both in text-files and, e.g., renaming files.
# 
# There are [https://www.amazon.com/Mastering-Regular-Expressions-Jeffrey-Friedl/dp/0596528124](entire books) written on regular expressions as well as [comprehensive online references](https://www.regular-expressions.info/). We'll only concern ourselves with a few basics here. 
# 
# Start by looking over the [first couple lessons of this tutorial](https://regexone.com/), paying special attention to the sidebar on right, which I reproduce below.

# Syntax | Meaning
# ------------- |:-------------
# abc…	 |  Literal letters
# \d	 | 	Any Digit
# \D	 | 	Any Non-digit character
# .	 | 	Any Character
# \.	 | 	Period (slash is an escape character)
# [abc]	 | 	Only a, b, or c
# [^abc]	 | 	Not a, b, nor c
# [a-z]	 | 	Characters a to z
# [0-9]	 | 	Numbers 0 to 9
# \w	 | 	Any Alphanumeric character
# \W	 | 	Any Non-alphanumeric character
# {m}	 | 	m Repetitions
# {m,n}	 | 	m to n Repetitions
# *	 | 	Zero or more repetitions
# +	 | 	One or more repetitions
# ?	 | 	Optional character
# \s	 | 	Any Whitespace
# \S	 | 	Any Non-whitespace character
# ^…$	 | 	Starts and ends
# (…)	 | 	Capture Group
# (a(bc))	 | 	Capture Sub-group
# (.*)	 | 	Capture all
# (abc&#124;def)	 | 	Matches abc or def
# 

# ## Use as a filter

# Let's begin by reading in a file containing a bunch of words from the [American National Corpus](http://www.anc.org/) that have a frequency of at least 9. Here's a sample of what this file looks like.
# 
#     word	lemma	pos	freq
#     the	the	DT	1081168
#     of	of	IN	539793
#     and	and	CC	466737
#     to	to	TO	448519
#     a	a	DT	406057
#     in	in	IN	360853
#     is	be	VBZ	192975
# 
# For those unfamiliar with language lingo, English lemmas are basically the word-stems, e.g., the lemma of *cars* is *car*; the lemma of *walking* is *walk*. pos stands for [*part of speech*](https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html).
# 
# Just to illustrate an alternate way of dealing with csv file, let's use the `csv` module:

# In[153]:


import csv

csvfile = open('datasets/ANC-written-count_over9.txt', 'r')
data = csv.DictReader(csvfile, delimiter='\t')


# `data` is a [DictReader](https://docs.python.org/2/library/csv.html#csv.DictReader) object which is kind of like a list of dictionaries of the kind we made when reading in trial files, except unlike a list we can't access a particular element, but have to iterate through it. The advantage of this is that we don't need to hold the entire dataset in memory at the same time (important for very large datasets, but not an issue in the present case).
# 
# Since memory is not an issue here, let's put all the unique words. We don't care about frequencies for this exercise.

# In[154]:


import re #import the python regexp module

words = set([row['word'] for row in data])
print "We have", len(words), "words"


# Now let's use some regular expressions starting with simple ones, and moving on to every slightly more complicated ones.

# Grab words beginning with *q*

# In[155]:


[curWord for curWord in words if re.findall('^q',curWord)]


# Grab all words begin with an *a* and end with an *i*

# In[156]:


[curWord for curWord in words if re.findall('^a\w+i$',curWord)]


# Grab all words that begin with an *a*, followed by 4-6 letters and and on an *i*

# In[157]:


[curWord for curWord in words if re.findall('^a\w{4,6}i$',curWord)]


# Grab words that start with a *l*, end on an *t*, and contain a *t* somewhere in the middle

# In[158]:


[curWord for curWord in words if re.findall('^b\w+t\w+t$',curWord)]


# Let's say we want to exclude words that end on two *t*s. 

# In[159]:


[curWord for curWord in words if re.findall('^b\w+t\w+[^tt]t$',curWord)]


# Let's get all the words containing the vowels a, e, i, o, in that order

# In[160]:


[curWord for curWord in words if re.findall('\w+a+\w+e+\w+i+\w+o+',curWord)]


# You know that saying [i before e except after c](https://en.wikipedia.org/wiki/I_before_E_except_after_C) (in which case it's i after e, like *receive*). Let's see how well this mnemonic holds up.

# Let's find out how many words there are that have *ie* vs. *ei* in them.
# 

# In[161]:


print "ie words:", len([curWord for curWord in words if re.findall('ie',curWord)])
print "ei words:", len([curWord for curWord in words if re.findall('ei',curWord)])


# Now let's check what happens when we check for a 'c' preceding ie/ei

# In[162]:


print "cie words:", len([curWord for curWord in words if re.findall('cie',curWord)])
print "cei words:", len([curWord for curWord in words if re.findall('cei',curWord)])


# There are actually *more* words that violate the mnemonic than those that obey it!
# What are these words?

# In[163]:


[curWord for curWord in words if re.findall('cie',curWord)]


# Here's a tricky one. Let's find words containing 4 *r*s (interspersed among other letters). One way to do this is to explicitly specify it... any character, r, any character, r.. etc. Like so..

# In[164]:


[curWord for curWord in words if re.findall('\w*r+\w*r+\w*r+\w*r+\w*',curWord)]


# There are two shortcomings to this approach. The first is that if we want 3 or 5 matches, we need to explicitly remove or add code rather than changing a single number-of-matches parameter. Another shortcoming is that hyphenated words are excluded. We can add hyphens by replacing `\w` with `[a-z\-]`, but that makes the expression even longer. Here's a better solution:

# In[165]:


[curWord for curWord in words if re.findall('([^r]*r[^r]*){4}$',curWord)]


# Let's unpack that. We are matching a [group](https://www.regular-expressions.info/refcapture.html) which is demarcated by parentheses. The group pattern is: not-an-r (0 or more times), an r, and then not-an-r (0 or more times). We want words that match this pattern exactly 4 times. That gives us all the words containing four *r*s and anything in between them (including nothing, hence *grrrr*)

# ## Use in place of conditionals
# 
# Let's say we want to check whether an entered word is *color* or the British *colour*. We can do this with a conditional (`if "color" or "colour"`), but we can also use regular expressions (which scale much better than conditionals). For example:

# In[166]:


re.findall('colou?r','The British like to colour their colors')


# Play around with this:

# In[167]:


variousWords = re.compile('[d|c][a|o][g|t]')
variousWords.match('cog').group()
variousWords.match('cag').group()


# Here are some more examples.

# In[168]:


#will match any numbers
anyNums = re.compile('[0-9]+')
anyNums.findall('There are 99 bottles of beer on the wall. 999....') #will return all matches
anyNums.search('There are 99 bottles of beer on the wall. 999....').group() #will return just the first occurrence

#two digit numbers from 00 to 59 or 80 to 89 
someNums = re.compile('[0-5][0-9]|[8][0-9]')
matches = [someNums.search(x).group() for x in 'It will match 54, 52, and 88, but not 7 or 92 or any of the letters'.split(' ') if someNums.search(x)]
matches

#We don’t need to compile regular expressions using re.compile. but it speeds things up when using the same rule over a large corpus.

emailRegExGrouped = re.compile('([\w.-]+)@([\w.-]+)')
#the parenthesis allow us to access groups -- the first group corresponds to the first matched part (before the @). The second group to the domain (e.g., wisc.edu(

emailRegExGrouped.search('g.lupyan@gmail.com').groups()
('g.lupyan', 'gmail.com')

emailRegExGrouped.findall('g.lupyan@gmail.com lupyan@wisc.edu')
#returns [('g.lupyan', 'gmail.com'), ('lupyan', 'wisc.edu')]

#to get all the domains:
[email[1] for email in emailRegExGrouped.findall('g.lupyan@gmail.com lupyan@wisc.edu')]
#returns ['gmail.com', 'wisc.edu']


# ## Search and replace
# 
# All good text editors allow you to use regular expressions in search and replace. 
# A simple usage case is searching for lines that begin or end with a certain character sequence. To find lines that begin with "ab", search for `^ab`. To find lines that end on `ies` search for `ies$`
# 
# <div class="alert alert-block alert-info">
# Make sure to enable regular-expression search by clicking on .* in Sublime text or checking the appropriate box (sometimes labeled Grep) in other text editors</div>
# 

# When using regular expressions in search/replace, it becomes useful to use matching groups. 
# 
# For example, suppose you want to replace the occurrences of the following strings, which occur at the start of each line:
# ```
# bdSubjCode_130
# badSbjCode_131
# baSubjCode_132
# badSubjCode_133
# badubjCode_134
# BadSubjCode_135
# ```
# with 
# 
# ```
# MYSUBJCODE_130
# MYSUBJCODE_131
# MYSUBJCODE_132
# MYSUBJCODE_133
# MYSUBJCODE_134
# MYSUBJCODE_135
# ```
# You *could* manually do search replaces for each one. But if you have a hundred of these, that gets tedious fast and is a recipe for errors.
# 
# Here's a much better solution. Simply search for:
# 
# `(^\w+_)([0-9]+)`
# 
# and replace with
# 
# `MYSUBJCODE_\2`
# 
# The \2 refers to the second group, i.e., the number

# Here's another example. Delete all the lines that start with some letters and end in 'ing':
# 
# Search:
# `(^\w+ing).*`
# Replace with: nothing
# 
# Now you can do another search and replace, searching for
# `\n+`
# and replacing with
# `\n`
# To get rid of multiple newlines that the first search/replace may have created.

# ## Renaming files

# Use the same logic to rename files. You can do this in python or by using GUI programs like [NameChanger](https://mrrsoftware.com/namechanger/) (Mac), or [Bulk Rename](http://www.bulkrenameutility.co.uk/Main_Intro.php) (PC). These programs allow you to do batch renaming of files using simple search/replace (e.g., replace `_` with `-` or through search/replace augmented by regular expressions.
# 