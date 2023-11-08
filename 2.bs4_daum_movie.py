import requests
from bs4 import BeautifulSoup

for year in range(2017,2023):
    headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"}
    url = "https://search.daum.net/search?w=tot&q={}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR".format(year)
    print(year)
    res = requests.get(url, headers=headers)
    res.raise_for_status()

    soup = BeautifulSoup(res.text,"lxml")

    # 다음에서 2017 - 2022년영화 순위 별 포스터 가져와보기

    images = soup.find_all("img", attrs= {"class" : "thumb_img"})

    for idx, image in enumerate(images):
        image = image["src"]
        image_res = requests.get(image)
        image_res.raise_for_status()
        
        with open("movie{}_{}.jpg".format(year,idx+1), "wb") as f:
            f.write(image_res.content)
            
        if idx >= 4:
            break