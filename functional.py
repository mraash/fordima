import requests
from bs4 import BeautifulSoup

# Reusable functions
def getWebsiteSoup(url: str) -> BeautifulSoup:
    headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }

    response = requests.get(url, headers=headers)
    responseBody = response.text
    responseSoup = BeautifulSoup(responseBody, 'html.parser')

    return responseSoup


def writeToFile(filename: str, text: str) -> None:
    open(filename, 'w').write(text).close()


# Specific functions
def pullDataFromPostList(responseSoup: BeautifulSoup) -> list:
    responseSoup.find('ul', class_='list-recent-posts menu').find_all('li')

    postListData = []
    for postSoup in responseSoup:
        postListData.append({
            'link' :  postSoup.find('a').get('href'),
            'title' :  postSoup.find('h3').text,
            'date' :  postSoup.find('p').text,
        })

    return postListData


def makeResultString(postListData: list) -> str:
    resultText = ''
    for postData in postListData:
        for key, value in postData.items():
            resultText = resultText + value + '\n'
        resultText = resultText + '\n'
    
    return resultText


# Script execution
pythonOrgSoup = getWebsiteSoup('https://www.python.org/blogs/')

postListData = pullDataFromPostList(pythonOrgSoup)

result = makeResultString(postListData)

writeToFile('result.txt', result)
