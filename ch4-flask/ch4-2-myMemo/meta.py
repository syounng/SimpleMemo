import requests
from bs4 import BeautifulSoup

url = 'https://platum.kr/archives/120958'

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(url,headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

# 여기에 코딩을 해서 meta tag를 먼저 가져와보겠습니다.
# select_one을 사용해서 meta tag를 가져오기
og_image = soup.select_one('meta[property="og:image"]')
og_title = soup.select_one('meta[property="og:title"]')
og_description = soup.select_one('meta[property="og:description"]')

print(og_image)
print(og_title)
print(og_description)

# 가져온 meta tag의 content를 가져와보기
url_image = og_image['content']
url_title = og_title['content']
url_description = og_description['content']

print(url_image)
print(url_title)
print(url_description)

# 걍 나도 해보기 암거나
# 기자 이름 갖고와보기
reporter = soup.select_one('body > div.gb-container.gb-container-a7098352.inner-container > div > div > div.gb-grid-column.gb-grid-column-c5d3a519 > div > div > div > div > div > div > h6 > a')
print(reporter.text)

# meta 태그에서 property="article:tag"인 곳의 내용 출력하기
article_tag = soup.select_one('meta[property="article:tag"]')
print(article_tag['content'])