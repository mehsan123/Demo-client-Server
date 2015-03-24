import socket
import sys
server_addr= '127.0.0.1'

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (server_addr, 8000)

sock.connect(server_address)

message = 'Client: Hello World'
sock.sendall(message)
try:
	while 1:
		data = sock.recv(2012)

	
		if data:
			print data + '\n'
			out = "Client:"
			out = out + raw_input()
			sock.sendall(out)
		#elif !data:
		#	out = raw_input()
		#	sock.sendall(out)
		
		else:
				
			print "No Data"
			sock.close()

	
finally:
	sock.close()

