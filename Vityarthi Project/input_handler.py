def get_customer_details():
    print("\nEnter customer details")
    print("----------------------")

    while True:
        name = input("Customer name: ").strip()
        if name:
            break
        print("Name cannot be empty.")

    while True:
        consumer_id = input("Consumer ID: ").strip()
        if consumer_id:
            break
        print("Consumer ID cannot be empty.")

    return {
        "name": name,
        "consumer_id": consumer_id
    }


def get_units():
    while True:
        try:
            units = float(input("Enter electricity units consumed: "))

            if units < 0:
                print("Units cannot be negative.")
            else:
                return units

        except ValueError:
            print("Please enter a valid number.")
