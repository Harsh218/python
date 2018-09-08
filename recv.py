#importing modules
import socket
import matplotlib.pyplot as plt

##              ip_version4,         UDP 
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#defining ip address and port no. 
ip="127.0.0.1"
port=7890
s.bind((ip,port))
i=0
x=[]
a=0
d={}
while i<3:
#recieving data
	data=s.recvfrom(100)
	a=data[0].split()
	for j in a:
		x.append(j)
	i+=1

#identifying unique elements from data
u=set(x)
for j in u:
#counting and appending in dictionary	
	z=x.count(j)
	d.update({j:z})

print(d)
#plotting graph
plt.plot(d.keys(),d.values())
plt.scatter(d.keys(),d.values())
plt.show()

s.close()
