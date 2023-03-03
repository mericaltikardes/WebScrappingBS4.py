import requests
from bs4 import BeautifulSoup
import pymongo

counter = 0
i = 1
client = pymongo.MongoClient()
urller = []
mydb = client["Bilgisayarlarid2"]
mycol = mydb["bilgisayar bilgileri"]
islemciTipi = []
ssdKapasitesi = []
isletimSistemi = []
ram = []
İslemciModeli = []
price = []
ekranKartıTipi = []
ekranKartıHafizasi = []

for i in range(1):
    requestForLinksTrendyol = requests.get('https://www.trendyol.com/sr?wc=103108&os=1&sk=1&pi= ' + str(i + 1))
    # print('https://www.trendyol.com/sr?wc=103108&os=1&sk=1&pi='+str(i) )
    soupForLinksTrendyol = BeautifulSoup(requestForLinksTrendyol.content, 'html.parser')
    attrs_list = soupForLinksTrendyol.find_all("div", attrs={"class": "p-card-chldrn-cntnr card-border"})
    # for links
    j = 0
    # linkleri getirmek için
    for li in attrs_list:
        link = li.a
        url = "https://www.trendyol.com/" + link.get("href")
        print(url)
        requestForAttributesTrendyol = requests.get("https://www.trendyol.com/" + link.get("href"))
        # ürünlere gitmek için kullandığım soup
        soupForAttributesTrendyol = BeautifulSoup(requestForAttributesTrendyol.content, 'html.parser')
        counter += 1
        # bağlantı sağlam mı Kontrolü
        # print(r2) linklere gidip özellik alamk için
        attrsListTrendyol = soupForAttributesTrendyol.find_all("ul", attrs={"class": "detail-attr-container"})
        attrsListTrendyol = soupForAttributesTrendyol.find_all("span")
        # for attributes
        attrs_photo = soupForAttributesTrendyol.find_all("img")
        # marka çekmek için(titledan)
        attrsTitleTrendyol = soupForAttributesTrendyol.find_all("h3", attrs={"class": "detail-name"})
        attrs_price = soupForAttributesTrendyol.find_all("span", attrs={"class": "prc-dsc"})
        for att in attrsTitleTrendyol:
            attrsTitleTrendyol = att.text
        attrsTitleTrendyolForMarka = attrsTitleTrendyol.split(" ")
        print(attrsTitleTrendyol)
        marka = attrsTitleTrendyolForMarka[0]
        print(marka)

        for prc in attrs_price:
            price = prc.text
        print(price)
        i = 0
        link_img = attrs_photo[1]["src"]
        for lis in attrsListTrendyol:
            if lis.text == 'Ekran Kartı' and lis.findNext().string != ":":
                lis = lis.findNext()
                ekranKartıTipi = lis.string
                print(lis.string)
            if lis.text == 'Ekran Kartı Hafızası' and lis.findNext().string != ":":
                lis = lis.findNext()
                ekranKartıHafizasi = lis.string
                # print(lis.string)

            if lis.text == 'İşlemci Tipi' and lis.findNext().string != ":":
                lis = lis.findNext()
                islemciTipi = lis.string

                # print(lis.string)
            if lis.text == 'SSD Kapasitesi' and lis.findNext().string != ":":
                lis = lis.findNext()
                ssdKapasitesi = lis.string
                # print(lis.string)

            if lis.text == 'İşletim Sistemi' and lis.findNext().string != ":":
                lis = lis.findNext()
                isletimSistemi = lis.string
                # print(lis.string)

            if lis.text == 'Ram (Sistem Belleği)' and lis.findNext().string != ":":
                lis = lis.findNext()
                ram = lis.string
                # print(lis.string)
            if lis.text == 'İşlemci Modeli' and lis.findNext().string != ":":
                lis = lis.findNext()
                İslemciModeli = lis.string
                # print(lis.string)

        islemcitTipiDizisi = islemciTipi.split(" ")
        İslemciModeliDizisi = İslemciModeli.split(" ")
        print(islemcitTipiDizisi)
        print(İslemciModeliDizisi)
        j = j + 1
        for m in range(len(islemcitTipiDizisi)):
            for n in range(len(attrsTitleTrendyolForMarka)):
                if attrsTitleTrendyolForMarka[n] != islemcitTipiDizisi[m]:
                    print("model :"+attrsTitleTrendyolForMarka[m])
                    break
                else:
                    pass

    """mycol.insert_one({
       "id":j,
       "link": "https://www.trendyol.com/" + link.get("href"),
       "Marka":marka,
       "islemcitipi":islemciTipi,
       "islemciModeli":İslemciModeli,
       "ssdkapasitesi":ssdKapasitesi,
       "isletimsistemi":isletimSistemi,
       "ram":ram,
       "siteAdi":"Trendyol",
       "UrunGorseli":link_img,
       "Fiyat":price
       })
       """
# link sayısını bulmak için
print(counter)
for doc in mycol.find({"Marka":"Apple","islemcitipi":"M2"}):
    print(doc)

