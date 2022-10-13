import requests
from bs4 import BeautifulSoup

url = 'https://n.news.naver.com/article/032/0003178580?cds=news_media_pc&type=editn'

headers = {
    'User-Agent': 'Mizilla/5.0 (windows NT 10.0; win64; x64) Applewebkit/537.36 (KHTML, liek Gecko) Chrome/92.0.4515.131 Safari/537.36'}
result = requests.get(url, headers=headers)

doc = BeautifulSoup(result.text, 'html.parser')

title = doc.select('h2.media_end_head_headline')[0].get_text()
# get_text() 태그를 제거하고 text만 추출
# strip() : 앞 뒤 공백 제거

content = doc.select('div#dic_area')[0].get_text().strip()

print(f'본문 : {title}')  # fstring
print('내용 : {}'.format(content))  # format
