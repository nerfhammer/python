import sys

def histogram(tekst):
    wynik={}
    uzyteLitery=[]
    n=0
    for x in tekst:
        if x in uzyteLitery or x == ' ':
            continue
        uzyteLitery.append(x)
        for a in tekst:
            if(x==a):
                n+=1
        wynik[x]=n
        licznik=0
    return wynik

tekst_input = input("Wprowadz tekst : ")
print(histogram(tekst_input))