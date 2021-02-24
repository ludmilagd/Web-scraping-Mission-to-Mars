#!/usr/bin/env python
# coding: utf-8


# Dependencies
from bs4 import BeautifulSoup
import requests
import os
import re
import pandas as pd
from splinter import Browser
from splinter.exceptions import ElementDoesNotExist


executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)


# Source of Information
url="https://mars.nasa.gov/news/"
browser.visit(url)


# Create Beautiful soup parser
html= browser.html
soup= BeautifulSoup(html, 'html.parser')

#Navigate to the container
outercontainer= soup.find('div', class_='list_text')
outercontainer

# Go to next level- body and get description 
body = outercontainer.find('div', class_='article_teaser_body').text
body



#Navigate to title and extract text only
titles = outercontainer.find('div', class_='content_title').text
titles



# Go to list- example of how to get all the info from the list
lista= soup.find('ul', class_='item_list')
lista


# Visit Nasa page to get feature image
url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)


html= browser.html
soup= BeautifulSoup(html, 'html.parser')


outercontainer2= soup.find('div', class_='SearchResultCard')
outercontainer2


text=[]

for a in outercontainer2.find_all('a', href=True): 
    if a.text: 
        text.append(a['href'])
first_text=text[0]   
first_text


browser.click_link_by_partial_href(first_text)


browser.click_link_by_partial_text('Download JPG')



# Use beautiful soup to extract information 
html= browser.html
soup= BeautifulSoup(html, 'html.parser')



# Get the link to the image source
feature_image_img = soup.find('img')['src']
feature_image_img



# Obtain facts about Mars
url = 'https://space-facts.com/mars/'
browser.visit(url)



html= browser.html
soup= BeautifulSoup(html, 'html.parser')


table = soup.find('table', id="tablepress-p-mars")
print (table)



# Use Pandas to convert the data to a HTML table string
tables = pd.read_html(url)
table_df=tables[0]
table_df



table_df.columns=["Description","Value"]
table_df=table_df.set_index("Description")
table_df



table_html= table_df.to_html()
table_html



# Visit webpage to extract Hemisphere pics
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)



html= browser.html
soup= BeautifulSoup(html, 'html.parser')

hemiphere_list=[]

hemis = browser.find_by_tag('h3')

for i in range(len(hemis)):
    hemi_dict={}
    
    browser.find_by_css('h3')[i].click()
    
    image = browser.links.find_by_text('Sample').first
    hemi_dict['images']= image['href']
    
    hemi_dict['title']=browser.find_by_css('h2').text
    
    hemiphere_list.append(hemi_dict)
    browser.back()

    
    
    
    


print(hemiphere_list)








