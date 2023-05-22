import requests
from bs4 import BeautifulSoup


url = "https://sports.news.naver.com/wfootball/schedule/index?category=epl"
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    rank = 1
    for tr in soup.select("#frm > div > table > tbody > tr"):
        title = tr.select_one(".ellipsis.rank01 > span > a").text
        artist = tr.select_one(".ellipsis.rank02 > a").text
        print(rank, title, artist) 
        rank += 1
else:
        print(f"HTTP 요청 실패 코드: {response.status_code}")