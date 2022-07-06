import telnetlib
import os
host="10.35.37.175"
portno="21"
try:
    conn = telnetlib.Telnet(host,portno,5)
    response = host+' ' + str(portno) +' - Success'
    print(response)
    #os.system('source ~oracle/.bash_profile;set_DMRCNV;sqlplus / as sysdba << EOF \n begin fkuyuk.mail(); end; \n / \n EOF')
except:
    response = host+' ' + str(portno) +' - Failed'
    print(response)
    os.system('source ~oracle/.bash_profile;set_DMRCNV;sqlplus / as sysdba << EOF \n begin fkuyuk.mail(); end; \n / \n EOF')
