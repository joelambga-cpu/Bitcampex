# Esercizio 1 Higher Function
# a
def inverti_segnale(numero, operazione):
 risultato = operazione(numero)
 if risultato < 0:
  return -risultato
 else:
  return risultato


print(inverti_segnale(5, lambda x: x - 10))
print(inverti_segnale(2, lambda x: x + 3))


# b
def moltiplica_per_negativo_due(x):
 return x * -2




def quadrato_meno_venti(x):
 return x ** 2 - 20


print(inverti_segnale(4, moltiplica_per_negativo_due))
print(inverti_segnale(3, quadrato_meno_venti))

#Esercizio 2 Closure segreta
def crea_ricorda_stringa():
 segreta = ""

 def salva_stringa(stringa):
  nonlocal segreta
  segreta = stringa

 def inverti_stringa():
  return segreta[::-1]

 return salva_stringa, inverti_stringa

salva, inverti = crea_ricorda_stringa()
salva("Python è bello!")
print(inverti())  # Output: !olleb è nohtyP

#Esercizio 3 Funzioni di formattazione
from functools import partial

def inquadra_testo(testo, bordo_sinistro, bordo_destro):
    return bordo_sinistro * 2 + testo + bordo_destro * 2

inquadra_con_stelle = partial(inquadra_testo, bordo_sinistro='"', bordo_destro='"')

print(inquadra_con_stelle("ciao"))

#Eserzizio 4 Lambda Challenge

operatore_magico = (
    lambda a, b, c:
        (lambda somma: somma if somma >= 0 else -somma)(
            (a if a > b else b) + (lambda x: x * x)(c)
        )
)
print(operatore_magico(3, 7, -4))
print(operatore_magico(-5, -2, 3))
print(operatore_magico(10, 5, 0))

#Esercizio 5 Closure creativa

from functools import partial

def crea_annunciatore(prefisso):
    def annuncia(numero, unita):
        return f"{prefisso} {numero} {unita}"
    return annuncia


tra_tempo = crea_annunciatore("Tra")
print(tra_tempo(5, "minuti"))        # Tra 5 minuti
print(tra_tempo(3, "secondi"))       # Tra 3 secondi

mancano_10 = partial(crea_annunciatore("Mancano"), 10)
restano_ore = partial(crea_annunciatore("Restano"), unita="ore")

print(mancano_10("secondi"))         # Mancano 10 secondi
print(restano_ore(2))                # Restano 2 ore

##PARTE 2 ##
#ACCESS LIST ITEMS

def accesso_elemento(lista, indice):
 if 0 <= indice < len(lista):
  return lista[indice]
 else:
  return "Indice fuori dal range"

 print(accesso_elemento(frutta, 1))  # Output: "banana"
 print(accesso_elemento(frutta, 5))  # Output "Indice fuori dai ranghi"
 print(accesso_elemento(frutta, -1))  # Output: "Indice fuori dai ranghi"

##CHANGE LIST ITEMS

def cambia_elemento(lista, indice, nuovo_valore):
 if -len(lista) <= indice < len(lista):
  lista[indice] = nuovo_valore
  return lista
 else:
  return "Indice fuori dal range"
numeri = [10, 20, 30, 40]  #Qui mi dava errore unreachable

print(cambia_elemento(numeri, 2, 99))   # Output: [10, 20, 99, 40]
print(cambia_elemento(numeri, -1, 0))   # Output: [10, 20, 99, 0]
print(cambia_elemento(numeri, 10, 5))   # Output:  "Indice fuori dai ranghi"

##ADD LIST ITEMS
lista = []
elemento = input("Inserisci un elemento da aggiungere alla lista: ")
lista.append(elemento) #Sarà in coda....

print("Lista aggiornata:", lista)

##REMOVE LIST ITEMS
frutti: list[str] = ['mela', 'pera','banana','cocco','pesca','fragola']
el_to_del: str = frutti.pop()
if el_to_del in frutti: frutti.remove(el_to_del)
print(frutti)
print(frutti.remove(el_to_del))

###PARTE 3###

##SOMMA DI UNA LISTA

def somma_lista(lista):
 if not lista:
  return 0
 else:
  return lista[0] + somma_lista(lista[1:])

numeri = [1, 2, 3, 4, 5]
risultato = somma_lista(numeri)
print("La somma dei numeri è:", risultato)
