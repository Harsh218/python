from random import choice,choices
import time

points={1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:10,"Jack":10,"Queen":10,"King":10,"Ace":(1,11)}
a=list(points.keys())
print(a)

p_sum=0
d_sum=0
flag=False
d_card1,d_card2=choices(a,k=2)
p_card1,p_card2=choices(a,k=2)

print(d_card1,d_card2,p_card1,p_card2)

def black_jack(c,d):
	global p_sum,d_sum

	if c == "Ace":
		p_sum+=11
	else:
		p_sum+=points[c]

	if d == "Ace":
		if c=="Ace":
			p_sum+=1
		else:
			p_sum+=11
	else:
		p_sum+=points[d]
	print(p_sum)
	if p_sum==21:
		return True
	else:
		return False


def hit(z):
	global p_sum,d_sum
	r=choice(a)
	if z=="p":
		print("You got: ",r)
		if r=="Ace":
			if p_sum+11>21:
				p_sum+=1
			else:
				p_sum+=11
		else:
			p_sum+=points[r]
	elif z=="d":
		print("Dealer got: ",r)
		if r=="Ace":
			if d_sum+11>21:
				d_sum+=1
			else:
				d_sum+=11
		else:
			d_sum+=points[r]
		time.sleep(2)

'''
def check(l):
	if l>21:
		return True
	elif l==21:
		return "Stand"
	else:
		return False
'''

def dealer_sum(c,d):
	global d_sum

	if c == "Ace":
		d_sum+=11
	else:
		d_sum+=points[c]

	if d == "Ace":
		if c=="Ace":
			d_sum+=1
		else:
			d_sum+=11
	else:
		d_sum+=points[d]









if black_jack(p_card1,p_card2):
	print("Player Won the Bet")
	flag=True
else:
	while True:
		x=input("do u want to Hit or Stand: ")
		if x=="Hit":
			hit("p")
			if p_sum>21:
				print("You Lost the Bet")
				flag=True
				break
			elif p_sum==21:
				print("you are done as ur sum is 21")
				break
			else:
				print("Our sum is now: ",p_sum)				
				continue
		elif x=="Stand":
			print("Player's sum is: ",p_sum)
			break
		else:
			print("only Hit/Stand")
			continue


dealer_sum(d_card1,d_card2)

if flag==True:
	print("Game over")
else:
	print("Dealer's sum is: ",d_sum)
	if d_sum>p_sum:
		print("You Lost")
	else:
		while True:
			hit("d")
			if d_sum>21:
				print("You Won")
				break
			elif d_sum>p_sum:
				print("You Lost")
				break
			else:
				print("His sum is now: ",d_sum)
				time.sleep(3)
				continue
	print("Game Over Now")



















