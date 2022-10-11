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
# 1) requests로 해당 url의 전체 소스코드를 가지고 옴!
# 2) Beautifulsoup에게 전체 소스코드도 전달 -> doc
# 3) bs4가 전체 소스코드에게 원하는 데이터만 select


# 1. url :https://v.daum.net/v/20221006105152798
# 2. requests로 해당 url의 html 전체 코드를 수집

# ctrl + / 누르면 한 줄 모두 주석 ctrl + shift + 방향키 줄 위치 옮기기 f12 network ctrl R
# ctrl space는 자동완성
import requests
from bs4 import BeautifulSoup

url = 'https://v.daum.net/v/20221006105152798'

result = requests.get(url)
BeautifulSoup()
# print(result.text)

# 3. beautifulsoup를 통해서 제목과 본문만 추출
doc = BeautifulSoup(result.text, 'html.parser')

# python은 [] : List Type
# index 0  1  2  3   4
# -    [5, 6, 9, 18, 15] : List 내에는 다양한 데이터 저장 가능
title = doc.select('h3.tit_view')[0].get_text()  #h3태그 중에 이름이 tit_view를 갖는 select

# html -> tag + 선택자
#  -  tag : 기본적으로 정의돼있음(h3, p, div, span, .....)
contents = doc.select('section p')  # section 태그를 부모로 둔 모든 자식 p 태그들 select


print(f'뉴스 제목: {title}')


#  contents = [<p1>, <p2>, <p3>, <p4> ........] : 복수의 본문 포함
#  <p1> = <p>111111111</p1>
#  <p2> = <p>222222222/p2>
#  <p3> = <p>333333333</p3>
#  <p4> = <p>444444444</p4>

#  반복적인 작업 -> for문

content = ''
for line in contents:  # 순서대로 <p>를 가져와서 Line에 넣고 다음 코드 실행
    content += line.get_text()
print(f'뉴스본문: {content}')
