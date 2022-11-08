#!/usr/bin/env python
# coding: utf-8

# # Intro to NLTK
# 
# A whirlwind tour of Python's natural language toolkit (NLTK).
# 
# We'll start by importing a few libraries and opening up a sample text file: Jane Austen's Pride and Prejudice.
# 
# If you get import errors, use `pip` to install the missing package (`pip install package_name`).

# In[18]:


import nltk
import urllib
from nltk.corpus import gutenberg
from nltk.text import Text

pride_prejudice = urllib.request.urlopen("https://psych750.github.io/data/pride_prejudice.txt").read().decode()


# In[19]:


print(pride_prejudice[0:100])


# Now let's tokenize and lowercase the text.

# In[20]:



pride_prejudice_raw_tokens = nltk.word_tokenize(pride_prejudice)
print( "Original tokens (first 100):")
print(pride_prejudice_raw_tokens[:100])

#lowercase 
pride_prejudice_raw_tokens = [token.lower() for token in pride_prejudice_raw_tokens]
print( "Lowercased tokens (first 100):")
print( pride_prejudice_raw_tokens[:100])


# Now let's remove punctuation

# In[16]:


pride_prejudice_clean_tokens = [token.lower() for token in pride_prejudice_raw_tokens if token.isalpha()]
print( "Clean yokens (first 100). Now without punctuation:")
print(pride_prejudice_clean_tokens[:100])


# ## Frequency Distributions
# 
# The first thing we'll do is build a frequency distribution using `nltk.FreqDist()`
# 

# In[17]:


pride_prejudice_freq_dist = nltk.FreqDist(pride_prejudice_clean_tokens)


# `pride_prejudice_freq_dist` is formatted as a Python dictionary -- nothing special here, but the nice thing is that FreqDist implements various methods we can use to compute and quickly plot various properties of the text.

# In[21]:


pride_prejudice_freq_dist


# How many tokens are there?
# 
# `.N()` gives us the total number of words -- the tokens. (N standa for Number)
# 
# `.B()` gives us the number of unique words -- the types. (B stands for Bins)
# 

# In[58]:


print ("Token count:", pride_prejudice_freq_dist.N())
print ("Type count:", pride_prejudice_freq_dist.B())

# We can get the frequency of a word by treating the FreqDist as a dictionary and looking up a word
print ("Occurences of 'darcy':", pride_prejudice_freq_dist['darcy'])
print ("Occurences of 'love':", pride_prejudice_freq_dist['love'])
print ("Occurences of 'money':", pride_prejudice_freq_dist['money'])

# Find out how many tokens end in -ed
# We just ask for the length of the list of tokens
# that end in -ed
print( "Tokens that end in -ed:", len([token for token in pride_prejudice_clean_tokens if token.endswith('ed')]))

# If we want the number of types, we can use the keys of the
# FreqDist
print ("Types that end in -ed:", len([word_type for word_type in pride_prejudice_freq_dist if word_type.endswith('ed')]))

pride_prejudice_freq_dist.plot(30)


# ## Removing stop words
# 
# Stop words is jargon for very frequent words that tend to be not very informative as to the meaning of the text. For example, we can't learn much about an English text from knowing that it has the words "a", "the", and "to" in it...  These frequent words dominate frequency distributions and so are often removed as part of pre-processing. NLTK has a collection of stop-words for English (other languages too!)

# In[59]:


from nltk.corpus import stopwords
print(stopwords.words('english'))

#remove them
pride_prejudice_clean_tokens_no_stop_words = [word for word in pride_prejudice_clean_tokens if word not in stopwords.words('english')]


# Let's get the frequency distribution of the text without the stop words:
# 
# 

# In[60]:


pride_prejudice_clean_tokens_no_stop_words_fd =  nltk.FreqDist(pride_prejudice_clean_tokens_no_stop_words)
pride_prejudice_clean_tokens_no_stop_words_fd.plot(40)


# A handy method inside FreqDist is `most_common`:

# In[61]:


pride_prejudice_clean_tokens_no_stop_words_fd.most_common(10)


# ## Concordances
# 
# Concordances are the context in which a word is used. To calculate these, we can use NLTK's [Text module](https://www.nltk.org/api/nltk.text.html)

# In[25]:


print(Text(pride_prejudice_raw_tokens).concordance("picture"))


# ## Dispersion plots
# 
# Another neat method inside the `Text` class is a dispersion plot.

# In[68]:


Text(pride_prejudice_raw_tokens).dispersion_plot(['love', 'money', 'marriage'])


