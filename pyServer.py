import sys
import socket as sck
from threading import Thread

sock = sck.socket(sck.AF_INET,sck.SOCK_STREAM)
SPORT = raw_input("\nENTER SERVER PORT ( > 2000) :\n")
while (int(SPORT) < 2000) :
    SPORT=raw_input("\nERROR :ENTER SERVER PORT AGAIN( > 2000) :\n")
SPORT = int(SPORT)   
sock.bind(("localhost",SPORT))
s = sck.socket(sck.AF_INET,sck.SOCK_DGRAM)
s.connect(("gmail.com",80))
SIP = s.getsockname()[0]
print "\n Server stablished on IP Number %s and port %d \n" %(SIP,SPORT)

sock.listen(5)
newsock,(remhost,remport)=sock.accept()
status = "\n (%s : %d ) Connected ... \n" %(remhost,remport)
print (status)
newsock.send(status)
def recv():
    while True:
        data = newsock.recv(4096)
        if not data: sys.exit(0)
        print ("\n (%s : %d ) >> %s \n" %(remhost,remport,data))

Thread(target=recv).start()
loop = True
while loop:
    data = raw_input(" >> ")
    if not data : newsock.send("not data")
    if data == "finish" : loop = False
    newsock.send(data)
newsock.close()
