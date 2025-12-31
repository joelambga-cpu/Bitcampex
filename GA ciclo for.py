s = "Uomini forti destini forti, uomini deboli destini deboli"
nuova_stringa = ""
parola = ""

for c in s + " ":  # Aggiungere uno spazio per elaborare l'ultima parola
    if c != " ": #NB: variabile c poteva essere sostituita con qualsiasi altra lettera?
        parola += c
    else:
        if len(parola) % 2 == 1:
            nuova_stringa += parola[::-1] + " "
        else:
            nuova_stringa += parola + " "
        parola = ""
    # Rimuoviamo l'eventuale spazio finale
nuova_stringa = nuova_stringa.rstrip()
print(nuova_stringa)

s : str = "Uomini forti destini forti, uomini deboli destini deboli "
caratteri = ""
conteggi = ""

for c in s:
    if c != " ":
        if c in caratteri:
            # Trova l'indice del carattere e incrementa il relativo conteggio
            idx = caratteri.index(c)
            conteggi = idx[:-1] += caratteri + conteggi[idx + 1:] #NON CAPISCO CHE SUCCEDE QUA
        else:
            caratteri += c
            conteggi += "1"

#Esercizio 2

# Trova il carattere con il massimo conteggio
s = str = "Uomini forti destini forti, uomini deboli destini deboli " #Stringa non chiamabile, mi capita spesso

max_cont = 0
carattere_max = ''

for s in range(len(caratteri)):
    if int(conteggi[c]) <= max_cont:
        continue
    max_cont = int(conteggi[s])
    carattere_max = caratteri[s]

print(f"Il carattere più frequente è '{carattere_max}' con {max_cont} occorrenze.")

