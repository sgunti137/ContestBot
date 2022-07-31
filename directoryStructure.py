import os
from bs4 import BeautifulSoup
from urllib.request import urlopen

def getTitle(str):
    for x in str:
        return x

def formatTitle(str):
    st = 0
    res = ""
    for x in str:
        if (st == 0 and x == '-'):
            st = 1
        elif (st == 1 and x == '-'):
            st = 0
        elif st == 1:
            res += x
    return res[1:-1]

def createFolder(relativePath):
    path = os.getcwd() + '\\' + relativePath
    if not os.path.isdir(path):
        os.makedirs(path)

response = urlopen('https://codeforces.com/contest/1711')
html = response.read()

soup = BeautifulSoup(html, 'html.parser')
    
title = getTitle(soup.find('title'))
titleText = formatTitle(title)

data = []
table = soup.find('table', attrs={'class':'problems'})
rows = table.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele])

createFolder(titleText)
for i in range(len(data) - 1):
    name = chr(ord('A') + i)
    createFolder(titleText + '\\' + name)