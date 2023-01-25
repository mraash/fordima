import requests
from bs4 import BeautifulSoup 


URL = 'https://www.python.org/blogs/'
HEADERS = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}

result = []

response = requests.get(URL, headers=HEADERS)
soup = BeautifulSoup(response.text, 'html.parser')
news_block = soup.find('ul', class_='list-recent-posts menu')
for data in news_block.find_all('li'):
    result.append({
        'link' :  data.find('a').get('href'),
        'title' :  data.find('h3').text,
        'date' :  data.find('p').text,
    })
    

with open('result.txt', 'w') as f:
    for res in result:
        for key, value in res.items():
            f.write(f'{value}\n')
        f.write('\n')