from operations import getData, performOperation

def main():
    while True:
        data = getData()

        if data is None:
            print("Program finished.")
            break

        operation, a, b = data

        result = performOperation(operation, a, b)

        if result is not None:
            print("Result =", result)

if __name__ == "__main__":
    main()