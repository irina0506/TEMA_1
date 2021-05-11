#PROBLEMA NR 2
while True:
	n=input("Introduceti un numar:")
	n=int(n)
	if n%2 == 0:
		print("Numarul este par")
	else:
		print("Numarul este impar")
	quit=input("Apasati R pentru iesire si orice tasta pentru a repeta operatiile: ")
	if quit.upper()=="R":
		break
	else:
		pass