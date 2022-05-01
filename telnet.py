
import sys
import telnetlib


host=input("enter hostname:")
portno=input("enter host number:")


try:
    conn = telnetlib.Telnet(host,portno)
    response = host+' ' + portno +' - Success'
except:
    response = host+' ' + portno +' - Failed'
finally:
    print(response)
