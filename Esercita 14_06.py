#Esercizio 1 Somma 1-200
somma = 0
numero = 1

while numero <= 200:
    somma += numero
    numero += 1

print(f"La somma di tutti i numeri da 1 a 200 è: {somma}")

#Esercizio 2 Inserisci nomi fino alla fine

while (nome := input("Inserisci un nome (o 'fine' per terminare): ")) != "fine":
    print(f"Hai inserito: {nome}")

print("Fine dei nomi")

#Esercizio 3 Numeri 1-100 tranne multipli 7
i = 1
while i <= 100:
    if i % 7 != 0:  # Se il numero non è un multiplo di 7
        print(i)
    i += 1
somma = 0

#Esercizio 4
while True:
    numero = float(input("Inserisci un numero (inserisci un numero negativo per terminare): "))

    if numero < 0:
        break

    somma += numero

print(f"La somma di tutti i numeri inseriti è: {somma}")

#Esercizio 5 (Non funziona)
verifiche = 0
somma_note = 0.0

while True:

    nota_input: int = (input('Inserisci la nota (da 1 a 6, o un numero negativo per terminare): ')

    if nota_input < 0:
        break
    if 1 <= nota_input <= 6:
        verifiche += 1
        somma_note += nota_input
        media = somma_note / verifiche
        print(f"Numero di verifiche effettuate: {verifiche}, Media delle note: {media:.2f}")
    else:
        print("Nota non valida. Inserisci una nota tra 1 e 6.")

print("Programma terminato.")

##Parte 2

#Esercizio 1 Quadrato di asterischi
n = int(input("Inserisci la dimensione del lato del quadrato: "))
i = 0
while i < n:
    print('*' * n)
    i += 1


#Esercizio 2 Triangolo di asterischi
n = int(input("Inserisci l'altezza del triangolo: "))

i = 0
while i < n:
    print('*' * (n - i))
    i += 1


#Esercizio 3 Triangolo rovesciato
n = int(input("Inserisci l'altezza del triangolo: "))
i = 1

while i <= n:
    print('*' * i)
    i += 1

#Esercizio 4 Quadrato vuoto (non so farlo 🤷‍♀️)

#Esercizio 5 Piramide centrata
n = int(input("Inserisci il numero di righe per la piramide: "))
i = 1

while i <= n:
    spazi = n - i
    asterischi = 2 * i - 1

    print(' ' * spazi + '*' * asterischi)
    i += 1

#Esercizi 6,7,8 INCAPACE🥴😵🥴

###Parte 3

#Esercizio 1 Tabella Pitagorica
i = 1
while i <= 10:

    b = 1
    while b <= 10:
        print(f"{i * b:3}", end=" ")
        b += 1
    print()
    i += 1

#Esercizio 3 Creare una griglia
n = 5
i = 0
while i < n:

    a = 0
    while a < n:

        print(i + a, end=" ")
        a += 1
    print()
    i += 1

#Esercizi 5,6,7 Non ho capito ⛔