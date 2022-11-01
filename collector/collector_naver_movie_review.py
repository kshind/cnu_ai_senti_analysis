import requests

from bs4 import BeautifulSoup



####################
# 1. 영화 제목 수집 #
####################

# movie_code: 네이버 영화 코드 (6자리 숫자)


# 제목 수집
# 함수
# -1.생성, 2.호출
# 함수는 생성하면 아무 동작x
# 반드시 생성 후 호출을 통해서 사용!
def movie_title_crawler(movie_code):
    url = f'https://movie.naver.com/movie/bi/mi/point.naver?code={movie_code}'
    result = requests.get(url)
    doc = BeautifulSoup(result.text, 'html.parser')
    title = doc.select('h3.h_movie > a')[0].get_text()
    return title

# 리뷰 수집 (리뷰, 평점, 작성자 ,작성 일자) + 제목
def movie_review_crawler(movie_code):
    title = movie_title_crawler(movie_code)  # 제목 수집
    # 리뷰를 수집하는 코드 작성
    url = ''

    print(f'제목: {title}')

    # set {제목, 리뷰, 평점, 작성자, 작성일자}