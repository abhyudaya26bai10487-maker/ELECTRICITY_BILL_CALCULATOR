from bill_calculator import calculate_bill


def test_bill_for_100_units():
    bill = calculate_bill(100)
    assert bill["energy_charge"] == 300.00
    assert bill["total"] == 350.00


def test_bill_for_200_units():
    bill = calculate_bill(200)
    assert bill["energy_charge"] == 750.00
    assert bill["fixed_charge"] == 50.00
    assert bill["surcharge"] == 37.50
    assert bill["total"] == 837.50


def test_bill_for_400_units():
    bill = calculate_bill(400)
    assert bill["energy_charge"] == 2050.00
    assert bill["surcharge"] == 102.50
    assert bill["total"] == 2202.50


print("Basic bill calculation tests completed.")