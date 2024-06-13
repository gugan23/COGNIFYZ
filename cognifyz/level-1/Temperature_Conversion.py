def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    print("Temperature Conversion Program")
    print("------------------------------")
    print('')
    temp = float(input("Enter the temperature value: "))
    unit = input("Enter the unit of measurement (C for Celsius, F for Fahrenheit): ").strip().upper()

    if unit == 'C':
        converted_temp = celsius_to_fahrenheit(temp)
        print(f"{temp}°C is equal to {converted_temp:.2f}°F")
    elif unit == 'F':
        converted_temp = fahrenheit_to_celsius(temp)
        print(f"{temp}°F is equal to {converted_temp:.2f}°C")
    else:
        print("Invalid unit of measurement. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

if __name__ == "__main__":
    main()
