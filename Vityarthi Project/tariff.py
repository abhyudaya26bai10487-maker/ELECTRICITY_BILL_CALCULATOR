# Electricity tariff information used by the calculator.
# This file is kept separate so that the rates can be changed easily.

SLABS = [
    {"limit": 100, "rate": 3.00},
    {"limit": 200, "rate": 4.50},
    {"limit": 400, "rate": 6.50},
    {"limit": float("inf"), "rate": 8.00}
]

FIXED_CHARGE = 50.00
SURCHARGE_RATE = 0.05
SURCHARGE_LIMIT = 500.00