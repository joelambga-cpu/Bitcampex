data = [
    (749.17, "Ritorno agli investimenti"),
    (-11.54, "Spese pedaggio"),
    (-247.58, "Shopping online"),
    (-410.65, "Affitto"),
    (310.60, "Affitto"),
    (563.70, "Regali"),
    (-205.55, "Manutenzione camper"),
    (2200, "Stipendio")
]

def print_transaction(transactions):
    for amount, description in transactions:
        print(f"Importo: {amount} € | Descrizione: {description}")

def print_summary(transactions):
    deposits = [amount for amount, _ in transactions if amount > 0]
    withdrawals = [amount for amount, _ in transactions if amount < 0]

    total_deposited = sum(deposits)
    total_withdrawn = sum(withdrawals)
    balance = total_deposited + total_withdrawn

    print("\n===== RIEPILOGO =====")
    print(f"Totale depositato:  {total_deposited:.2f}€")
    print(f"Totale prelevato:   {total_withdrawn:.2f}€")
    print(f"Saldo totale:       {balance:.2f}€")

print_transaction(data)
print_summary(data)
