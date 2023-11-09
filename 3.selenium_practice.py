import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import re

# 네이버에 접속해서 쇼핑 탭 클릭 후 선풍기 검색하여 선풍기 목록 랭킹 순으로 가져오기!

browser = webdriver.Chrome()
browser.maximize_window()
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36", "Accept-Language" : "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"}
url = "http://naver.com"
res =requests.get(url, headers=headers)
res.raise_for_status()
browser.get(url)
time.sleep(2)

browser.find_element(By.LINK_TEXT, "쇼핑").click()    #네이버 쇼핑 클릭
time.sleep(5)
browser.switch_to.window(browser.window_handles[-1])    #최근 열린 창으로 전환
elem = browser.find_element(By.CLASS_NAME, "_searchInput_search_text_3CUDs")
elem.send_keys("선풍기") #선풍기 검색
elem.send_keys(Keys.ENTER)
time.sleep(5)
 
prev_height = browser.execute_script("return document.body.scrollHeight") #창 세로 해상도 최대로 내리기

while True:
    browser.execute_script("window.scrollTo(0 , document.body.scrollHeight)")
    
    time.sleep(2)
    
    curr_height = browser.execute_script("return document.body.scrollHeight")
    
    if curr_height == prev_height:
        break
    
    prev_height = curr_height
    
soup = BeautifulSoup(browser.page_source , "lxml") #페이지 소스 가져오기

items = soup.find_all("div" , attrs={"class" : "product_item__MDtDF"}) 

for item in items:
    name = item.find("a",attrs={"class" : re.compile("product_link")}).get_text() #상품 이름과 가격 가져오기
    price = item.find("span",attrs={"class" : "price_num__S2p_v"}).get_text()
    print(name,price)