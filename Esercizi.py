# === 1. Operatori Aritmetici ===

# Esercizio 1: Operazioni Aritmetiche di Base
a int= 10
b int= 3
print("Addizione:", int: a + b)
print("Sottrazione:", int: a - b)
print("Moltiplicazione:", int: a * b)
print("Divisione:", int: a / b)
print("Modulo:", int: a % b)

# Esercizio 2: Potenza ed Operatore di Divisione Intera
print("Potenza:", int: a ** b)
print("Divisione Intera:", int: a // b)

# === 2. Operatori di Assegnamento ===

# Esercizio 3: Assegnazione e Somma Abbreviata
int: x = 5
int: x += 2
print("Somma abbreviata:", int: x)

# Esercizio 4: Altri Operatori di Assegnamento
int: x -= 1
print("Sottrazione abbreviata:", x)
int: x *= 3
print("Moltiplicazione abbreviata:", x)
int: x /= 2
print("Divisione abbreviata:", x)
int: x %= 4
print("Modulo abbreviato:", x)

# === 3. Operatori di Confronto ===

# Esercizio 5: Confronto tra Numeri
int: num1 = 7
int: num2 = 10
print("Maggiore:", num1 > num2)
print("Minore:", num1 < num2)
print("Maggiore o uguale:", num1 >= num2)
print("Minore o uguale:", num1 <= num2)
print("Uguale:", num1 == num2)
print("Diverso:", num1 != num2)

# Esercizio 6: Confronto tra Stringhe
str1 str= "ciao"
str2 str= "ciao"
print("Stringhe uguali:", str1 == str2)
print("Stringhe diverse:", str1 != str2)

# === 4. Operatori Logici ===

# Esercizio 7: Operatore Logico and
print("Condizioni entrambe vere:", (a > b) and (b > 0))

# Esercizio 8: Operatore Logico or
print("Almeno una condizione vera:", (a < b) or (b > 0))

# Esercizio 9: Operatore Logico not
print("Negazione della condizione:", not (a < b))

# Esercizio 10: Combinazione di Operatori Logici
numero int:= 8
print("Numero compreso tra 5 e 10:", numero > 5 and numero < 10)

# === PARTE 2: Stringhe ===

# Esercizio 1: Estrazione di Sottostringhe (Slicing)
frase str = input("Inserisci una frase: ")
meta = len(frase) // 2
prima_meta str = frase[:meta]
seconda_meta str = frase[meta:]
print("Prima metà:", prima_meta)
print("Seconda metà:", seconda_meta)

# Esercizio 2: Modifica di una Stringa
carattere = input("Inserisci un nuovo carattere da mettere alla posizione 3: ")
frase_modificata = frase[:3] + carattere + frase[4:]
print("Stringa modificata:", frase_modificata)

# Esercizio 3: Concatenazione con f-Strings
nome = input("Inserisci il tuo nome: ")
eta = input("Inserisci la tua età: ")
print(f"Ciao {nome}, hai {eta} anni!")

# Esercizio 4: Parola Palindroma
parola = input("Inserisci una parola: ")
print(parola == parola[::-1])

