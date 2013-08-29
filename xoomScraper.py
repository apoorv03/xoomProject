import urllib2
import re
import html5lib
from bs4 import BeautifulSoup
# from BeautifulSoup import BeautifulSoup
# or if you're using BeautifulSoup4:
# from bs4 import BeautifulSoup

soup = BeautifulSoup(urllib2.urlopen('https://www.xoom.com/india').read())
origVal = BeautifulSoup(urllib2.urlopen('http://finance.yahoo.com/q?s=USDINR=X').read())

h = soup('em', {'class': 'fx-rate'})[0]

oval = origVal('span', {'id': 'yfs_l10_usdinr=x'})[0]

print h.string[8:15], ", ", oval.string, ", ", float(oval.string) - float(h.string[8:15]) 
