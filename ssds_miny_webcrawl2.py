# DESCRIPTION : Python 웹크롤링 : 연관검색어 추출
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs

import openpyxl
import pandas as pd
import time

# set driver
def set_chrome_driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    return driver

# create and save 
update_date = time.strftime('%Y%m%d', time.localtime())
def create_xls(pl, pl_html):
    # df.to_excel('./youtube_playlist', sheet_name=, index=False)
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = pl
    # 시트에 내용 추가
    ws.append(['#', 'title', 'url'])
    # video list 읽어와서 추가
    for i, yt in enumerate(pl_html.select('a#video-title')):
        title = yt.get('title')
        content_url = 'https://www.youtube.com'+yt.get('href')

        ws.append([i+1, title, content_url])

        time.sleep(0.5)

    # 엑셀 저장
    wb.save(f'miny_youtube_{update_date}.xlsx')
    print('[!] youtube playlist 저장 완료')


# create new driver
new_driver = set_chrome_driver()
yt_url = "https://youtube.com/playlist?list=FLN3QmzfUO5BvjP5qVpRQfjg"
new_driver.get(yt_url)
new_driver.maximize_window()

# 페이지 스크롤
time.sleep(2)
new_driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

# playlist title 가져오기
yts_title = new_driver.find_element(By.XPATH, '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-playlist-header-renderer/div/div[2]/div[1]/div/yt-dynamic-sizing-formatted-string/div/yt-formatted-string')
pl_title = yts_title.text

# source lxml로 가져오기
yt_html = bs(new_driver.page_source, 'lxml')
new_driver.close()

create_xls(pl_title, yt_html)
