# 1. Verifica Numero Positivo, Negativo o Zero
numero = float(input("Inserisci un numero: "))
if numero > 0:
    print("Il numero è positivo.")
elif numero < 0:
    print("Il numero è negativo.")
else:
    print("Il numero è zero.")

# 2. Valutazione Fascia d'Età
eta = int(input("\nInserisci la tua età: "))
if eta < 0:
    print("Età non valida.")
elif eta < 13:
    print("Fascia d'età: bambino")
elif eta < 18:
    print("Fascia d'età: adolescente")
elif eta < 65:
    print("Fascia d'età: adulto")
else:
    print("Fascia d'età: anziano")

# 3. Calcola il Prezzo Scontato
prezzo = float(input("\nInserisci il prezzo del prodotto: €"))
sconto = float(input("Inserisci lo sconto in percentuale (0-100): "))
if 0 <= sconto <= 100:
    prezzo_scontato = prezzo - (prezzo * sconto / 100)
    print(f"Prezzo finale dopo lo sconto: €{prezzo_scontato:.2f}")
else:
    print("Sconto non valido.")
