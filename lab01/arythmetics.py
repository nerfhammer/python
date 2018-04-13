import sys

l1 = int(sys.argv[1])
l2 = int(sys.argv[3])

if (sys.argv[2]=="+"):
	wynik = l1+l2
	w = str(wynik) 
	print("Operacja dodawania: " + sys.argv[1] + sys.argv[2] + sys.argv[3] + "=" + w )

if (sys.argv[2]=="-"):
	wynik = l1-l2
	w = str(wynik)
	print("Operacja odejmowania: " + sys.argv[1] + sys.argv[2] + sys.argv[3] + "=" + w )
	
	
if (sys.argv[2]=="*"):
	wynik = l1*l2
	w = str(wynik)
	print("Operacja mnożenia: " + sys.argv[1] + sys.argv[2] + sys.argv[3] + "=" + w )
	