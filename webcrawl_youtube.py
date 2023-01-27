# DESCRIPTION : Python 웹크롤링 : 유튜브 플레이리스트 추출
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs
import pandas as pd
import time
import os
import re

# set driver
def set_chrome_driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    return driver

# make url
def channel_name(ch):
    while True:
        if re.findall(r'@[a-z]+', ch) != []:
            print("@를 제외하고 채널명만 입력하세요.")
        elif '/' in ch:
            print("채널명을 올바르게 입력해주세요.")
        else:
            check_input = input(f"입력한 채널명이  {ch}  맞습니까? Y/N: ")
            if check_input.upper() == 'Y':
                url = f"https://www.youtube.com/@{ch}/playlists"
                break
    return url


# page scroller
def scroll_webpage(driver):
    heightPre = driver.execute_script("return document.documentElement.scrollHeight")
    while True:
        driver.execute_script(
            "window.scrollTo(0, document.documentElement.scrollHeight);")
        time.sleep(1)  # SCROLL DELAY
        heightCurr = driver.execute_script(
            "return document.documentElement.scrollHeight")

        if heightCurr == heightPre:
            print(">>> scroll 마지막까지 완료")
            return False

        return True

# crawling youtube
def crawl_yt(pls_title, yt_html):
    print(f'>>> playlist {pls_title} crawling >>>')
    title_list = []
    url_list = []
    for i, yt in enumerate(yt_html.select('a#video-title')[len(miny_plays):]):
        title = yt.get('title')
        content_url = 'https://www.youtube.com'+yt.get('href')

        title_list.append(title)
        url_list.append(content_url)

        time.sleep(0.5)

    df = pd.DataFrame({
        'yt_title': title_list,
        'url' : url_list
    })

    save_xls(pls_title, df)

# create and save xls file
def save_xls(pl, df):
    # sheet_name : The name does not contain any of the following characters:  :  \  /  ?  *  [  or  ]
    check = re.compile('[\\,/,?,*,[,\]]')
    result = check.findall(pl)
    if len(result) > 0: 
        for c in result:
            pl = pl.replace(c, '')

    update_date = time.strftime('%Y%m%d', time.localtime())

    if not os.path.exists(f'./{channel}_ytplaylist_{update_date}.xlsx'):
        with pd.ExcelWriter(f'./{channel}_ytplaylist_{update_date}.xlsx', mode = 'w', engine='openpyxl') as writer:
            df.to_excel(writer, sheet_name=pl, index=False)
    else:
        with pd.ExcelWriter(f'./{channel}_ytplaylist_{update_date}.xlsx', mode = 'a', engine='openpyxl') as writer:
            df.to_excel(writer, sheet_name=pl, index=False)

    print(f'>>> [!] youtube playlist - < {pl} > 저장 완료')
    print('-'*50)

# start program - create new driver
home_driver = set_chrome_driver()
while True:
    channel = input("탐색할 유튜브 채널이름을 입력하세요: ")
    yt_url = channel_name(channel)
    home_driver.get(yt_url)
    if "404" in home_driver.title:
        print(f'[!] 입력한 url : {yt_url} 이 잘못되었습니다. 다시 입력해 주세요')
    else:
        announce = ' ' + channel + ' 의 playlists 탐색 시작 '
        print('{:-^50}'.format(announce))
        break

time.sleep(5)
scroll_webpage(home_driver)

# playlists 가져오기
miny_plays = home_driver.find_elements(By.CSS_SELECTOR, 'a#video-title')
print(f'>>> 총 {len(miny_plays)}개의 playlists가 있습니다. ')
for i, pls in enumerate(miny_plays):
    pls_title = pls.get_attribute('title')
    time.sleep(2)

    # playlist 접근
    print(f'>>> {i+1}번째 playlist {pls_title} 접근 시작')
    test = home_driver.find_elements(By.CSS_SELECTOR, '#view-more > a')
    test[i].click()

    # 페이지가 열릴때까지 기다린다.
    home_driver.implicitly_wait(5)

    # page source를 html로 가져오기
    time.sleep(3)
    scroll_webpage(home_driver)
    yt_html = bs(home_driver.page_source, 'lxml')

    # playlist 내 video 크롤링 후 이전페이지로 이동
    crawl_yt(pls_title, yt_html)
    home_driver.back()

    # 페이지가 열릴때까지 기다린다.
    home_driver.implicitly_wait(10)

# close
print('[!] playlist 저장을 종료합니다.')
home_driver.quit()
