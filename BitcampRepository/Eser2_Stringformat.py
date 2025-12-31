# 1 -Modifica di una stringa
stringa: str = "Python"
nuovo_carattere: str = "X"

# Sostituzione del carattere in posizione 3 (indice 2) #
stringa_modificata: str = stringa[:2] + nuovo_carattere + stringa[3:]

print(stringa_modificata)

# 2 -format()
citta: str = input("Inserisci una città: ")
abitanti: int = int(input("Inserisci il numero di abitanti: "))

frase: str = "La città di {} ha {} abitanti.".format(citta, abitanti)
print(frase)

# 3 -Formattazione numerica
numero_intero: int = int(input("Inserisci un numero intero: "))
numero_decimale: float = float(input("Inserisci un numero decimale: "))

frase: str = "Il numero intero è {} e il numero decimale è {:.2f}".format(
    numero_intero, numero_decimale
)

print(frase)

# 4 -Conta le vocali
testo: str = input("Inserisci una stringa: ")
vocali: str = "aeiou"
conteggio: int = 0

for carattere in testo.lower():
    if carattere in vocali:
        conteggio += 1

print("Numero di vocali:", conteggio)

# 5 -Rimuovi tutte le vocali
testo: str = input("Inserisci una stringa: ")
vocali: str = "aeiou"

risultato: str = ""

for carattere in testo.lower():
    if carattere.lower() not in vocali:
        risultato += carattere

print(risultato)

# 6 -Titoli corrotti
titolo: str = input("Inserisci un titolo: ")

titolo_corretto: str = titolo.title()
titolo_corrotto: str = ""

for carattere in titolo_corretto:
    if carattere.lower() in ("e", "o"):
        titolo_corrotto += "@"
    else:
        titolo_corrotto += carattere

print(titolo_corrotto)

# 7 -Numeri arabi e romani (Match case)
romano: str = input("Inserisci un numero romano: ").upper()
valore: int

match romano:
    case "I":
        valore = 1
    case "V":
        valore = 5
    case "X":
        valore = 10
    case "L":
        valore = 50
    case "C":
        valore = 100
    case "D":
        valore = 500
    case "M":
        valore = 1000
    case _:
        valore = -1

print(valore if valore != -1 else "Numero romano non valido")

# 8 -Gioco delle previsioni
import random

numero_segreto: int = random.randint(1, 10)
tentativo: int = int(input("Indovina il numero (1-10): "))

if tentativo < numero_segreto:
    print("Troppo basso")
elif tentativo > numero_segreto:
    print("Troppo alto")
else:
    print("Esatto!")

# 9 -Scelta personaggio
personaggio: str = input("Scegli un personaggio (guerriero, mago, arciere): ").lower()

match personaggio:
    case "guerriero":
        print("Alta forza e resistenza")
    case "mago":
        print("Poteri magici devastanti")
    case "arciere":
        print("Attacchi rapidi dalla distanza")
    case _:
        print("Personaggio non valido")

# 10 -Due numeri uguali
a: int = int(input("Inserisci il primo numero: "))
b: int = int(input("Inserisci il secondo numero: "))

if a == b:
    print("Sono uguali!")
else:
    print("Non sono uguali!")

# 11 -If senza else
a: int = int(input("Inserisci il primo numero: "))
b: int = int(input("Inserisci il secondo numero: "))

print("I numeri", end=" ")

if a != b:
    print("non", end=" ")

print("sono uguali!")

# 12 -Numero maggiore tra tre
a: int = int(input())
b: int = int(input())
c: int = int(input())

maggiore: int = max(a, b, c)

print("Il maggiore è:", maggiore)

# 13 -Ordine crescente
a: int = int(input())
b: int = int(input())
c: int = int(input())

numeri: list[int] = [a, b, c]
numeri.sort()

print("Risultato:", numeri[0], numeri[1], numeri[2])

# 14 -Anno bisestile
anno: int = int(input("Inserisci un anno: "))

bisestile: bool = (
    (anno % 4 == 0 and anno % 100 != 0) or
    (anno % 400 == 0)
)

print("Bisestile" if bisestile else "Non bisestile")

# 15 -Verifica triangolo
a: int = int(input())
b: int = int(input())
c: int = int(input())

if a + b > c and a + c > b and b + c > a:
    print("Triangolo valido")
else:
    print("Triangolo non valido")

#16 -Tipo di triangolo
a: int = int(input())
b: int = int(input())
c: int = int(input())

if a + b <= c or a + c <= b or b + c <= a:
    print("Non è un triangolo")
elif a == b == c:
    print("Triangolo equilatero")
elif a == b or a == c or b == c:
    print("Triangolo isoscele")
else:
    print("Triangolo scaleno")
