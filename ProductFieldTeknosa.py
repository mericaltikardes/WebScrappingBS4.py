import requests
from bs4 import BeautifulSoup
import json
url="https://www.teknosa.com/hp-255-g9-6q8n2es-ryzen-5-5625u-156-8-gb-ram-512-gb-ssd-fhd-freedos-tasinabilir-bilgisayar-p-786282534"
r=requests.get(url)
soup=BeautifulSoup(r.content, 'html.parser')
listQuestionsAndAnswer=soup.find_all("div", attrs={"class": "ptf-body"})
listQuestionsAndAnswer = soup.find_all("tr")
listQuestions=soup.find_all("th")
listAnswer=soup.find_all("td")
print(len(listQuestions))
print(len(listAnswer))
print(len(listQuestionsAndAnswer))
i=0
for i in range(len(listQuestionsAndAnswer)):
    #print(listQuestions[i].text+":"+listAnswer[i].text)
    pass