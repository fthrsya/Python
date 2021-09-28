from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import pyautogui
import time


import os
from img_proc import *

def giris_yap(x):
    x.get("https://www.turkcell.com.tr/")
    element = x.find_element_by_xpath("/html/body/header/div[2]/div/div[2]/div[2]/div/a[2]/i")
    element.click();
    element1 = x.find_element_by_xpath("/html/body/header/div[3]/div[1]/div[1]/div/div[2]/div/div/div/div/div[1]/div[2]/div/a")
    element1.click();
    element2 = x.find_element_by_xpath('//*[@id="input-1"]')
    element2.click();
  
    element2.send_keys("phone number")

    element3 = x.find_element_by_xpath('//*[@id="input-2"]')
 
    element3.send_keys("pass")

    element3.send_keys("\ue007")
    time.sleep(5)
    try:
        elementreklam = x.find_element_by_xpath('//*[@id="hype-sale-modal"]/a')
        elementreklam.click();
    except:
        print("Reklam yok")

def neoluyor_aga(y):
    i=1
    k=1
    ortak_url = '//*[@id="header-profile"]/div/div[2]/div[2]/div/div[1]/div/'

    while k<7:
        h=str(k)
        while i<3:
            a=str(i)
            paket_kalan_url = 'div['+h+']/div/div[' + a + ']/div/div[2]/div/div[1]'
            url = ortak_url + paket_kalan_url
            kalan_url=ortak_url+paket_kalan_url[:-6]+'div[2]/div/span[2]'
            tur_adı=ortak_url+paket_kalan_url[:-6]+'div[3]'
            kalan_gun = ortak_url + paket_kalan_url[:-6] + 'div[4]/div/strong'
            ozet_kalan=ortak_url+paket_kalan_url[:-17]+'div[1]/h3'
            try:
                print('Paket isimi : ' + y.find_element_by_xpath(url).text)
                print('Paket kalan : ' +y.find_element_by_xpath(kalan_url).text)
                print('Paket Türü : ' + y.find_element_by_xpath(tur_adı).text)
                print('Paket Kalan Gün : ' + y.find_element_by_xpath(kalan_gun).text)
                print('Paket Ozet Kalan : ' + y.find_element_by_xpath(ozet_kalan).text)
            except:
                print("Link yok")

            i = i + 1

        try:
            paket_kalan_url = 'div[' + h + ']/div/div/div/div[2]/div/div[1]'
            url = ortak_url + paket_kalan_url
            kalan_url = ortak_url + paket_kalan_url[:-6] + 'div[2]/div/span[2]'
            tur_adı = ortak_url + paket_kalan_url[:-6] + 'div[3]'
            kalan_gun = ortak_url + paket_kalan_url[:-6] + 'div[4]/div/strong'

            print('Paket isimi : ' + y.find_element_by_xpath(url).text)
            print('Paket kalan : ' + y.find_element_by_xpath(kalan_url).text)
            print('Paket Türü : ' + y.find_element_by_xpath(tur_adı).text)
            print('Paket Kalan Gün : ' + y.find_element_by_xpath(kalan_gun).text)

        except:
            print("Link yok")

        time.sleep(1)
        try:

            tik(y)
        except:
            print("saya kalmadı xxxxxxxx")
        k=k+1




def tik(z):
    #element = driver.find_element_by_xpath(url)
    #element.click();
    a=1
    sms='//*[@id="header-profile"]/div/div[2]/div[2]/div/div[1]/div/div[5]/div/div/div/div[2]/div/div[3]'
    url = "a.a-btn-icon.m-slider__next.a-btn-icon--circle"
    element=z.find_element_by_css_selector(url)
    try:
        if z.find_element_by_xpath(sms).text!='SMS Her Yöne':
            element.click()
            print("tikladım")
            a=0
    except:
        print("bitti")


    time.sleep(1)
    return a

def ekran_al(driver):
    i=1
    os.chdir('C:/Users/User/Desktop/Kodlarim/python/selenium_turkcell')
    element = driver.find_element_by_class_name("swiper-wrapper")
    element.screenshot('./static/img/0.png')
    print("alındı")
    try:
        while i<8:
            if tik(driver)!=1:
                element = driver.find_element_by_class_name("o-header__slider")
                element.screenshot('./static/img/'+str(i)+'.png')
                print("alındı")
            i=i+1
    except:
        print("link yok")

def sil():
    print(os.getcwd())
    os.chdir('C:/Users/User/Desktop/Kodlarim/python/selenium_turkcell/static/img')
    print(os.getcwd())
    for f in os.listdir():
        if f[-3:] == 'png':
            os.remove(f)
   # for f in os.listdir():
   #     print(f)
   #     if f[-3:] == 'png':
    #        os.remove(f)

def cakma_return(x):
    a=''
    b=''
    #a='<img src="/static/img/0.png"></br>'

    os.chdir('C:/Users/User/Desktop/Kodlarim/python/selenium_turkcell/static/img/crop')
    for f in os.listdir():
        a='<img src="/static/img/crop/'+str(f)+'"></br>'
        b=b+a

    return b

def turkcell():
    options = Options()
    options.add_argument("--disable-notifications")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--disable-popup-blocking')
    options.add_argument('--disable-translate')
    #options.add_argument("--headless")
    driver_path = 'C:/Users/User/Desktop/Kodlarim/python/selenium_turkcell/chromedriver.exe'
    driver = webdriver.Chrome(executable_path=driver_path,options=options)
    driver.maximize_window()
    #driver.set_window_size(1366, 768)

    sil()
    old_sil()

    giris_yap(driver)


    ekran_al(driver)
    toplu()
    boyut_sil()

    driver.close()

    os.chdir('C:/Users/User/Desktop/Kodlarim/python/selenium_turkcell/static/img')
    i=0
    for f in os.listdir():
         if f[-3:] == 'png':
            i=i+1


    return cakma_return(i)


def tcell_2_sample():
    kalangun=22
    kalan_sms=990
    toplam_sms=1000
    harcanan_net=5
    kalan_net=25
    toplam_net=30
    kalan_net_yüzdesi=100*kalan_net/toplam_net
    kalan_net_yüzdesi=int(kalan_net_yüzdesi)
    kalan_net_yüzdesi=22
   # kalan_dakika_yüzdesi=100*kalan_dakika/toplam_dakika


    renk_net='bg-success'
    if 75 > kalan_net_yüzdesi > 25:
        renk_net='bg-warning'
    elif kalan_net_yüzdesi<25:
        renk_net='bg-danger'


    return_kalan='''<p align=center>{0} Gün var.</p></br>'''
    return_kalan=return_kalan.format(kalangun)

    return_kalan_net='''<p align=center><img src="/static/img/wifi.svg" > {0} Gb internet <img src="/static/img/wifi.svg"></p></br><div class="progress" border=2 style="height: 30px;"><div class="progress-bar {2}" role="progressbar" style="width: {1}%" aria-valuenow="{1}" aria-valuemin="0" aria-valuemax="100"><h3>%{1}</h3></div></div>'''
    return_kalan_net=return_kalan_net.format(kalan_net,kalan_net_yüzdesi,renk_net)

    return_kalan_dakika = '''<p align=center>{0} Dakika var.</p></br><div class="progress" style="height: 30px;"><div class="progress-bar {2}" role="progressbar" style="width: {1}%" aria-valuenow="{1}" aria-valuemin="0" aria-valuemax="100">%{1}</div></div>'''
    return_kalan_net = return_kalan_net.format(kalan_net, kalan_net_yüzdesi, renk_net)

    return return_kalan+return_kalan_net


#turkcell()
