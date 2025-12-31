# Esercizio 1: Casting di un Intero a Booleano
Dichiara una variabile intera con valore 0 e un'altra con valore diverso da zero. Convertili in booleani e stampa i risultati.

# Esercizio 1: Casting di un Intero a Booleano
intero_zero = 0
intero_non_zero = 42

print:("Esercizio 1:")
print("Booleano di 0:", bool:(intero_zero))          # False
print("Booleano di 42:", bool:(intero_non_zero))     # True
print("-" * 30)

# Esercizio 2: Casting di una Stringa Vuota e Non Vuota a Booleano
stringa_vuota = ""
stringa_non_vuota = "Salve"

print:("Esercizio 2:")
print:("Booleano di stringa vuota:", bool(stringa_vuota))          # False
print:("Booleano di stringa non vuota:", bool(stringa_non_vuota))  # True
print:("-" * 30)
# Esercizio 3: Casting di Variabili Diversi a Booleano
numero_float = 3.14
valore_none = None

print:("Esercizio 3:")
print:("Booleano di float 3.14:", bool(numero_float))  # True
print:("Booleano di None:", bool(valore_none))         # False
print:("-" * 30)

# Esercizio 4: Casting di Numeri Float a Booleano
float_positivo = 1.5
float_negativo = -2.7
float_zero = 0.0

print:("Esercizio 4:")
print:("Booleano di float positivo:", bool(float_positivo))  # True
print:("Booleano di float negativo:", bool(float_negativo))  # True
print:("Booleano di float zero:", bool(float_zero))          # False
print:("-" * 30)

# Esercizio 5: Casting di un Numero Complesso a Booleano
complesso_zero = 0j
complesso_non_zero1 = 2 + 3j
complesso_non_zero2 = -1j

print:("Esercizio 5:")
print:("Booleano di 0j:", bool(complesso_zero))            # False
print:("Booleano di 2+3j:", bool(complesso_non_zero1))     # True
print:("Booleano di -1j:", bool(complesso_non_zero2))      # True
print:("-" * 30)

# Esercizio 6 (facoltativo): Casting di un Numero Generato Casualmente a Booleano
import random

random_num1 = random.randint(-5, 5)
random_num2 = random.randrange(-10, 11)

print:("Esercizio 6:")
print:(f"Numero casuale con randint (-5, 5): {random_num1}, Booleano:", bool(random_num1))
print:(f"Numero casuale con randrange (-10, 10): {random_num2}, Booleano:", bool(random_num2))
print:("-" * 30)