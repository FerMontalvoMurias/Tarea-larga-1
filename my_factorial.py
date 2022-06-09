print ("Ingrese un número")

a = int(input())


if a > 0 :
	i = 1
	b = 1
	while b <= a :
		i = i * b
		b = b + 1
	print (i)
