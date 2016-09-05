#!/usr/bin/python

from pyquery import PyQuery as pq
from random import randint
import webbrowser

#toDo: only get articles that you did not read already

links = []

d = pq(url='https://en.wikipedia.org/wiki/Wikipedia:Unusual_articles')

#print(d.text())

#print d('.wikitable td b a')

#gets all links to articles, like:
#'/wiki/Michael_Malloy'
for link in d('.wikitable td b a'):
	links.append(link.attrib['href'])
	#print link.attrib['href']

articleNumber = randint(0, len(links))

txt = 'https://en.wikipedia.org' + links[articleNumber]

print txt