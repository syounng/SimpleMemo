import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.imdb.com/chart/top/?ref_=nv_mv_250', headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

# 제목, 개봉 연도, 상영 시간, 영상물 등급 가져오기
movies = soup.select('#__next > main > div > div.ipc-page-content-container.ipc-page-content-container--center > section > div > div.ipc-page-grid.ipc-page-grid--bias-left > div > ul > li')

# 방법 1
for movie in movies:
    title = movie.select_one('a > h3').text
    
    elements = movie.select('.cli-title-metadata-item')
    year = elements[0].text
    time = elements[1].text
    rank = elements[2].text
    
    print(title)
    print(year)
    print(time)
    print(rank)

print('-------')

# 방법 2
for movie in movies:
    title = movie.select_one('a > h3').text
    
    year = movie.select_one('.cli-title-metadata-item:nth-child(1)').text
    time = movie.select_one('.cli-title-metadata-item:nth-child(2)').text
    rank = movie.select_one('.cli-title-metadata-item:nth-child(3)').text
    
    print(title)
    print(year)
    print(time)
    print(rank)

