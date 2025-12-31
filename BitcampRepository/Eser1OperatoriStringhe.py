# 1
# Si dichiarano due variabili intere e si applicano le operazioni aritmetiche fondamentali #

a: int = 10
b: int = 3

somma: int = a + b
sottrazione: int = a - b
moltiplicazione: int = a * b
divisione: float = a / b
modulo: int = a % b

print("Somma:", somma)
print("Sottrazione:", sottrazione)
print("Moltiplicazione:", moltiplicazione)
print("Divisione:", divisione)
print("Modulo:", modulo)
# 2 -Potenza e divisione intera
base: int = 2
esponente: int = 5
potenza: int = base ** esponente

x: int = 17
y: int = 4
divisione_intera: int = x // y

print("Potenza:", potenza)
print("Divisione intera:", divisione_intera)

# 3 -Assegnazione e somma abbreviata
numero: int = 10
numero += 5

print("Risultato:", numero)

##Altri operatori di assegnamento##
numero -= 3
print("Dopo -= :", numero)

numero *= 2
print("Dopo *= :", numero)

numero //= 4
print("Dopo //= :", numero)

numero %= 3
print("Dopo %= :", numero)

# 5 -Confronto tra numeri
n1: int = 7
n2: int = 10

print(n1 > n2)
print(n1 < n2)
print(n1 >= n2)
print(n1 <= n2)
print(n1 == n2)
print(n1 != n2)

# 6 -Confronto tra stringhe
s1: str = "python"
s2: str = "Python"

uguali: bool = s1 == s2
diverse: bool = s1 != s2

print("Uguali:", uguali)
print("Diverse:", diverse)

# 7 -Operatore logico and
eta: int = 20
patente: bool = True

puo_guidare: bool = eta >= 18 and patente
print("Può guidare:", puo_guidare)

# 8 -Operatore logico or
giorno_festivo: bool = False
weekend: bool = True

riposo: bool = giorno_festivo or weekend
print("Giorno di riposo:", riposo)

# 9 -Operatore logico not
piove: bool = False
non_piove: bool = not piove

print("Non piove:", non_piove)

# 10 -Combinazione di operatori logici
numero: int = 15

compreso: bool = 10 <= numero <= 20
print("Compreso tra 10 e 20:", compreso)

# 11 -Slicing
frase: str = input("Inserisci una frase: ")

lunghezza: int = len(frase)
meta: int = lunghezza // 2

prima_parte: str = frase[:meta]
seconda_parte: str = frase[meta:]

print("Prima metà:", prima_parte)
print("Seconda metà:", seconda_parte)

# 12 -Modifica simulata di una stringa
nuovo_carattere: str = input("Inserisci un carattere: ")

stringa_modificata: str = (
    frase[:3] + nuovo_carattere + frase[4:]
)

print("Stringa modificata:", stringa_modificata)

# 13 -Concatenazione con f-string
nome: str = input("Inserisci il nome: ")
eta: int = int(input("Inserisci l'età: "))

messaggio: str = f"Ciao {nome}, hai {eta} anni!"
print(messaggio)


# 14 -Parola palindroma
parola: str = input("Inserisci una parola: ")

inversa: str = parola[::-1]
palindroma: bool = parola == inversa

print("È palindroma:", palindroma)


