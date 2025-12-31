print()
print('###ESERCIZIO 1###')
print ()
x: int = 7
y: int = 9

somma: int= x + y
sottrazione: int = x -1
prodotto: int = x - 1
divisone: float = x/y
resto: int = x % y

print(f'''
      La somma di {x} e {y} è: {somma}
	  La sottrazione di {x} e {y} è: {sottrazione}
	  Il prodotto di {x} e {y} è: {prodotto}
	  Il resto di {x} e {y} è: {resto}
''')

print('###ESERCIZIO 2###')
print()

potenza: int= x ** y
divisione_intera: int = x // y

print(f'''
		La potenza di {x} elevato a {y} è: {potenza}
		La divisione intera di {x} e {y} è: {divisione_intera}
''')

print()
print('###ESERCIZIO 3###')
print()

a: int = 9
print(f'Il valore di a è: {a}')

a += 2
a -= 5
a *= 1
a /= 7
a %= 2

a: int = 9
print(f'Il valore di {a} incrementato è: {a + 1}')
print(f'Il valore di {a} decrementato è: {a - 1}')
print(f'Il valore moltiplicato di {a} è: {a * 2}')
print(f'Il valore diviso di {a} è: {a / 2}')


print()
print('###ESERCIZIO 4###')
print()

numero1: int= 76
numero2: int= 37

print(f'''
    Il numero {numero1} è maggiore di {numero2}? : {numero1 > numero2}
    Il numero {numero1} è minore di {numero2}? : {numero1 < numero2}
    Il numero {numero1} è maggiore o uguale a {numero2}? : {numero1 >= numero2}
    Il numero {numero1} è minore o uguale a {numero2}? : {numero1 <= numero2}
    Il numero {numero1} è uguale a {numero2}? : {numero1 == numero2}
    Il numero {numero1} è diverso da {numero2}? : {numero1 != numero2}
''')