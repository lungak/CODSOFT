
# Functions for operators
def ADD(x, y):
    return x + y

def SUBT(x, y):
    return x - y

def MULT(x, y):
    return x * y

def DIVISION(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"

def calculator():
    try:
        num1 = float(input("Enter the first number: "))
        operator = input("Enter the operator (+, -, *, /): ")
        num2 = float(input("Enter the second number: "))

        if operator == '+':
            result = ADD(num1, num2)
        elif operator == '-':
            result = SUBT(num1, num2)
        elif operator == '*':
            result = MULT(num1, num2)
        elif operator == '/':
            result = DIVISION(num1, num2)
        else:
            result = "Error: Invalid operator"

        print(f"Result: {result}")

# Accounting for errors that might occur when the user inserts and invalid input and/or any other errors that might occur.
    except ValueError:
        print("Error: Please enter valid numbers.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    calculator()
