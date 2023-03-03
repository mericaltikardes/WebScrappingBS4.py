import requests
from bs4 import BeautifulSoup
import pymongo

counter=0
i=1
client=pymongo.MongoClient()
urller=[]
mydb=client["Bilgisayarlarid2"]
mycol=mydb["Bilgisayarlar"]
markaTrendyol=[]
islemciModeliTrendyol=[]
ramTrendyol=[]
ssdTrendyol=[]
for i in range(10):
   requestForLinksTrendyol = requests.get('https://www.trendyol.com/sr?wc=103108&os=1&sk=1&pi= ' + str(i + 1))
   #print('https://www.trendyol.com/sr?wc=103108&os=1&sk=1&pi='+str(i) )
   soupForLinksTrendyol = BeautifulSoup(requestForLinksTrendyol.content, 'html.parser')
   requestForLinksTrendyol = requests.soup(requestForLinksTrendyol.content, 'html.parser')
   attrs_list = soupForLinksTrendyol.find_all("div", attrs={"class": "p-card-chldrn-cntnr card-border"})
   #for links
   j=0
   #linkleri getirmek için
   for li in attrs_list:
      link = li.a
      url="https://www.trendyol.com/" + link.get("href")
      #print(url)
      requestForAttributesTrendyol=requests.get("https://www.trendyol.com/" + link.get("href"))
      #ürünlere gitmek için kullandığım soup
      soupForAttributesTrendyol = BeautifulSoup(requestForAttributesTrendyol.content, 'html.parser')
      counter+=1
      #bağlantı sağlam mı Kontrolü
      #print(r2) linklere gidip özellik alamk için
      attrsListTrendyol = soupForAttributesTrendyol.find_all("ul", attrs={"class": "detail-attr-container"})
      attrsListTrendyol = soupForAttributesTrendyol.find_all("span")
      #for attributes
      attrs_photo=soupForAttributesTrendyol.find_all("img")
      # marka çekmek için(titledan)
      attrsTitleTrendyol=soupForAttributesTrendyol.find_all("h3", attrs={"class": "detail-name"})
      attrs_price=soupForAttributesTrendyol.find_all("span",attrs={"class":"prc-dsc"})
      for att in attrsTitleTrendyol:
         attrsTitleTrendyol = att.text
      attrsTitleTrendyol = attrsTitleTrendyol.split(" ")
      markaTrendyol=attrsTitleTrendyol[0]
      #print(marka)
      for prc in attrs_price:
         priceTrendyol = prc.text
      #print(price)
      i=0
      link_img_Trendyol=attrs_photo[1]["src"]
      for lis in attrsListTrendyol:
         if lis.text == 'Ekran Kartı' and lis.findNext().string != ":":
            lis = lis.findNext()
            ekranKartıTipiTrendyol=lis.string
            #print(lis.string)
         if lis.text == 'Ekran Kartı Hafızası' and lis.findNext().string != ":":
            lis = lis.findNext()
            ekranKartıHafizasiTrendyol = lis.string
           # print(lis.string)

         if lis.text == 'İşlemci Tipi' and lis.findNext().string != ":":
            lis = lis.findNext()
            islemciTipi=lis.string
            #print(lis.string)

         if lis.text == 'SSD Kapasitesi' and lis.findNext().string != ":":
            lis = lis.findNext()
            ssdKapasitesi=lis.string
           # print(lis.string)

         if lis.text == 'İşletim Sistemi' and lis.findNext().string != ":":
            lis = lis.findNext()
            isletimSistemi=lis.string
            #print(lis.string)

         if lis.text == 'Ram (Sistem Belleği)' and lis.findNext().string != ":":
            lis = lis.findNext()
            ramTrendyol=lis.string
            #print(lis.string)
         if lis.text == 'İşlemci Modeli' and lis.findNext().string != ":":
             lis= lis.findNext()
             IslemciModeli=lis.string
            #print(lis.string)
      j = j + 1
      # pymongo eklemesi için
      mycol.insert_one({
         "id":j,
         "link": "https://www.trendyol.com/" + link.get("href"),
         "Marka":markaTrendyol,
         "islemcitipi":islemciTipi,
         "islemciModeli":IslemciModeli,
         "ekranKartıTipi":ekranKartıTipiTrendyol,
         "ekranKartıHafızası":ekranKartıHafizasiTrendyol,
         "ssdkapasitesi":ssdKapasitesi,
         "isletimsistemi":isletimSistemi,
         "ram":ramTrendyol,
         "siteAdi":"Trendyol",
         "UrunGorseli":link_img_Trendyol,
         "Fiyat":priceTrendyol
         })

