
"""
Convert a number from one base to another.

This program converts a number from one base to another. The user can
choose the base of the number to be converted and the base to which it
will be converted. The program will then convert the number and display
the result.
"""

def convert_to_base_10(number, base):
    """Convert number Or string to base 10."""
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    base_10 = 0
    for digit in number:
        base_10 = base_10 * base + digits.index(digit)
    return base_10

def convert_from_base_10(number, base):
    """Convert number from base 10."""
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    new_number = ""
    while number > 0:
        new_number = digits[number % base] + new_number
        number //= base
    return new_number

def get_number():
    """Get the number Or string to convert."""
    while True:
        number = input("Enter the number to convert: ").upper()
        if number.isalnum():
            return number
        print("ERROR: Enter a number or string.")

def get_base_from():
    """Get the base of the number."""
    while True:
        base_from = input("Enter the base of the number: ")
        if base_from.isdigit():
            return int(base_from)
        print("ERROR: Enter a positive integer.")

def get_base_to():
    """Get the base to convert to."""
    while True:
        base_to = input("Enter the base to convert to: ")
        if base_to.isdigit():
            return int(base_to)
        print("ERROR: Enter a positive integer.")

def convert_number(number, base_from, base_to):
    """Convert the number."""
    # Convert number to base 10.
    base_10 = convert_to_base_10(number, base_from)

    # Convert number from base 10.
    new_number = convert_from_base_10(base_10, base_to)

    return new_number

def main():
    """Main function."""
    # Get the number to convert.
    number = get_number()

    # Get the base of the number.
    base_from = get_base_from()

    # Get the base to convert to.
    base_to = get_base_to()

    # Convert the number.
    new_number = convert_number(number, base_from, base_to)

    # Display the result.
    print(f"{number} in base {base_from} is {new_number} in base {base_to}.")

if __name__ == "__main__":
    main()
