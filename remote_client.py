#!/usr/bin/env python2

import  socket
import commands
#  we are looking for UDP (user datagram protocol )
#              ip_version4,         UDP 
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# defining ip and port below 
#ip="192.168.10.201"
port=7890
#  binind ip and port with bind function that takes input as tuple
s.bind(("",port))

# defining  empty list 
x=[]
j=1
for  i in range(10) :
#  now receiving data
	data=s.recvfrom(100)
	print(commands.getoutput(data[0]))
	j+=1
	if j>5 :
		j=1
		print(commands.getoutput("clear"))
s.close()