#link sayısını bulmak için
print(counter)

#N11
counter = 1
i =0
for i in range(10):
    requestForLinksN11 = requests.get('https://www.n11.com/bilgisayar/dizustu-bilgisayar?pg=' + str(i + 1))
    #print(('https://www.n11.com/bilgisayar/dizustu-bilgisayar?pg='+str(i+1)))
    soupForLinksN11 = BeautifulSoup(requestForLinksN11.content, 'html.parser')
    listForLinksN11=soupForLinksN11.find_all("li", {"class": "column"})
    for li in listForLinksN11:
        link=li.div.a
        print(counter)
        counter+=1
        print(link.get("href"))
        linkForLinksN11=link.get("href")
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
            priceN11=price.text
        for img in listForİmg:
            link=img.a
            print(link.get("href"))
            link_imgN11=link.get("href")
        for i in range(len(listForAnswer)):
            #print(listForQuestions[i].string + ":" + listForAnswer[i].string)
            if listForQuestions[i].text == 'İşlemci' and listForQuestions[i].findNext().string != ":":
                lis = listForAnswer[i].string
                islemciTipiN11=lis.string
                print(lis.string)
            if listForQuestions[i].text == 'İşlemci Modeli' and listForQuestions[i].findNext().string != ":":
                lis = listForAnswer[i].string
                islemciModeliN11=lis.string
                print(lis.string)
            if listForQuestions[i].text == 'Marka' and listForQuestions[i].findNext().string != ":":
                lis = listForAnswer[i].string
                markaN11=lis.string
                print(lis.string)
            if listForQuestions[i].text == 'Disk Kapasitesi' and listForQuestions[i].findNext().string != ":":
                lis = listForAnswer[i].string
                ssdN11=lis.string
                print(lis.string)
            if listForQuestions[i].text == 'Bellek Kapasitesi' and listForQuestions[i].findNext().string != ":":
                lis = listForAnswer[i].string
                ramN11=lis.string
                print(lis.string)
            if listForQuestions[i].text == 'Model' and listForQuestions[i].findNext().string != ":":
                lis = listForAnswer[i].string
                modelNoN11=lis.string
                print(lis.string)
            if listForQuestions[i].text == 'İşletim Sistemi' and listForQuestions[i].findNext().string != ":":
                lis = listForAnswer[i].string
                isletimSistemiN11=lis.string
                print(lis.string)
            if listForQuestions[i].text == 'Ekran Kartı Türü' and listForQuestions[i].findNext().string != ":":
                lis = listForAnswer[i].string
                ekranKartıTipiN11=lis.string
                print(lis.string)
            if listForQuestions[i].text == 'Ekran Kartı Modeli' and listForQuestions[i].findNext().string != ":":
                lis = listForAnswer[i].string
                ekranKartıModeliN11=lis.string
                print(lis.string)
                # pymongo eklemesi için
        mycol.insert_one({
            "link":linkForLinksN11,
            "Marka": markaN11,
            "ModelNo":modelNoN11,
            "islemcitipi": islemciTipiN11,
            "islemciModeli": islemciModeliN11,
            "ekranKartıTürü":ekranKartıTipiN11,
            "ekranKartıModeli":ekranKartıModeliN11,
            "ssdkapasitesi": ssdN11,
            "isletimsistemi": isletimSistemiN11,
            "ram": ramN11,
            "siteAdi": "N11",
            "UrunGorseli": link_imgN11,
            "Fiyat": priceN11
            })

