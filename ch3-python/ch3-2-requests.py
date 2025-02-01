import requests

# r = requests.get(url) -> http response가 r객체에 저장됨
r = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
# .json()은 requests라이브러리에서 제공하는 jons 파싱 메서드. response 데이터를 jons형식(딕셔너리)으로 변환해줌
rjson = r.json()

# 모든 구의 IDEX_MVL값 프린트하기
for x in rjson['RealtimeCityAir']['row']:
    print('IDEX_MVL: ')
    print(x['IDEX_MVL'])

print('----------')

# 모든 구의 IDEX_MVL 값이 60 미만인 구의 이름과 값 프린트하기
for x in rjson['RealtimeCityAir']['row']:
    if x['IDEX_MVL']<70 :
        print(x['MSRSTE_NM'] + " : " + str(x['IDEX_MVL']))
    else: print(x['MSRSTE_NM'] + " : " + 'it\'s over 70')
        
