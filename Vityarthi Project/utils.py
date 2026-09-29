def format_rupees(amount):
    return f"Rs. {amount:.2f}"


def is_valid_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False