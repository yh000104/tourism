import sys
import os
import pandas as pd
import numpy as np
import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from tqdm import tqdm_notebook

#크롬 드라이버 실행 및 홈페이지 열기
path = "C:\김용훈\기타\대학\정보보안응용\work\chromedriber.exe"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://korean.visitkorea.or.kr/list/ms_list.do?areacode=All')
time.sleep(2)

#데이터 수집
travel_url_list = []
travel_name_list = []
travel_price_list = []
travel_site_list = []
travel_point_list = []

page = 5

#관광지 이름

travel_name_raw = driver.find_elements_by_css_selector('.travel_name_ko.ng-binding')

travel_name_list = []

for travel_name in travel_name_raw:
    i = travel_name.txt
    travel_name_list.append(i)
time.sleep(1)

#관광지 가격

price_raw = driver.find_elements_by_css_selector('.min_price')

price_list = []

for price in price_raw:
    i = price.text.replace('원', '').replace(',', ''). replace('~','')
    price_list.append(i)

price_list = [x for x in price_list if not x =='']
time.sleep(1)

#관광지 id

travel_ids = driver.find_element_by_css_selectior('.lst_travel > li')

travel_id_list = []

for travel_id in travel_ids:
    travel = travel_id.get_attribute('id')
    travel_id_list.append(travel)
time.sleep(1)

print(len(travel_name_list), len(price_list),len(travel_id_list))