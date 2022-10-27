#!/usr/bin/env python
# coding: utf-8

# # Webscraping with Beautiful Soup
# 
# In this notebook, we'll see how to use the [Beautiful Soup](https://www.youtube.com/watch?v=FWxFsJUlBbw) library for some psychology-relevant webscraping tasks. 

# ## Get heading names in a Wikipedia article
# 
# Let's begin by automatically grabbing The Simpsons character names from the *Simpson Family* [Wikipedia page](https://en.wikipedia.org/wiki/Simpson_family). Looking at the wiki article, we see that the character names are part of a bulleted list (produced by the html `<ul>` tag. Furthermore, they're bolded. Let's give that a try.

# In[44]:


from bs4 import BeautifulSoup
import requests

url = "https://en.wikipedia.org/wiki/Simpson_family"
r = requests.get(url)
soup = BeautifulSoup(r.content)

for headline in soup('span', {'class' : 'mw-headline'}):
    print headline.text
    topics = headline.find_next('ul').find_all('b') #ul is bulletpoints; b is bold
    for topic in topics:
        print '*', topic.text       



# There are some false alarms, but this generally works! You might wonder whether this is too much trouble to go through just to get the Simpsons headings. But of course the identical code will work on pretty much *any* wiki article. And that's really the point.

# ## Scrape images from a Google Image Search
# 
# Wouldn't it be neat if we could automatically download the images returned from a [Google Image Query](https://www.google.com/search?tbm=isch&sa=1&ei=4x3hWtaILpCJjwTKy7xA&q=biggest+dog&oq=biggest+dog). 
# Here's one way to do it ([props to this repo](https://gist.github.com/genekogan/ebd77196e4bf0705db51f86431099e57)).

# ### Barebones version of Google image scraping

# In[48]:


from bs4 import BeautifulSoup
import requests
#import re
import urllib2
import os
#import sys
import json

def get_soup(url,header):
	return BeautifulSoup(urllib2.urlopen(urllib2.Request(url,headers=header)),'html.parser')

query = "cats"
save_directory = query
max_images = 12

url="https://www.google.com/search?q="+query+"&source=lnms&tbm=isch"
header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
soup = get_soup(url,header)

try:
    os.stat(save_directory)
except:
    os.mkdir(save_directory)


ActualImages=[]# contains the link for Large original images, type of  image
for a in soup.find_all("div",{"class":"rg_meta"}):
    link , Type =json.loads(a.text)["ou"]  ,json.loads(a.text)["ity"]
    ActualImages.append((link,Type))
for i , (img , Type) in enumerate( ActualImages[0:max_images]):
    try:
        print 'retrieving image', i
        req = urllib2.Request(img, headers={'User-Agent' : header})
        raw_img = urllib2.urlopen(req).read()
        if len(Type)==0:
            f = open(os.path.join(save_directory , "img" + "_"+ str(i)+".jpg"), 'wb')
        else :
            f = open(os.path.join(save_directory , "img" + "_"+ str(i)+"."+Type), 'wb')
        f.write(raw_img)
        f.close()
    except Exception as e:
        print "could not load : "+img
        print e


# ### Google image scraping with some bells and whistles
# 
# The code above does the job, but can be improved considerably. First, we can refactor it, dividing up the various calls into separate functions. Second, we can make the query, directory, and number of images desired be command-line arguments. The code below (slightly adapted from a post by [*hadsed*](https://gist.github.com/hadsed) [here](https://gist.github.com/genekogan/ebd77196e4bf0705db51f86431099e57). 
# 
# Among other things, the code demonstrates the use of the argument-parsing [`argparse`](https://docs.python.org/2.7/library/argparse.html) package which allows you to specify options at the terminal that your python program can see (e.g., the query string, number of images, etc). This code also demonstrates logging.

# In[ ]:


import argparse
import json
import itertools
import logging
import re
import os
import sys
from urllib2 import urlopen, Request
from bs4 import BeautifulSoup


