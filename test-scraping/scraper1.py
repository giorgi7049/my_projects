from urllib.request import urlopen
from bs4 import BeautifulSoup


url = urlopen("https://pythonscraping.com/pages/warandpeace.html")
bs = BeautifulSoup(url, 'html.parser')
namelist = bs.find_all('span', {'class': 'green'})
for name in namelist:
    print(name.get_text())
