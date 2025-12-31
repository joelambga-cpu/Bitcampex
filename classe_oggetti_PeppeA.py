class Bike:
    def __init__(self, bike_id:str, modello: str, tariffa_base_ora: float, disponibile=True):
        self.bike_idb = bike_id    ## Ho voluto provare a "privatizzare", nella mia prima versione è senza doppio _ #self.bike_id
        self.modello = modello
        self.tariffa_base_ora = tariffa_base_ora
        self.disponibile = disponibile

    @property
    def modello(self) -> str:
        return self.modello

    @modello.setter
    def modello(self, value: str)
        if not value:
            raise ValueError("Il modello non può essere vuoto.")
        self.modello = value

    @property
    def tariffa_base_ora(self) -> float:
        return self.tariffa_base_ora

    @tariffa_base_ora.setter
    def tariffa_base_ora(self, value) -> None:
        if value < 0:
            raise ValueError("La tariffa deve essere ≥ 0.")
        self.tariffa_base_ora = value

    @classmethod
    def from_string(cls, s):
        parts = s.strip().split(";")
        if parts[0] != "BIKE":
            raise ValueError("Formato non valido per Bike.")
        _, bike_id, modello, tariffa_str, disponibile_str = parts
        return cls(
            bike_id=bike_id,
            modello=modello,
            tariffa_base_ora=float(tariffa_str),
            disponibile=bool(int(disponibile_str))
        )

    def __str__(self):
        return f"Bike({self.bike_id}, {self.modello}, €{self.tariffa_base_ora}/h, Disponibile={self.disponibile})"


class EBike(Bike):
    def __init__(self, bike_id, modello, tariffa_base_ora, disponibile, capacita_batteria_wh, ricarica_rapida):
        super().__init__(bike_id, modello, tariffa_base_ora, disponibile)
        if capacita_batteria_wh <= 0:
            raise ValueError("La capacità della batteria deve essere > 0.")
        self.capacita_batteria_wh = capacita_batteria_wh
        self.ricarica_rapida = ricarica_rapida

    @classmethod
    def from_string(cls, s):
        parts = s.strip().split(";")
        if parts[0] != "EBIKE":
            raise ValueError("Formato non valido per EBike.")
        _, bike_id, modello, tariffa_str, disponibile_str, cap_str, rapida_str = parts
        return cls(
            bike_id=bike_id,
            modello=modello,
            tariffa_base_ora=float(tariffa_str),
            disponibile=bool(int(disponibile_str)),
            capacita_batteria_wh=int(cap_str),
            ricarica_rapida=bool(int(rapida_str))
        )

    def __str__(self):
        return (f"EBike({self.bike_id}, {self.modello}, €{self.tariffa_base_ora}/h, "
                f"Disponibile={self.disponibile}, {self.capacita_batteria_wh}Wh, "
                f"Ricarica rapida={self.ricarica_rapida})")


class Customer:
    def __init__(self, customer_id, nome):
        self.customer_id = customer_id
        self.nome = nome

    @classmethod
    def from_string(cls, s: str)
        parts = s.strip().split(";")
        if parts[0] != "CUST":
            raise ValueError("Formato non valido per Customer.")
        _, customer_id, nome = parts
        return cls (customer_id=customer_id, nome=nome)

    def __str__(self):
        return f"Customer({self.customer_id}, {self.nome})"


b1: Bike = Bike.from_string("BIKE;B005;CityBike;4.5;1")
print(b1)

b2: Bike = Bike.from_string("BIKE;B006;MountainBike;6.5;1")
print(b1)

eb1: EBike = EBike.from_string("EBIKE;E003;MountainE;6.0;0;500;1")
print(eb1)

c1: Customer = Customer.from_string("CUST;C124;Donatella Curreri")
print(c1)

try:
    b_err: Bike = Bike.from_string("BIKE;B002;;3.0;1")  # modello vuoto
except ValueError as e:
    print("Errore:", e)

try:
    eb_err: EBike = EBike.from_string("Ebike;E002;SpeedE;-2.0;1;400;0")  # tariffa negativa e formato Ebike non valido
except ValueError as e:
    print("Errore:", e)

try:
    eb_err2: EBike = EBike.from_string("EBIKE;E003;SpeedE;5.0;1;0;1")  # capacità batteria 0
except ValueError as e:
    print("Errore:", e)

try:
    customer_error: Customer = Customer.from_string("Cust;C456;Barbara Virza")  # Customer non valido
except ValueError as e:
    print('Errore:', e)


class PricingStrategy:
    def calcolo(self, bike, ore: int) -> float:
        raise ('Devi implementare il metodo calcolo')


class StandardPricing(PricingStrategy):
    def calcolo(self, bike, ore: int) -> float:
        return bike.tariffa_base_ora * ore


class EBikePricing(PricingStrategy):
    def calcolo(self, bike, ore: int) -> float:
        base = bike.tariffa_base_ora
        if getattr(bike, 'ricarica_rapida', False):
            return base * 1.2
        return base * 1.1


class Rental:
    def __init__(self, rental_id, customer, bike, ore: int):
        if ore <= 0:
            raise ValueError("Le ore devono essere > 0.")
        if not bike.disponibile:
            raise ValueError("La bici non è disponibile.")
        self.rental_id = rental_id
        self.customer = customer
        self.bike = bike
        self.ore = ore
        self.prezzo_calcolato = None

    def finalizza(self, strategy: PricingStrategy):
        self.prezzo_calcolato = strategy.calcolo(self.bike, self.ore)
        self.bike.disponibile = False

    def __str__(self):
        return (f"Rental({self.rental_id}, {self.customer.nome}, {self.bike.modello}, "
                f"{self.ore}h, €{self.prezzo_calcolato:.2f})")


r1 = Rental("R001", c1, b1, 3)
r1.finalizza(StandardPricing())
print(r1)

r2 = Rental("R002", c1, b2, 4)
r2.finalizza(EBikePricing())
print(r2)

