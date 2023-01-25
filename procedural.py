import requests
from bs4 import BeautifulSoup

URL = 'https://www.python.org/blogs/'
HEADERS = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}

response = requests.get(URL, headers=HEADERS)
responseBody = response.text
responseSoup = BeautifulSoup(responseBody, 'html.parser')

postListSoup = responseSoup.find('ul', class_='list-recent-posts menu').find_all('li')


postListData = []
for postSoup in postListSoup:
    postListData.append({
        'link' :  postSoup.find('a').get('href'),
        'title' :  postSoup.find('h3').text,
        'date' :  postSoup.find('p').text,
    })


resultText = ''
for postData in postListData:
    for key, value in postData.items():
        resultText = resultText + value + '\n'
    resultText = resultText + '\n'


open('result.txt', 'w').write(resultText).close()
