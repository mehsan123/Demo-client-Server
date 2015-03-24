import socket
import os

p = 8000
ip_add = ('127.0.0.1',p)


serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(ip_add)
serversocket.listen(5)
(clientsocket, address) = serversocket.accept()
try:
	while 1:
		data = clientsocket.recv(2012)
		
		if data == "Client:close":
			out = "Server: Ok! I am closing! Good bye!"
			clientsocket.sendall(out)
			clientsocket.close()
		
		if data:
			print data
			out = "Server:"
			out= out+ raw_input()
			clientsocket.sendall(out)
			

		else:
			print " No Data"

		
	
finally:
	
	clientsocket.close()



