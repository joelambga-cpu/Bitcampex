italian_food = ["Pasta alla Bolognese", "Pizza margherita", "Lasagna", "Pollo allo spiedo"]
indian_food = ["Curry", "Chutney","Samosa","Naan"]

def find_meal(name, menu):
    return name if name in menu else None

def select_meal(name,food_type):
    if food_type == f"Italian.strip()":
        return find_meal(name, italian_food)
    elif food_type == f"Indian.strip()":
        return find_meal(name, indian_food)
    else:
        return None

def display_available_meals(food_type):
    if food_type == f"Italian.strip()":
     print("Disponibile il menu della cucina più buona del mondo")
     for meal in italian_food:
        print(meal)
    elif food_type == f"Indian.strip()":
        print("Complimenti hai deciso di mangiare speziato")


def create_summary(name, amount,food_type):
    order = select_meal(name,food_type)
    if order:
        return f"Hai ordinato {amount} di {name}"
    else:
        return "Cibo non trovato!"

print("Benvenuti nel menu Mille sapori: ")
type_input = input("Inserisci il tipo di cucina che vuoi ordinare: ")
display_available_meals(type_input)
name_input = input("Inserisci il nome nel menu che vuoi ordinare: ")
amount_input = int(input("Seleziona la quantità che vuoi ordinare: "))

result = create_summary(name_input, amount_input,type_input)
print(result)
