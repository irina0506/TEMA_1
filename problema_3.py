#PROBLEMA NR 3
while True:
	n=input("Introduceti anul:")
	n=int(n)
	if n%4==0:
		print("Anul introdus este bisect")
	else:
		print("Anul introdus nu este bisect")
	quit=input("Apasa S pentru iesire si orice tasta pentru a repeta operatiile:")
	if quit.upper()=="S":
		break
	else:
		pass
