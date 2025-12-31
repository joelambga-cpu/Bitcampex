from typing import List


def è_intero_positivo_limitato(s: str) -> bool:
    """
    Controlla se una stringa rappresenta un intero compreso tra 0 e 3.
    Ritorna True solo se è un numero valido nella griglia.
    """
    try:
        valore: int = int(s)
        return 0 <= valore <= 3
    except:
        return False


griglia: List[List[str]] = [
    ['🌊', '🚢', '🌊', '🌊'],
    ['🌊', '🌊', '🚢', '🌊'],
    ['🚢', '🌊', '🌊', '🚢'],
    ['🌊', '🌊', '🌊', '🌊']
]


turni: int = 0
colpi: int = 0
NAVI_TOTALI: int = 4 

print("🎯 Benvenuto alla Battaglia Navale! Trova tutte le navi nascoste!")

while colpi < NAVI_TOTALI:
    print(f"\n Turno {turni + 1}")

 
    riga_input: str = input("Inserisci il numero di riga (0-3): ")
    col_input: str = input("Inserisci il numero di colonna (0-3): ")

    if not (è_intero_positivo_limitato(riga_input) and è_intero_positivo_limitato(col_input)):
        print(" Inserisci solo numeri interi tra 0 e 3.")
        continue

    riga: int = int(riga_input)
    colonna: int = int(col_input)

  
    if griglia[riga][colonna] == '🚢':
        griglia[riga][colonna] = '💥'  # Nave colpita
        colpi += 1
        turni += 1
        print(f"✅ Colpito! Navi rimaste: {NAVI_TOTALI - colpi}")
    elif griglia[riga][colonna] == '💥':
        print(" Hai già colpito questa nave!")
    else:
        print("❌ Mancato.")
        turni += 1

# Fine gioco
print(f"\n🏆 Vittoria! Hai distrutto tutte le navi in {turni} turni.")
