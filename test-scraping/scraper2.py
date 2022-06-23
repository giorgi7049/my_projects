from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

html = urlopen("https://pythonscraping.com/pages/page1.html")
bs = BeautifulSoup(html, 'html.parser')

def getTitle(url):
    try:
        html1 = urlopen(url)
    except HTTPError as e:
        return None
    try:
        title = bs.body.h1
    except AttributeError as e:
        return None
    return title


title = getTitle(html)
if title == None:
    print('Title could not be found')
else:
    print(title)

