import os, sys
from venv import create
from bs4 import BeautifulSoup
from urllib.request import urlopen

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
            d = data[i].text.lstrip()
            f.write(d)
        outPath = relativePath + '\\out' + str(ind) + '.txt'
        with open(outPath, 'w') as f:
            d = data[i + 1].text.lstrip()
            f.write(d)
        ind = ind + 1

    file = open("templates.cpp", "r")
    solPath = relativePath + '\\sol.cpp'
    with open(solPath, 'w') as f:
        f.write(file.read())
    file.close()

class createDirectoryStructure:
    print('Creating Problem Folders...')
    contestId = sys.argv[1]
    URL = 'https://codeforces.com/contest/' + contestId + '/'

    response = urlopen(URL)
    html = response.read()

    soup = BeautifulSoup(html, 'html.parser')

    data = []
    table = soup.find('table', attrs = {'class': 'problems'})
    rows = table.find_all('tr')

    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])

    for i in range(len(data) - 1):
        name = data[i + 1][0]
        createFolder(name)
        createTestCases(name, URL + '/problem/' + name)
        print('Files created for Problem ' + name)

createDirectoryStructure