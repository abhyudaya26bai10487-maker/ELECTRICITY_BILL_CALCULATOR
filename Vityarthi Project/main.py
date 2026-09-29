from bill_calculator import calculate_bill
from input_handler import get_customer_details, get_units
from bill_history import save_bill
from report import display_bill


def main():
    print("\n========================================")
    print("       ELECTRICITY BILL CALCULATOR")
    print("========================================")

    customer = get_customer_details()
    units = get_units()

    bill = calculate_bill(units)

    display_bill(customer, units, bill)
    save_bill(customer, units, bill)

    print("\nBill generated successfully.")
    print("Thank you for using the Electricity Bill Calculator!")


if __name__ == "__main__":
    main()