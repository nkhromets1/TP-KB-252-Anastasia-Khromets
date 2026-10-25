from functions import add, subtract, multiply, divide

def getNumber(prompt: str):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Wrong data. Please enter a number.")

def getData():
    while True:
        operation = input("Enter operation (+, -, *, /) or exit: ")

        if operation == "exit":
            return None

        if operation in ["+", "-", "*", "/"]:
            a = getNumber("Enter first number: ")
            b = getNumber("Enter second number: ")
            return operation, a, b

        print("Unknown operation. Try again.")

def performOperation(operation, a, b):
    match operation:
        case "+":
            return add(a, b)
        case "-":
            return subtract(a, b)
        case "*":
            return multiply(a, b)
        case "/":
            return divide(a, b)