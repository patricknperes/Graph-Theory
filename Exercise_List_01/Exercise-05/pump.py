class Pump:
    def __init__(self, fuel_type, price_per_liter, fuel_quantity):
        self.fuel_type = fuel_type
        self.price_per_liter = price_per_liter
        self.fuel_quantity = fuel_quantity

    def refuel_by_value(self, value):
        liters_refueled = value / self.price_per_liter
        if liters_refueled <= self.fuel_quantity:
            print(f"Refueled: {liters_refueled:.2f} liters. Total cost: ${value:.2f}")
            self.fuel_quantity -= liters_refueled
        else:
            print("Insufficient fuel quantity in the pump")

    def refuel_by_quantity(self, quantity):
        if quantity <= self.fuel_quantity:
            print(f"Refueled {quantity:.2f} liters. Total cost: ${quantity * self.price_per_liter:.2f}")
        else:
            print("Insufficient fuel quantity in the pump")