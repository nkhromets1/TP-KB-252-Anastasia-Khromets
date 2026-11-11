from functions import CalculatorFunctions

class Calculator:
    def __init__(self):
        self.functions = CalculatorFunctions()

    def get_number(self, prompt):
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Wrong data. Please enter a number.")

    def get_data(self):
        while True:
            operation = input("Enter operation (+, -, *, /) or exit: ")

            if operation == "exit":
                return None

            if operation in ["+", "-", "*", "/"]:
                a = self.get_number("Enter first number: ")
                b = self.get_number("Enter second number: ")
                return operation, a, b

            print("Unknown operation. Try again.")

    def perform_operation(self, operation, a, b):
        match operation:
            case "+":
                return self.functions.add(a, b)
            case "-":
                return self.functions.subtract(a, b)
            case "*":
                return self.functions.multiply(a, b)
            case "/":
                return self.functions.divide(a, b)