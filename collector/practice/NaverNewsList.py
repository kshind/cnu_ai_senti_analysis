import requests
from bs4 import BeautifulSoup

url = 'https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=105'

headers = {'User-Agent' : 'Mizilla/5.0 (windows NT 10.0; win64; x64) Applewebkit/537.36 (KHTML, liek Gecko) Chrome/92.0.4515.131 Safari/537.36'}
result = requests.get(url, headers=headers)

doc = BeautifulSoup(result.text, 'html.parser')
title_list = doc.select('div.section_body a')
print(len(title_list))