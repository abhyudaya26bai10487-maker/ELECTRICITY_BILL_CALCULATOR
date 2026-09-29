from tariff import FIXED_CHARGE, SURCHARGE_LIMIT, SURCHARGE_RATE


def calculate_bill(units):
    """Calculate electricity charges using simple slab rates."""

    if units <= 100:
        energy_charge = units * 3.00
    elif units <= 200:
        energy_charge = (100 * 3.00) + ((units - 100) * 4.50)
    elif units <= 400:
        energy_charge = (100 * 3.00) + (100 * 4.50) + ((units - 200) * 6.50)
    else:
        energy_charge = (
            (100 * 3.00)
            + (100 * 4.50)
            + (200 * 6.50)
            + ((units - 400) * 8.00)
        )

    if energy_charge > SURCHARGE_LIMIT:
        surcharge = energy_charge * SURCHARGE_RATE
    else:
        surcharge = 0.00

    total = energy_charge + FIXED_CHARGE + surcharge

    return {
        "energy_charge": energy_charge,
        "fixed_charge": FIXED_CHARGE,
        "surcharge": surcharge,
        "total": total
    }
