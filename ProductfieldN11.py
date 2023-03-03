from builtins import print

import requests
from bs4 import BeautifulSoup

r=requests.get("https://www.n11.com/urun/lenovo-ideapad-3-15itl6-82h802f6tx-i5-1135g7-8-gb-1-tb-ssd-156-free-dos-dizustu-bilgisayar-17853320?magaza=yorungeonline")
soupForAttributes = BeautifulSoup(r.content, 'html.parser')
#list=soup.find_all("li",attrs={"class":"unf-prop-list-item"})
listForQuestions=soupForAttributes.find_all("p", attrs={"class": "unf-prop-list-title"})
listForAnswer=soupForAttributes.find_all("p", attrs={"class": "unf-prop-list-prop"})

i=0
for i in range(len(listForAnswer)) :
    print(listForQuestions[i].string+":"+listForAnswer[i].string)


