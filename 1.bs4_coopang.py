import requests
import re
from bs4 import BeautifulSoup

headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36", "Accept-Language" : "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"}
for i in range(1,4):
    print("\n{}번째 페이지".format(i))
    url = "https://www.coupang.com/np/search?q=%EC%84%A0%ED%92%8D%EA%B8%B0&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=1=9&backgroundColor=".format(i)

    res =  requests.get(url, headers=headers)
    res.raise_for_status()

    soup = BeautifulSoup(res.text , "lxml")

    # 쿠팡 선풍기 목록에서 광고 상품 제외한 5만원 이상 목록 1-3페이지까지 가져와보기

    items = soup.find_all("li", attrs={"class":re.compile("^search-product")})
    
    for item in items :
        name = item.find("div",attrs = {"class":"name"}).get_text().strip()
        price = item.find("strong", attrs={"class":"price-value"}).get_text().replace(",","")
        if int(price)<= 50000:
            continue
        print(name , price)
