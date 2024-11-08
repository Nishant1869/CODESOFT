# Function to add two numbers
def add(x, y):
    return x + y

# Function to multiply two numbers
def Multiply(x, y):
    return x * y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to divide two numbers
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

# Main program loop
def Simplecalculator():
    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Multiply")
        print("3. subtract")
        print("4. Divide")
        print("5. Exit")

        # Get user input
        choice = input("Enter choice (1/2/3/4/5): ")

        # Check if user wants to exit
        if choice == '5':
            print("Exiting the calculator. Goodbye!")
            break

        # Check if input is valid
        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == '1':
                    print(f"{num1} + {num2} = {add(num1, num2)}")
                elif choice == '2':
                    print(f"{num1} * {num2} = {Multiply(num1, num2)}")
                elif choice == '3':
                    print(f"{num1} - {num2} = {subtract(num1, num2)}")
                elif choice == '4':
                    print(f"{num1} / {num2} = {divide(num1, num2)}")
            except ValueError:
                print("Invalid input. Please enter numeric values.")
        else:
            print("Invalid choice! Please select a valid option.")

# Run the calculator
if __name__ == "__main__":
    Simplecalculator()
