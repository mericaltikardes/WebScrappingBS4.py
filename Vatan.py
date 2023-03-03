import requests
from bs4 import BeautifulSoup

url="https://www.vatanbilgisayar.com/notebook/?page="
for i in range(1):
    requestForLinksVatan=requests.get(url + str(i + 1))
    soupForLinksVatan = BeautifulSoup(requestForLinksVatan.content, 'html.parser')
    listForLinkVatan = soupForLinksVatan.find_all("div", attrs={"class": "product-list__image-safe"})
    for li in listForLinkVatan:
       li=li.a
       print("https://www.vatanbilgisayar.com"+li.get("href"))
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
       for prc in attsPriceVatan:
           print(prc.text)
       for mrk in attsTitleVatan:
           marka = mrk.text.split(" ")
           print(marka[0])
       for att in attrsListVatan:
           if att.text == 'İşlemci Nesli' and att.findNext().string != ":":
               att = att.findNext().findNext()
               islemciNesli = att.string
               print(att.string)
           if att.text == 'İşlemci Numarası' and att.findNext().string != ":":
               att = att.findNext().findNext()
               islemciNumarasi = att.string
               print(att.string)
           if att.text == 'Ram (Sistem Belleği)' and att.findNext().string != ":":
               att = att.findNext().findNext()
               ram = att.string
               print(att.string)
           if att.text == 'Disk Kapasitesi' and att.findNext().string != ":":
               att = att.findNext().findNext()
               disk = att.string
               print(att.string)
           if att.text == 'İşletim Sistemi' and att.findNext().string != ":":
               att = att.findNext().findNext()
               isletimsistemi = att.string
               print(att.string)
           if att.text == 'Ekran Kartı Tipi' and att.findNext().string != ":":
               att = att.findNext().findNext()
               isletimsistemi = att.string
               print(att.string)
           if att.text == 'Ekran Kartı Chipseti' and att.findNext().string != ":":
               att = att.findNext().findNext()
               isletimsistemi = att.string
               print(att.string)
