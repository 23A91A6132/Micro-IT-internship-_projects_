import math

def display_menu():
    print("\nAdvanced Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Power")
    print("7. Square Root")
    print("8. Logarithm (base 10)")
    print("9. Sine")
    print("10. Cosine")
    print("11. Tangent")
    print("0. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (0-11): ")

        if choice == '0':
            print("Exiting calculator. Goodbye!")
            break

        try:
            if choice in ['1', '2', '3', '4', '5', '6']:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == '1':
                    print(f"Result: {num1 + num2}")
                elif choice == '2':
                    print(f"Result: {num1 - num2}")
                elif choice == '3':
                    print(f"Result: {num1 * num2}")
                elif choice == '4':
                    if num2 == 0:
                        print("Error: Division by zero!")
                    else:
                        print(f"Result: {num1 / num2}")
                elif choice == '5':
                    print(f"Result: {num1 % num2}")
                elif choice == '6':
                    print(f"Result: {num1 ** num2}")

            elif choice == '7':
                num = float(input("Enter number: "))
                print(f"Square root of {num} is {math.sqrt(num)}")

            elif choice == '8':
                num = float(input("Enter number: "))
                if num <= 0:
                    print("Error: Logarithm not defined for non-positive numbers.")
                else:
                    print(f"log10({num}) = {math.log10(num)}")

            elif choice in ['9', '10', '11']:
                angle = float(input("Enter angle in degrees: "))
                radians = math.radians(angle)

                if choice == '9':
                    print(f"sin({angle}) = {math.sin(radians)}")
                elif choice == '10':
                    print(f"cos({angle}) = {math.cos(radians)}")
                elif choice == '11':
                    print(f"tan({angle}) = {math.tan(radians)}")

            else:
                print("Invalid choice. Please choose from the menu.")

        except ValueError:
            print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()