def configure_logging():
	logger = logging.getLogger()
	logger.setLevel(logging.DEBUG)
	handler = logging.StreamHandler()
	handler.setFormatter(
		logging.Formatter('[%(asctime)s %(levelname)s %(module)s]: %(message)s'))
	logger.addHandler(handler)
	return logger

logger = configure_logging()

REQUEST_HEADER = { #this can be changed to simulate different types of browsers
	'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}


def get_soup(url, header):
	response = urlopen(Request(url, headers=header))
	return BeautifulSoup(response, 'html.parser')

def get_query_url(query):
	return "https://www.google.com/search?q=%s&source=lnms&tbm=isch" % query

def extract_images_from_soup(soup):
	image_elements = soup.find_all("div", {"class": "rg_meta"})
	metadata_dicts = (json.loads(e.text) for e in image_elements)
	link_type_records = ((d["ou"], d["ity"]) for d in metadata_dicts)
	return link_type_records

def extract_images(query, num_images):
	url = get_query_url(query)
	logger.info("Souping")
	soup = get_soup(url, REQUEST_HEADER)
	logger.info("Extracting image urls")
	link_type_records = extract_images_from_soup(soup)
	return itertools.islice(link_type_records, num_images)

def get_raw_image(url):
	req = Request(url, headers=REQUEST_HEADER)
	resp = urlopen(req)
	return resp.read()

def save_image(raw_image, image_type, file_name, save_directory):
	extension = image_type if image_type else 'jpg'
	save_path = os.path.join(save_directory, file_name+ "." + extension)
	print 'image_type is', image_type, 'path is', save_path
	with open(save_path, 'wb') as image_file:
		image_file.write(raw_image)

def download_images_to_dir(query, images, save_directory, num_images):
	for i, (url, image_type) in enumerate(images):
		try:
			logger.info("Making request (%d/%d): %s", i, num_images, url)
			raw_image = get_raw_image(url)
			file_name = query.replace('+','_')+'_'+str(i)
			save_image(raw_image, image_type, file_name, save_directory)
		except Exception as e:
			logger.exception(e)

def run(query, save_directory, num_images=100):
	query = '+'.join(query.split())
	logger.info("Extracting image links")
	images = extract_images(query, num_images)
	logger.info("Downloading images")
	try:
		os.stat(save_directory)
	except:
		os.mkdir(save_directory)
	download_images_to_dir(query, images, save_directory, num_images)
	logger.info("Finished")

def main():
	parser = argparse.ArgumentParser(description='Scrape Google images')
	parser.add_argument('-s', '--search', default='bananas', type=str, help='search term or phrase')
	parser.add_argument('-n', '--num_images', default=10, type=int, help='num images to save')
	parser.add_argument('-d', '--directory', default='.', type=str, help='save directory')
	args = parser.parse_args()
	if args.directory=='.':
		args.directory = args.search.replace(' ','_') #use query string as directory
	print args.search, args.directory
	run(args.search, args.directory, args.num_images)

if __name__ == '__main__':
	main()


# Downloading more than 100 images requires simulating a scrolling action with a web-browser. This can be done by using Selenium. You'll need to [download it](https://www.seleniumhq.org/), and also download [Chromedriver](https://sites.google.com/a/chromium.org/chromedriver/downloads). Then incorporate the code provided by [*aaronsherwood*](https://gist.github.com/genekogan/ebd77196e4bf0705db51f86431099e57) into the code above.

# ## Other useful resources: Scraping Reddit, Online News
# 
# There's really enormous infrastructure for web scraping, e.g., [PRAW](http://www.storybench.org/how-to-scrape-reddit-with-python/) for scraping reddit, [newspaper](https://github.com/codelucas/newspaper) for scraping online news. See [here](http://bdewilde.github.io/blog/blogger/2012/11/26/web-scraping-and-html-parsing-2/) and [here](https://opensourceforu.com/2016/07/22843/) for more examples. A really creative example of scraping is [this blog post by Erik Bern](https://erikbern.com/2017/02/01/language-pitch.html) which bulk downloads pronunciations of words in various languages to examine whether there are consistent differences in pitch (fundamental frequency) between languages (Hint, yes. Finnish is Lowwww).
# 
# 

# In[ ]:




