import requests
from bs4 import BeautifulSoup
counter = 1
i =0
islemciModeliN11=[]
for i in range(1):
    requestForLinksN11 = requests.get('https://www.n11.com/bilgisayar/dizustu-bilgisayar?pg=' + str(i + 1))
    #print(('https://www.n11.com/bilgisayar/dizustu-bilgisayar?pg='+str(i+1)))
    soupForLinksN11 = BeautifulSoup(requestForLinksN11.content, 'html.parser')
    listForLinksN11=soupForLinksN11.find_all("li", {"class": "column"})

    for li in listForLinksN11:
        link=li.div.a
        print(counter)
        counter+=1
        print(link.get("href"))
        #buraya kadarı aldığım linkleri yazdırmak için yaptım
        #şimdi yapmam gereken her linke request atıp özelliklerini çekmek
        requestForAttributes=requests.get(link.get("href"))
        #print(requestForAttributes)
        soupForAttributesN11=BeautifulSoup(requestForAttributes.content, "html.parser")
        listForQuestions = soupForAttributesN11.find_all("p", attrs={"class": "unf-prop-list-title"})
        listForAnswer = soupForAttributesN11.find_all("p", attrs={"class": "unf-prop-list-prop"})
        i = 0
        listForİmg=soupForAttributesN11.find_all("div", attrs={"class": "imgObj"})
        listForPrice=soupForAttributesN11.find_all("div", attrs={"class": "unf-p-summary-price"})
        for price in listForPrice:
            print(price.text)
        for img in listForİmg:
            link=img.a
            print(link.get("href"))
        for i in range(len(listForAnswer)):
            #print(listForQuestions[i].string + ":" + listForAnswer[i].string)
            if listForQuestions[i].text == 'İşlemci' and listForQuestions[i].findNext().string != ":":
                lis = listForAnswer[i].string
                print(lis.string)
            if listForQuestions[i].text == 'İşlemci Modeli' and listForQuestions[i].findNext().string != ":":
                lis = listForAnswer[i].string
                print(lis.string)
            if listForQuestions[i].text == 'Marka' and listForQuestions[i].findNext().string != ":":
                lis = listForAnswer[i].string
                print(lis.string)
            if listForQuestions[i].text == 'Disk Kapasitesi' and listForQuestions[i].findNext().string != ":":
                lis = listForAnswer[i].string
                print(lis.string)
            if listForQuestions[i].text == 'Bellek Kapasitesi' and listForQuestions[i].findNext().string != ":":
                lis = listForAnswer[i].string
                print(lis.string)
            if listForQuestions[i].text == 'Model' and listForQuestions[i].findNext().string != ":":
                lis = listForAnswer[i].string
                print(lis.string)
            if listForQuestions[i].text == 'İşletim Sistemi' and listForQuestions[i].findNext().string != ":":
                lis = listForAnswer[i].string
                print(lis.string)
            if listForQuestions[i].text == 'Ekran Kartı Türü' and listForQuestions[i].findNext().string != ":":
                lis = listForAnswer[i].string
                print(lis.string)
            if listForQuestions[i].text == 'Ekran Kartı Modeli' and listForQuestions[i].findNext().string != ":":
                lis = listForAnswer[i].string
                print(lis.string)
print("islemci modelleri")
print(islemciModeliN11)
