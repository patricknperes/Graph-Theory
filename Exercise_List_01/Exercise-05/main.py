from pump import Pump
import os

os.system("cls")

gasoline_pump = Pump(fuel_type="Gasoline", price_per_liter=5.0, fuel_quantity=100.0)

gasoline_pump.refuel_by_value(50.0)
gasoline_pump.refuel_by_quantity(10.0)
