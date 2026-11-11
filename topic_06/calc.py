import logging
from operations import getData, performOperation

logging.basicConfig(
    filename="calc.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def main():
    logging.info("Calculator started")

    while True:
        data = getData()

        if data is None:
            print("Program finished.")
            logging.info("Calculator finished")
            break

        operation, a, b = data

        logging.info(f"Input data: {a}, {b}")
        logging.info(f"Operation: {operation}")

        result = performOperation(operation, a, b)

        if result is not None:
            print("Result =", result)
            logging.info(f"Result: {result}")
        else:
            logging.error("Operation failed")

if __name__ == "__main__":
    main()