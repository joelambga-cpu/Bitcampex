#Esercizio 1
def genera_codice(frase):
    codice = ""
    i = 0

    while i < len(frase):
        carattere = frase[i]

        match carattere:
            case 'a':
                codice += '1'
            case 'e':
                codice += '2'
            case 'i':
                codice += '3'
            case 'o':
                codice += '4'
            case 'u':
                codice += '5'
            case _:
                codice += carattere

        i += 1

    return codice
print(genera_codice("Padrone, non mi mettere in pentola. L'acqua bolle e le patate non sono buone con me"))

#Esercizio 2
def trova_prima_occorrenza(frase, lettera):
    i = 0
    while i < len(frase):
        if frase[i] == lettera:
            return i
        i += 1
    return -1
print(trova_prima_occorrenza("Pdor figlio di Kmer", "o"))
print(trova_prima_occorrenza("Pdor figlio di Kmer", "k"))

#Esercizio 3
def conta_maiuscole_minuscole(stringa):
    maiuscole = 0
    minuscole = 0
    i = 0

    while i < len(stringa):
        if stringa[i].isupper():
            maiuscole += 1
        elif stringa[i].islower():
            minuscole += 1
        i += 1

    return maiuscole, minuscole
maiusc, minusc = conta_maiuscole_minuscole("Questa è Sparta!")
print("Maiuscole:", maiusc)
print("Minuscole:", minusc)

#Esercizio 4
def codice_morse(messaggio):
    morse = ""

    for lettera in messaggio.lower():
        if lettera in "aeiou":
            morse += "·"
        elif lettera.isalpha():
            morse += "-"
    return morse

