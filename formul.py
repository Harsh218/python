import sys

# taking no.s for multiplication
s=sys.argv[1:]
mul=1

for i in s:
	mul=mul*int(i)

print(mul)
