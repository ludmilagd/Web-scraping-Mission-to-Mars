#!/usr/bin/env python
# coding: utf-8

# In[14]:


# Dependencies
from bs4 import BeautifulSoup
import requests
import os
from splinter import Browser
from splinter.exceptions import ElementDoesNotExist


# In[15]:


executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)


# In[16]:


# Source of Information
url="https://mars.nasa.gov/news/"
browser.visit(url)


# In[17]:


# Create Beautiful soup parser
html= browser.html
soup= BeautifulSoup(html, 'html.parser')


# In[18]:


#Navigate to the container
outercontainer= soup.find('div', class_='list_text')
outercontainer


# In[19]:


# Go to next level- body and get description 
body = outercontainer.find('div', class_='article_teaser_body').text
body


# In[20]:


#Navigate to title and extract text only
titles = outercontainer.find('div', class_='content_title').text
titles


# In[21]:


# Go to list- example of how to get all the info from the list
lista= soup.find('ul', class_='item_list')


# In[22]:


# Visit Nasa page to get feature image
url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)


# In[23]:


# Tell Browsert to navigate to the next page by clicking FULL IMAGE
browser.click_link_by_id('full_image')


# In[24]:


# Click to "More Info" button
browser.click_link_by_partial_text('more info')


# In[25]:


# Use beautiful soup to extract information 
html= browser.html
soup= BeautifulSoup(html, 'html.parser')


# In[26]:


# Find fugre container
feature_image= soup.find('figure', class_='lede')
feature_image


# In[27]:


# Obtain reference and create complete link to feature image
feature_image_= feature_image.find('a')['href']
feature_image_= url+feature_image_
feature_image_        


# In[28]:


# Visit webpage to extract Hemisphere pics
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)


# In[29]:


html= browser.html
soup= BeautifulSoup(html, 'html.parser')

hemiphere_list=[]

hemis = browser.find_by_tag('h3')

for i in range(len(hemis)):
    hemi_dict={}
    
    browser.find_by_css('h3')[i].click()
    
#     image=soup.find('div', class_='downloads')
#     hemi_dict['image']= image.find('a')['href']
    image = browser.links.find_by_text('Sample').first
    hemi_dict['images']= image['href']
    
    hemi_dict['title']=browser.find_by_css('h2').text
    
    hemiphere_list.append(hemi_dict)
    browser.back()

    
    
    
    


# In[30]:


print(hemiphere_list)


# In[ ]:




