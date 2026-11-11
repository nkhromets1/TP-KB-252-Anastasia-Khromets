import logging
import os
from operations import Calculator

log_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "calc.log")

logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    force=True
)

print("Log file:", log_file) 

def main():
    calculator = Calculator()

    logging.info("Calculator started")

    while True:
        data = calculator.get_data()

        if data is None:
            print("Program finished.")
            logging.info("Calculator finished")
            break

        operation, a, b = data

        logging.info(f"Input data: {a}, {b}")
        logging.info(f"Operation: {operation}")

        result = calculator.perform_operation(operation, a, b)

        if result is not None:
            print("Result =", result)
            logging.info(f"Result: {result}")
        else:
            logging.error("Operation failed")

if __name__ == "__main__":
    main()

