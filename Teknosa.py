import requests
from bs4 import BeautifulSoup
i=0
for i in range(1):
    requestForLinksTeknosa=requests.get("https://www.teknosa.com/laptop-notebook-c-116004?s=%3Arelevance&page=" + str(i + 1))
    soupForLinksTeknosa = BeautifulSoup(requestForLinksTeknosa.content, 'html.parser')
    listForLinkTeknosa=soupForLinksTeknosa.find_all("a", attrs={"class": "prd-link"})
    counter=0
    for li in listForLinkTeknosa:
        print("https://www.teknosa.com"+li.get("href"))
        requestForAttributesTeknosa=requests.get("https://www.teknosa.com" + li.get("href"))
        #print(requestForAttributes)
        soupForAttributesTeknosa=BeautifulSoup(requestForAttributesTeknosa.content, "html.parser")
        listQuestionsAndAnswer = soupForAttributesTeknosa.find_all("tr")
        listQuestions = soupForAttributesTeknosa.find_all("th")
        listAnswer = soupForAttributesTeknosa.find_all("td")
        # marka çekmek için title aldım
        attrsTitleTeknosa=soupForAttributesTeknosa.find_all("h2", attrs={"class": "name"})
        attrsPriceTeknosa=soupForAttributesTeknosa.find("span", attrs={"class": "prc prc-last"})
        attrsİmageTeknosa=soupForAttributesTeknosa.find_all("img", attrs={"class": ""})

        for att in attrsİmageTeknosa:
            att=att["src"]
            #print(att)
            att=att.split("data")
            print(att[0])
        for price in attrsPriceTeknosa:
            print(price)
        for a in attrsTitleTeknosa:
            attrsTitleTeknosa=a.text
        attrsTitleTeknosa=attrsTitleTeknosa.split(" ")
        print(attrsTitleTeknosa[0])
        print("Teknosa")
        for i in range(len(listQuestions)):
            #print(listQuestions[i].text + ":" + listAnswer[i].text)
            if listQuestions[i].text == 'İşlemci' and listQuestions[i].findNext().string != ":":
                lis = listAnswer[i].string
                print(lis.string)
            if listQuestions[i].text == 'İşlemci Modeli' and listQuestions[i].findNext().string != ":":
                lis = listAnswer[i].string
                print(lis.string)
            if listQuestions[i].text == 'SSD Kapasitesi' and listQuestions[i].findNext().string != ":":
                lis = listAnswer[i].string
                print(lis.string)
            if listQuestions[i].text == 'Ram' and listQuestions[i].findNext().string != ":":
                lis = listAnswer[i].string
                print(lis.string)
            if listQuestions[i].text == 'Model Kodu' and listQuestions[i].findNext().string != ":":
                lis = listAnswer[i].string
                print(lis.string)
            if listQuestions[i].text == 'İşletim Sistemi Yazılımı' and listQuestions[i].findNext().string != ":":
                lis = listAnswer[i].string
                print(lis.string)
            if listQuestions[i].text == 'Ekran Kartı Modeli' and listQuestions[i].findNext().string != ":":
                lis = listAnswer[i].string
                print(lis.string)
            if listQuestions[i].text == 'Ekran Kartı Belleği (GB)' and listQuestions[i].findNext().string != ":":
                lis = listAnswer[i].string
                print(lis.string)















