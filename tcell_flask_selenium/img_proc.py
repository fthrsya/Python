from PIL import Image
import os

def toplu():
    os.chdir('C:/Users/User/Desktop/Kodlarim/python/selenium_turkcell/static/img')
    i = 0
    for f in os.listdir():
        if f[-3:] == 'png':
            kirp(f)
            i = i + 1

def kirp(x):

    isim=str(x)
    isim1=int(isim[:1])
    isim2=int(isim[:1])

    if isim1==0:
        isim1=0
    else:
        isim1=isim1*2

    if isim2==0:
        isim2=1
    else:
        isim2=isim2*2+1

    isim1=str(isim1)
    isim2=str(isim2)

    im=Image.open(x)
    width, height = im.size

    left = 0
    top = 0
    right = width / 2
    bottom = height

    os.chdir('C:/Users/User/Desktop/Kodlarim/python/selenium_turkcell/static/img/crop')
    im1 = im.crop((left, top, right, bottom))
    im1.save(isim1+'.PNG', "PNG");


    left = width / 2
    top = 0
    right = width
    bottom = height

    im1 = im.crop((left, top, right, bottom))
    im1.save(isim2+'.PNG', "PNG");
    os.chdir('C:/Users/User/Desktop/Kodlarim/python/selenium_turkcell/static/img')


def boyut_sil():
    os.chdir('C:/Users/User/Desktop/Kodlarim/python/selenium_turkcell/static/img/crop')
    i = 0
    for f in os.listdir():
        if f[-3:] == 'PNG':
            a=os.stat(f)
            if a.st_size<10000:
                os.remove(f)


def old_sil():
    os.chdir('C:/Users/User/Desktop/Kodlarim/python/selenium_turkcell/static/img/crop')
    for f in os.listdir():
        if f[-3:] == 'PNG':
            os.remove(f)


#old_sil()
#toplu()
#boyut_sil()
