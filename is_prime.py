print ("Inserte un número")

n = int(input())

i = 2

while i < n:
	if n % i == 0:
		print ("False")
		break
	i = i + 1
	
else:
		print ("True")
