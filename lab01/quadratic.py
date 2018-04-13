import sys
import math

# obliczanie miejsc zerowych funkcji kwadratowej

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])
delta = b*b-4*(a*c)

if delta > 0:
	sqrtdelta = math.sqrt(delta)
	print("2 miejsca zerowe")
	x1 = (-b-sqrtdelta)/(2*a)
	x2 = (-b+sqrtdelta)/(2*a)
	print(str(x1) + " " + str(x2))
	
if delta == 0:
	print("1 miejsce zerowe")
	x = (-b)/(2*a)
	print (str(x))
	
if delta <0:
	print("Brak miejsc zerowych")