#VATANBİLGİSAYAR
url="https://www.vatanbilgisayar.com/notebook/?page="
for i in range(10):
    requestForLinksVatan=requests.get(url + str(i + 1))
    soupForLinksVatan = BeautifulSoup(requestForLinksVatan.content, 'html.parser')
    listForLinkVatan = soupForLinksVatan.find_all("div", attrs={"class": "product-list__image-safe"})
    for li in listForLinkVatan:
       li=li.a
       print("https://www.vatanbilgisayar.com"+li.get("href"))
       linkForLinksVatan="https://www.vatanbilgisayar.com"+li.get("href")
       requestForAttributesVatan=requests.get("https://www.vatanbilgisayar.com"+li.get("href"))
       soupForAttributes=BeautifulSoup(requestForAttributesVatan.content,"html.parser")
       attrsListVatan = soupForAttributes.find_all("table", attrs={"class": "product-table"})
       attrsListVatan = soupForAttributes.find_all("td")
       #marka çekmek için title
       attsTitleVatan = soupForAttributes.find_all("h1", attrs={"class": "product-list__product-name"})
       #fiyat çekmek için
       attsPriceVatan = soupForAttributes.find("span", attrs={"class": "product-list__price"})
       #fotoları çekmek için
       attrsPhotoVatan = soupForAttributes.find("img", attrs={"class": "img-responsive"})
       print(attrsPhotoVatan['data-src'])
       link_imgVatan=attrsPhotoVatan['data-src']
       for prc in attsPriceVatan:
           print(prc.text)
           priceVatan=prc.text
       for mrk in attsTitleVatan:
           marka = mrk.text.split(" ")
           print(marka[0])
           markaVatan=marka[0].lstrip()
       for att in attrsListVatan:
           if att.text == 'İşlemci Nesli' and att.findNext().string != ":":
               att = att.findNext().findNext()
               islemciNesliVatan = att.string
               print(att.string)
           if att.text == 'İşlemci Numarası' and att.findNext().string != ":":
               att = att.findNext().findNext()
               islemciNumarasiVatan = att.string
               print(att.string)
           if att.text == 'Ram (Sistem Belleği)' and att.findNext().string != ":":
               att = att.findNext().findNext()
               ramVatan = att.string
               print(att.string)
           if att.text == 'Disk Kapasitesi' and att.findNext().string != ":":
               att = att.findNext().findNext()
               diskVatan = att.string
               print(att.string)
           if att.text == 'İşletim Sistemi' and att.findNext().string != ":":
               att = att.findNext().findNext()
               isletimsistemiVatan = att.string
               print(att.string)
           if att.text == 'Ekran Kartı Tipi' and att.findNext().string != ":":
               att = att.findNext().findNext()
               ekranKartıTipiVatan = att.string
               print(att.string)
           if att.text == 'Ekran Kartı Chipseti' and att.findNext().string != ":":
               att = att.findNext().findNext()
               ekranKartıModeliVatan = att.string
               print(att.string)
       mycol.insert_one({
           "link": linkForLinksVatan,
           "Marka": markaVatan,
           "islemcitipi": islemciNesliVatan,
           "islemciModeli":islemciNumarasiVatan,
           "ekranKartıTipi":ekranKartıTipiVatan,
           "ekranKartıModeli":ekranKartıModeliVatan,
           "ssdkapasitesi": diskVatan,
           "isletimsistemi": isletimsistemiVatan,
           "ram": ramVatan,
           "siteAdi": "Vatan",
           "UrunGorseli": link_imgVatan,
           "Fiyat": priceVatan
       })
