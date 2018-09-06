import sys

# taking arguments from command line
num1=sys.argv[1]
num2=sys.argv[2]

try:
#type casting the arguments
	x=float(num1)
	y=float(num2)
	sum=x+y
	if sum%1!=0:
		print(sum)
	elif sum%1==0:
		print(int(sum))

except:
	print("invalid argument")


