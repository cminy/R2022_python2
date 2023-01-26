# DESCRIPTION : Python 웹크롤링 : 연관검색어 추출
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# import string
# en_list = [e for e in string.ascii_lowercase]
# letters = kor_list + en_list

# set driver
def set_chrome_driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    return driver

new_driver = set_chrome_driver()
yt_url = "https://youtu.be/mnpQsM-tqQU"
new_driver.get(yt_url)

yt = new_driver.find_element(By.CSS_SELECTOR, value='a#video-title')
print(yt.get_attribute('title'), yt.get_attribute('href'), sep='----')


# infos = miny_drive.find_elements(By.CSS_SELECTOR, "div#dismissible")
# infos = miny_drive.find_elements(By.CSS_SELECTOR, value='a#video-title')
# print ('-------------',infos)
# for info in infos:
#     title = info.text
#     link = info.get_attribute('href')
#     print(title, link)
