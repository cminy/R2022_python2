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

yt_body = new_driver.find_element(By.TAG_NAME, value='body')
# 스크롤 key값 활용: PageDown, PageUp, 방향기(위/아래)
for i in range(5):
    yt_body.send_keys(Keys.END)
    time.sleep(1.5)
    
# selenium을 이용해서 HTML문서를 변환한 후에는 반드시 브라우저를 종료해야 한다!
yt_html = bs(new_driver.page_source, 'lxml')
new_driver.close()

print ('>>>> start')
titleList = []
hrefList = []
for yt in yt_html.select('a#video-title'):
    title = yt.get('title')
    content_url = 'https://www.youtube.com'+yt.get('href')

    titleList.append(title)
    hrefList.append(content_url)

df_yt = pd.DataFrame({
    'yt_title' : titleList,
    'yt_href' : hrefList
})

print(df_yt)
print('>>>> end')
