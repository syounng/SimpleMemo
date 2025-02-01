import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,
# http요청을 보낼 때 포함되는 '요청 헤더'. User-Agent는 브라우저 정보를 담고 있음
# 일부 웹사이트는 봇(스크래핑 프로그램)이 데이터를 가져가는 걸 막기 위해 User-Aget가 없는 요청을 차단하기 때문에 사람이 요청한 것처럼 보이려면 html을 받아올 때 이 헤더를 같이 전달해야 한다.
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.imdb.com/chart/top/?ref_=nv_mv_250', headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
# 첫 번째 인자로 html코드, 두 번째 인자로 파이썬 기본 제공 html 분석기를 지정.
soup = BeautifulSoup(data.text, 'html.parser')
#print(soup)  # HTML을 받아온 것을 확인할 수 있다.


#############################

# soup.select('css 선택자')를 통해 해당 선택자에 해당하는 모든 요소를 list로 반환
# 한 개가 아니라 여러 개의 요소를 한 번에 가져올 때 사용됨
# .는 클래스를 찾는다는 의미, >는 바로 아래에 있는 자식 요소만 선택한다는 의미.
# 즉 ipc-age-grid__item--span-2 클래스 요소 내부의 모든 <li>태그를 가져와서 movies에 리스트로 저장됨.
# 참고로 soup.select_one()은 첫 번째 요소만 반환됨.

# 모든 영화들 찾기
movies = soup.select('.ipc-page-grid__item--span-2 > .ipc-metadata-list--base > li')


for movie in movies:
    # movie 안에 h3가 있으면 조건을 만족하는 첫 번째 요소를, 없으면 None을 반환
    tag_element = movie.select_one('.ipc-title-link-wrapper > h3')
    if not tag_element:
        continue
    # h3의 text를 찍어보기
    print(tag_element.text)

# 꿀팁: 개발자 도구 Elements 탭에서 요소를 우클릭한 후 Copy > Copy selector를 해서 선택자를 얻을 수 있다.