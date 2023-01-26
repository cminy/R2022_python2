# DESCRIPTION : Python 웹크롤링 : 연관검색어 추출
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs
import pandas as pd
import time

# set driver
def set_chrome_driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    return driver

new_driver = set_chrome_driver()
yt_url = "https://youtube.com/playlist?list=FLN3QmzfUO5BvjP5qVpRQfjg"
new_driver.get(yt_url)

yts = new_driver.find_elements(By.CSS_SELECTOR, value='a#video-title')
titleList = []
hrefList = []

print ('>>>> start')
for yt in yts:
    titleList.append(yt.get_attribute('title'))
    hrefList.append(yt.get_attribute('href'))
    time.sleep(1)

new_driver.close()

df_yt = pd.DataFrame({
    'yt_title' : titleList,
    'yt_href' : hrefList
})

df_yt.head()
print('>>>> end')
