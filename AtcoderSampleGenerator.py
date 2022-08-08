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
    data = soup.find_all('div', {'class': 'part'})
    filter = []

    for d in data:
        for section in d.find_all('section'):
            if section.text[0:7].lstrip()[0:7] == 'Sample':
                filter.append(d)

    data = filter

    tests = []
    for d in data:
        da = d.find_all('pre')
        for t in da:
            tests.append(t.text.rstrip())

    ind = 0
    for i in range(0, len(tests), 2):
        inpPath = relativePath + '\\inp' + str(ind) + '.txt'
        with open(inpPath, 'w') as f:
            f.write(tests[i])
        outPath = relativePath + '\\out' + str(ind) + '.txt'
        with open(outPath, 'w') as f:
            f.write(tests[i + 1])
        ind = ind + 1

    file = open("templates.cpp", "r")
    solPath = relativePath + '\\sol.cpp'
    with open(solPath, 'w') as f:
        f.write(file.read())
    file.close()

class createDirectoryStructure:
    contestId = sys.argv[1]
    URL = 'https://atcoder.jp/contests/' + contestId +'/tasks'

    response = urlopen(URL)
    html = response.read()

    soup = BeautifulSoup(html, 'html.parser')

    data = []
    table = soup.find('table', attrs = {'class': 'table table-bordered table-striped'})
    rows = table.find_all('tr')

    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        href = row.find_all('a')
        if href == []:
            continue
        new_data = [ele for ele in cols if ele]
        new_data.append(href[0]['href'])
        data.append(new_data)

    for i in range(len(data) - 1):
        name = data[i][0]
        createFolder(name)
        createTestCases(name, 'https://atcoder.jp' + data[i][4])
        print('Files created for Problem ' + name)

print('Creating Problem Folders...')
createDirectoryStructure