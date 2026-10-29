# Project 01 - Interactive Calculator & Unit Converter

def read_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid! Please enter numbers only.")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b

def km_to_miles(km):
    return km * 0.621371

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def main():
    while True:
        print("\n--- Interactive Calculator ---")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Km to Miles")
        print("6. Celsius to Fahrenheit")
        print("7. Quit")

        choice = input("Enter choice 1-7: ")

        if choice == '7':
            print("Thank you! Bye!")
            break

        if choice in ['1','2','3','4']:
            n1 = read_number("Enter first number: ")
            n2 = read_number("Enter second number: ")
            if choice == '1':
                print(f"Result: {add(n1, n2)}")
            elif choice == '2':
                print(f"Result: {subtract(n1, n2)}")
            elif choice == '3':
                print(f"Result: {multiply(n1, n2)}")
            elif choice == '4':
                print(f"Result: {divide(n1, n2)}")

        elif choice == '5':
            km = read_number("Enter km: ")
            print(f"{km} km = {km_to_miles(km)} miles")

        elif choice == '6':
            c = read_number("Enter Celsius: ")
            print(f"{c} C = {celsius_to_fahrenheit(c)} F")

        else:
            print("Invalid choice! Try 1-7")

if __name__ == '__main__':
    main()
