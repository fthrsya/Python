from lxml import html
import requests

sehirler={'ankara':'https://namazvakitleri.diyanet.gov.tr/tr-TR/9206/ankara-icin-namaz-vakti'}

a=[]
b=[]

def vakit_getir(sehir):
    path='//*[@id="today-pray-times-row"]'

    r = requests.get(sehirler[sehir])


    x = html.fromstring(r.content)

    tree3 = x.xpath("//*[@id='today-pray-times-row']//*/div[@class='tpt-title']")
    tree4 = x.xpath("//*[@id='today-pray-times-row']//*/div[@class='tpt-time']")

    for c in tree3:
        a.append(c.text)
    for c in tree4:
        b.append(c.text)

    print(sehir +' için namaz vakitleri')

    for c,d in zip(a,b):
        print(c+' : '+d)

vakit_getir("ankara")