#TEKNOSA
i=0
linkimgforteknosa=[]
for i in range(10):
    requestForLinksTeknosa=requests.get("https://www.teknosa.com/laptop-notebook-c-116004?s=%3Arelevance&page=" + str(i + 1))
    soupForLinksTeknosa = BeautifulSoup(requestForLinksTeknosa.content, 'html.parser')
    listForLinkTeknosa=soupForLinksTeknosa.find_all("a", attrs={"class": "prd-link"})
    counter=0
    for li in listForLinkTeknosa:
        print("https://www.teknosa.com"+li.get("href"))
        linkForLinksTeknosa="https://www.teknosa.com"+li.get("href")
        requestForAttributesTeknosa=requests.get("https://www.teknosa.com" + li.get("href"))
        #print(requestForAttributes)
        soupForAttributesTeknosa=BeautifulSoup(requestForAttributesTeknosa.content, "html.parser")
        listQuestionsAndAnswer = soupForAttributesTeknosa.find_all("tr")
        listQuestions = soupForAttributesTeknosa.find_all("th")
        listAnswer = soupForAttributesTeknosa.find_all("td")
        # marka çekmek için title aldım
        attrsTitleTeknosa=soupForAttributesTeknosa.find_all("h2", attrs={"class": "name"})
        attrsPriceTeknosa=soupForAttributesTeknosa.find("span", attrs={"class": "prc prc-last"})
        attrsImageTeknosa=soupForAttributesTeknosa.find_all("img", attrs={"class": ""})

        for attprs in attrsImageTeknosa:
            imageTeknosa=attprs["src"]
            #print(att)
            imageTeknosa = imageTeknosa.split("data")
            print(imageTeknosa[0])
        for price in attrsPriceTeknosa:
            print(price)
            priceTeknosa=price
        for a in attrsTitleTeknosa:
            attrsTitleTeknosa=a.text
        attrsTitleTeknosa=attrsTitleTeknosa.split(" ")
        print(attrsTitleTeknosa[0])
        markaTeknosa=attrsTitleTeknosa[0]
        for i in range(len(listQuestions)):
            #print(listQuestions[i].text + ":" + listAnswer[i].text)
            if listQuestions[i].text == 'İşlemci' and listQuestions[i].findNext().string != ":":
                lis = listAnswer[i].string
                print(lis.string)
                islemciTipiTeknosa=lis.string
            if listQuestions[i].text == 'İşlemci Modeli' and listQuestions[i].findNext().string != ":":
                lis = listAnswer[i].string
                print(lis.string)
                islemciModeliTeknosa=lis.string
            if listQuestions[i].text == 'SSD Kapasitesi' and listQuestions[i].findNext().string != ":":
                lis = listAnswer[i].string
                print(lis.string)
                ssdTeknosa=lis.string
            if listQuestions[i].text == 'Ram' and listQuestions[i].findNext().string != ":":
                lis = listAnswer[i].string
                print(lis.string)
                ramTeknosa=lis.string
            if listQuestions[i].text == 'Model Kodu' and listQuestions[i].findNext().string != ":":
                lis = listAnswer[i].string
                print(lis.string)
                modelNoTeknosa=lis.string
            if listQuestions[i].text == 'İşletim Sistemi Yazılımı' and listQuestions[i].findNext().string != ":":
                lis = listAnswer[i].string
                print(lis.string)
                isletimsistemiTeknosa=lis.string

        mycol.insert_one({
            "link": linkForLinksTeknosa,
            "Marka": markaTeknosa,
            "ModelNo":modelNoTeknosa,
            "islemcitipi": islemciTipiTeknosa,
            "islemciModeli": islemciModeliTeknosa,
            "ssdkapasitesi": ssdTeknosa,
            "isletimsistemi": isletimsistemiTeknosa,
            "ram": ramTeknosa,
            "siteAdi": "Teknosa",
            "Fiyat": priceTeknosa
        })








