#PROBLEMA NR 5
n=input('''Meniu:
			1-Afisare lista cumparaturi
			2-Adaugare element
			3-Stergere element
			4-Stergere lista cumparaturi
			5-Cautare in lista de cumparaturi
			''')	
while True:
	x=input("Introduceti optiunea dorita:")
	x=int(x)
	if x==1:
		print("Afisare lista cumparaturi")
	elif x==2:
		print("Adaugare element")
	elif x==3:
		print("Stergere element")
	elif x==4:
		print("Stergere lista cumparaturi")
	elif x==5:
		print("Cautare in lista de cumparaturi")
	else:
		print("Alegerea nu exista.Reincercati!")
	quit=input("Apasa S pentru iesire si orice tasta pentru a repeta operatiile:")
	if quit.upper()=="S":
		break
	else:
		pass
