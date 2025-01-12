import requests
import threading

print ("merhaba")

import requests

url = "example.com"

def istek_yap():
    for i in range(1000):
        response = requests.get(url)


for a in range(30):
    x = threading.Thread(target=istek_yap,)
    x.start()

