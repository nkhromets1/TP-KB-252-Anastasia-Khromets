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

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: division by zero")
        return None

while True:
    data = getData()

    if data is None:
        print("Program finished.")
        break

    operation, a, b = data

    match operation:
        case "+":
            result = add(a, b)
        case "-":
            result = subtract(a, b)
        case "*":
            result = multiply(a, b)
        case "/":
            result = divide(a, b)

    if result is not None:
        print("Result =", result)