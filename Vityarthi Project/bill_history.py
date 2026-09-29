from datetime import datetime


def save_bill(customer, units, bill):
    try:
        with open("bill_history.txt", "a", encoding="utf-8") as file:
            date_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

            file.write("\n----------------------------------------\n")
            file.write(f"Date: {date_time}\n")
            file.write(f"Customer Name: {customer['name']}\n")
            file.write(f"Consumer ID: {customer['consumer_id']}\n")
            file.write(f"Units Consumed: {units}\n")
            file.write(f"Energy Charge: Rs. {bill['energy_charge']:.2f}\n")
            file.write(f"Fixed Charge: Rs. {bill['fixed_charge']:.2f}\n")
            file.write(f"Surcharge: Rs. {bill['surcharge']:.2f}\n")
            file.write(f"Total Bill: Rs. {bill['total']:.2f}\n")

    except OSError:
        print("Warning: Bill was calculated, but history could not be saved.")