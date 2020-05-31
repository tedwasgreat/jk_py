import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

for row in soup.select('tbody > .list'):
    rank = row.select_one('.number').text.split("\n")[0]
    title = row.select_one('.info > .title.ellipsis').text.strip()
    artist = row.select_one('.info > .artist.ellipsis').text
    if rank: 
        print(rank, title, artist)