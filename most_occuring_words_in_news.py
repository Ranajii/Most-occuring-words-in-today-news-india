# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 13:31:22 2018

@author: vishal
"""
from selenium import webdriver
# Using Chrome to access web
driver = webdriver.Chrome(r"C:\Users\visha\chromedriver")
driver.get('https://news.google.com/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNRE55YXpBU0FtVnVLQUFQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen')
headlines = []

for i in range(1,30):
    link = '//*[@id="yDmH0d"]/c-wiz/div/c-wiz/div/div[2]/div/main/c-wiz/div[1]/div['+str(i)+']/div/article/div[1]/div/h3/a/span'
    head = driver.find_element_by_xpath(link)
    k = head.text
    er = k.split()
    headlines = headlines + er
     
l = [i.lower() for i in headlines]

'removing STOP words'
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english')) #some words are just plain useless, and are filler words

SW = []
for k in l:
    if k not in stop_words:
        SW.append(k)
from nltk.probability import FreqDist
fdist = FreqDist(SW)
fdist.plot(5,cumulative=True) #this will plot the frquency plot for 10 most occuring words in the URL
      
  