# ## N-grams and their frequencies
# 
# N-grams are word sequences on n-length. For example, 2-grams (typically called bigrams) are all the combinations of 2 words that occur sequentially in a text. 3-grams (trigrams) are all the 3-word combinations. To compute them, use nltk's bigram and trigram modules
# 

# In[35]:


import nltk.collocations as collocations
from nltk import FreqDist, bigrams, trigrams

#compute bigrams and their frequencies
bigram_freqs = nltk.FreqDist(nltk.bigrams(pride_prejudice_clean_tokens_no_stop_words))

bigram_freqs.most_common(20)



# We can also look at trigrams, but with just a single book this is not going to be very effective. Notice that even the most frequent trigrams aren't observed very often!
# 
# ```{note}
# To compute n-grams beyond 3, you can use nltk.ngrams, but for small corpora like those of a book (or even a 100 books), you'll find that the vast majority will only occur once, and so there's nothing to work with... 
# ``` 

# In[63]:



trigram_freqs = nltk.FreqDist(nltk.trigrams(pride_prejudice_clean_tokens_no_stop_words))
print(trigram_freqs.most_common(20))



# Let's look at the most frequent trigrams in a slightly larger corpus: NLTK's Project Gutenberg. Project Gutenberg contains the text of many out-of-copyright books and you can download all of them. NLTK bundles a handful: 

# In[37]:


nltk.download('gutenberg')
print(nltk.corpus.gutenberg.fileids())


# Any idea what the most common trigrams are if we combine all of these books into a single corpus?

# In[64]:



some_books = nltk.corpus.gutenberg.words()

some_books_clean = [token.lower() for token in some_books if token.isalpha()]
trigram_freqs = nltk.FreqDist(nltk.trigrams(some_books_clean))
print(trigram_freqs.most_common(30))


# ## Collocations
# 
# Bigrams and trigrams are simply all the pairs (and triplets) of words that occur sequentially. The most frequent ones are... more frequent, but part of the reason they're more frequent is that their *individual* words are more frequent. 
# 
# Here's an example of getting collocations -- combinations of words that are unlikely to appear together, but do (and so are important). 
# (more and more complex examples [here](https://www.nltk.org/howto/collocations.html))

# In[38]:


Text(pride_prejudice_clean_tokens_no_stop_words).collocation_list()


# Let's compare it to the collocations from Alice in Wonderland. We'll tokenize in a slightly different way here, as an added example.

# In[39]:


alice_raw = nltk.corpus.gutenberg.raw('carroll-alice.txt')

alice_tokenizer = nltk.tokenize.RegexpTokenizer('\w+') #can put in whatever regexp you want here
alice_tokenized = alice_tokenizer.tokenize(alice_raw)
alice_tokenized = [token.lower() for token in alice_tokenized if token not in stopwords.words('english')]

alice_clean =  [token.lower() for token in alice_tokenized if token not in stopwords.words('english')]

Text(alice_clean).collocation_list()


# If we compare the collocations to the most common bigrams, we see that the collocations are more informative.

# In[40]:


nltk.FreqDist(nltk.bigrams(alice_clean)).most_common(30)


# ## Lemmatization
# 
# A lemma is the base form of a word. It is what would typically be used as an entry in an English dictionary. Lemmatization refers to grouping together words that are inflectional variants of the same lemma: (go,went), (read, reading, reads), (cat, cats), etc..  

# In[55]:


from nltk import WordNetLemmatizer

lemmatizer = nltk.WordNetLemmatizer()

print("cats :", lemmatizer.lemmatize("cats"))
print("corpora :", lemmatizer.lemmatize("corpora"))
print("says :", lemmatizer.lemmatize("says"))
print("went :", lemmatizer.lemmatize("went"))
print("leaves :", lemmatizer.lemmatize("leaves"))


# Ok, so we can see a few problems here. First, went stayed as went. And "leaves" was matched to "leaf" whereas I was thinking of "leaves" as in a person leaves the room. The reason is that the WordNetLemmatizer is stupid. It defaults to treating words as nouns (with some exceptions). We can, however, pass it a part of speech as an argument:
# 
# ```{note}
# For the wordnet lemmatizer, the possible parts of speech are: n for noun, v for verb, a for adjective, r for adverb, s for satellite adjective
# ```

# In[56]:



print("went :", lemmatizer.lemmatize("went",pos="v"))
print("leaves :", lemmatizer.lemmatize("leaves",pos="v"))
print("redder :", lemmatizer.lemmatize("redder",pos="a"))


# What use is lemmatization if we have to manually tell it what part of speech something is? Well, we don't have to do it *manually*. If we're processing words in context, we can use NLTK's [automatic Part of Speech Tagging](https://www.nltk.org/book/ch05.html) instead!  
