import os, sys
from venv import create
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

def createTestCases(relativePath, url):
    response = urlopen(url)
    html = response.read()

    soup = BeautifulSoup(html, 'html.parser')
    data = soup.find_all('pre')

    ind = 0
    for i in range(0, len(data), 2):
        inpPath = relativePath + '\\inp' + str(ind) + '.txt'
        with open(inpPath, 'w') as f:
            f.write(data[i].text)
        outPath = relativePath + '\\out' + str(ind) + '.txt'
        with open(outPath, 'w') as f:
            f.write(data[i + 1].text)
        ind = ind + 1

    file = open("templates.cpp", "r")
    solPath = relativePath + '\\sol.cpp'
    with open(solPath, 'w') as f:
        f.write(file.read())
    file.close()

class createDirectoryStructure:
    URL = sys.argv[1]

    response = urlopen(URL)
    html = response.read()

    soup = BeautifulSoup(html, 'html.parser')
        
    title = getTitle(soup.find('title'))
    titleText = formatTitle(title)

    data = []
    table = soup.find('table', attrs = {'class': 'problems'})
    rows = table.find_all('tr')

    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])

    createFolder(titleText)
    for i in range(len(data) - 1):
        name = data[i + 1][0]
        createFolder(titleText + '\\' + name)
        createTestCases(titleText + '\\' + name, URL + '/problem/' + name)
        print('Files created for Problem ' + name)

createDirectoryStructure