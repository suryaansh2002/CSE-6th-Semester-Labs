import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

udp_host = socket.gethostname()
udp_port = 12345

print('Do Ctrl+c to exit the program!!')
while True:
	message = input('Msg to send')
	s.sendto(message.encode(),(udp_host,udp_port))
	data = s.recv(1024)
	print('Msg Recieved: ', data.decode())