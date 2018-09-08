import socket
#              ip_version4,         UDP 
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#defining ip address  and port no.
ip="127.0.0.1"
port=7890
i=0
while i<3:
#sending data 
	msg=raw_input()
	s.sendto(msg.encode(),(ip,port))
	i+=1

