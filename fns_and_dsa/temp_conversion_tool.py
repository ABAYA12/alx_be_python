FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
OFFSET = 32

# Conversion Functions


def convert_to_celsius(fahrenheit):
    return (fahrenheit - OFFSET) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + OFFSET

# User Interaction


def main():
    try:
        temperature = float(input("Enter the temperature: "))
        unit = input("Is this in (C)elsius or (F)ahrenheit? ").strip().upper()

        if unit == 'C':
            converted = convert_to_fahrenheit(temperature)
            print(f"{temperature}C is {converted:.2f}F")
        elif unit == 'F':
            converted = convert_to_celsius(temperature)
            print(f"{temperature}F is {converted:.2f}C")
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")


if __name__ == "__main__":
    main()
