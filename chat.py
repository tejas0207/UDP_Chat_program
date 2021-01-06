import socket
import threading
s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
winip = "x.x.x.x"
serverport = 1234
linip = "x.x.x.x"
s.bind((winip , serverport))
def a():
	while True:
		x = s.recvfrom(30)
		text = x[0].decode()
		print("")
		print ("Linux \t:\t " , end =" ")
		print (text)
		
def b():
	while True:
		msg = input("you(win) :\t")
		msg1 = msg.encode()
		s.sendto(msg1 , (linip , serverport))
print("\t\t\tWELCOME TO CHAT APPLICATION")

x1 = threading.Thread( target=a)
x2 = threading.Thread( target=b)

x1.start()
x2.start()
