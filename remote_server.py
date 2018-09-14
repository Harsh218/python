import  socket
import commands
#  we are looking for UDP (user datagram protocol )
#              ip_version4,         UDP 
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# defining ip and port below 
ip="192.168.43.179"
port=7890
i=0
while i<10  :
#  sending  data to  target machine 
	msg=raw_input("enter your message :   ")
	a=commands.getoutput(msg)
# if invalid command found enter again
	if "not found" in a:
		print("Invalid command!! Enter again")
		continue
	s.sendto(msg,(ip,port))
	i+=1
