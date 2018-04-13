import sys

n = len(sys.argv)
m = 0
for x in range(n-1, 0, -1):
	if len(sys.argv[x])>2:
		print (sys.argv[x])
		m+=1
print("Znaleziono " + str(m) + " słów dłuższych niż 3 litery i wyświetlono je w odwróconej kolejności")