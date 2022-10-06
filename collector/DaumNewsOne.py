#1. 프로젝트(cnu_ai_senti)analysis-main)
# ㄴ 2. python package (collector)
#    ㄴ 3. python file(test.py, DaumNewsOne.py)
# python package : python file 들을 모아두는 폴더
#                 폴더 아이콘 안에 구멍 뚫려있음

#import와 Library(module)
# python 코드를 직접 작성해서 개발할 수도 있지만 다른 개발자가 이미 만들어 놓은 코드를 사용하면 편리함
#이미 개발되어있는 코드들의 묶음 = 라이브러리(module)
#1. built in Library : python을 설치하면 자동으로 제공
# 외부 Library 우리가 직접 추가해서 사용
# 예: requests, beautifulsoup4
#Library를 사용하기 위해서는 import 작업 진행
# import는 도서관에서 필요한 책을 빌려오는 개념



# 목표 : Daum뉴스 웹페이지 제목과 본문 데이터 수집
# 1. url :https://v.daum.net/v/20221006105152798
# 2. requests로 해당 url의 html 전체 코드를 수집

# ctrl + / 누르면 한 줄 모두 주석 ctrl + shift + 방향키 줄 위치 옮기기 f12 network ctrl R
#ctrl space는 자동완성
import requests
from bs4 import BeautifulSoup

url = 'https://v.daum.net/v/20221006105152798'

result = requests.get(url)
BeautifulSoup()
# print(result.text)

# 3. beautifulsoup를 통해서 제목과 본문만 추출
doc = BeautifulSoup(result.text, 'html.parser')

#python은 [] : List Type
# index 0  1  2  3   4
# -    [5, 6, 9, 18, 15] : List 내에는 다양한 데이터 저장 가능

title = doc.select('h3.tit_view')[0].get_text()

print(f'뉴스 제목: {title}')