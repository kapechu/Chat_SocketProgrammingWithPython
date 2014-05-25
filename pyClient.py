import sys
import socket as sck
from threading import Thread

sock = sck.socket(sck.AF_INET,sck.SOCK_STREAM)

CPORT = raw_input("\nENTER Client PORT ( > 2000) :\n")
while int(CPORT) < 2000 :
    CPORT=raw_input("\nERROR :ENTER Client PORT AGAIN( > 2000) :\n")
CPORT = int(CPORT)
sock.bind(("localhost",CPORT))
print "\n Client stablished on port %d \n" %CPORT

SPORT = raw_input("\nENTER SERVER PORT ( > 2000) :\n")
while int(SPORT) < 2000 :
    SPORT=raw_input("\nERROR :ENTER SERVER PORT AGAIN( > 2000) :\n")
SPORT = int(SPORT)   
SIP = raw_input("\nENTER SERVER IPAddres :\n")
SADDR=(SIP,SPORT)
sock.connect(SADDR)
status = sock.recv(4096)
print (status)

def recv():
    while True:
        data = sock.recv(4096)
        if not data: sys.exit(0)
        print ("\n (%s : %d ) >> %s \n" %(SIP,SPORT,data))
	


loop = True
while loop:
    Thread(target=recv).start()
    data = raw_input(" >> ")
    if not data : sock.send("not data")
    if data == "finish" : loop = False
    sock.send(data)
sock.close()

