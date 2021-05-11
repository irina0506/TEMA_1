#PROBLEMA NR 4
while True:
	n=input("Introduceti un numar:")
	n=int(n)
	if n>0 and n<10:
		print("Numarul este pozitiv")
	elif n==0:
		print("Numarul este egal cu zero")
	elif n<0:
		x=abs(n)
		print("Numarul negativ transformat in numar pozitiv este:",x)
	quit=input("Apasa S pentru iesire si orice tasta pentru a repeta operatiile:")
	if quit.upper()=="S":
		break
	else:
		pass
