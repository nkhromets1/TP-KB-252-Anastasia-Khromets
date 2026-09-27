def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b 

def divide(a, b):
    return a / b

while True:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    operation = input("Enter operation (+, -, *. /) or exit: ")

    if operation == "exit":
        print("Program finished")
        break

    match operation: 
        case "+":
            print("Result=", add(a, b))
        case "-":
            print("Result=", subtract(a, b))
        case "*":
            print("Result=", multiply(a, b))
        case "/":
            print("Result=", divide(a, b))
        case _:
            print ("Unknown operation")
    