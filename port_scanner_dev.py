import socket
import time
import threading
import sys
import os

def active_thread_count():
    while True:
        time.sleep(5)
        if threading.active_count()<3:
            bitis_zamani = time.time()
            calisma_suresi = bitis_zamani - baslangic_zamani
            print(f"Çalışma süresi: {calisma_suresi} saniye")
            sys.exit()


def port_tara(target_host, start_port, end_port):
    for port in range(start_port, end_port + 1):
        soket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        soket.settimeout(1)  # Zaman aşımı süresini ayarlayabilirsiniz
        #print(str(port) +"numaralı port taranıyor ...")
        result = soket.connect_ex((target_host, port))

        if result == 0:
            print(f"Port {port} açık.+++++++++++++++++++++++++++++++++++++")
        soket.close()

def port_tara2(port,parca):
    
    for x in range(port*parca,(port+1)*parca):
        if x<=65535:
            #time.sleep(2)
            soket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            soket.settimeout(1)  # Zaman aşımı süresini ayarlayabilirsiniz
            #print(str(x) +" numaralı port taranıyor ...")
            result = soket.connect_ex((target_host, x))

            if result == 0:
                print(f"Port {x} açık.+++++++++++++++++++++++++++++++++++++")
            soket.close()
        else:
            return 0

target_host="192.168.1.127"
port_max=65535
thread=100
thread_başı_port_tarama_sayısı=port_max/thread
parca=round(thread_başı_port_tarama_sayısı)
print(parca)
print(target_host)

baslangic_zamani = time.time()

def main():
    global range_length, total_requests

    y = threading.Thread(target=active_thread_count, args=())
    y.start()

    try:
        # start threads
        for i in range(thread):
            x = threading.Thread(target=port_tara2, args=(i,parca,))
            x.start()

    except Exception as e:
        print({e})

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nStopped")
        sys.exit()




