########################################################
# collector 비즈니스 로직을 모아둔 파이썬 파일
########################################################
# - Date : 2022.10.18: 파일 생성, 김승현
########################################################

import requests
from bs4 import BeautifulSoup

# 함수 생성
# - 함수: 반복적으로 사용하는 기능을 코드로 묶어서 만듦
# - 사용: 함수이름으로 호출!
# - Python에서 ()이 붙어 있으면 대부분 함수
# - 예: print(), pprint(), get(), get_text()
# - 내장 함수: 파이썬 설치하면 기본적으로 제공
# - 외부 함수 다른 개발자가 만들어 놓은 거 import 해서 사용
#            requests.get(), BeautifulSoup()
# - 사용자 정의 함수: 직접 만들어서 사용

# Python Naming RULE
# 1) 파스칼(Pascal)    -> GetDaumNews(고대언어)
# 2) 카멜(Camel)       -> getDaumNews
# 3) 스네이크(snake)    -> get_daum_news(최신언어)


def get_daum_news(url) :
    result = requests.get(url)

    doc = BeautifulSoup(result.text, 'html.parser')
    title = doc.select('h3.tit_view')[0].get_text()
    contents = doc.select('section p')
    print(f'뉴스 제목: {title}')

    # if문 -> 제어문(조건이 True인 경우에만 실행)
    # != 같지 않다.
    if len(contents) != 0:  # 본문이 있는 경우에만
        content = ''
        for line in contents:
            content += line.get_text()
        print(f'뉴스본문: {content}')