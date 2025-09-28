CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9


def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        # Get temperature from user
        temperature = float(input("Enter the temperature to convert: "))

        # Get unit (C/F)
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        # Match case for unit
        match unit:
            case "C":
                result = convert_to_fahrenheit(temperature)
                print(f"{temperature}°C is {result}°F")
            case "F":
                result = convert_to_celsius(temperature)
                print(f"{temperature}°F is {result}°C")
            case _:
                print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()
