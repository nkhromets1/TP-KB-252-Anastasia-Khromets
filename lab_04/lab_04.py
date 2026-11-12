import re

PRIORITY = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    'u-': 3,
    '^': 4
}

def infix_to_rpn(expression):
    tokens = re.findall(r'\d+(?:\.\d+)?|[()+\-*/^]', expression)

    if ''.join(tokens).replace(' ', '') != expression.replace(' ', ''):
        raise ValueError("The expression contains unknown symbols")

    output = []
    operators = []
    previous = None

    for token in tokens:

        if re.fullmatch(r'\d+(?:\.\d+)?', token):
            output.append(token)

        elif token == '(':
            operators.append(token)

        elif token == ')':
            while operators and operators[-1] != '(':
                output.append(operators.pop())

            if not operators:
                raise ValueError("Incorrectly placed parentheses")

            operators.pop()

        else:
            if token == '-' and (previous is None or previous in '+-*/^('):
                token = 'u-'
                operators.append(token)
                previous = token
                continue

            while operators and operators[-1] != '(':
                top = operators[-1]

                if PRIORITY[top] > PRIORITY[token] or (
                    PRIORITY[top] == PRIORITY[token] and token != '^'
                ):
                    output.append(operators.pop())
                else:
                    break

            operators.append(token)

        previous = token

    while operators:
        if operators[-1] == '(':
            raise ValueError("Incorrectly placed parenteses")

        output.append(operators.pop())

    return output

def calculate_rpn(tokens):
    stack = []

    for token in tokens:

        if re.fullmatch(r'\d+(?:\.\d+)?', token):
            stack.append(float(token))

        elif token == 'u-':
            if len(stack) < 1:
                raise ValueError("Invalid mathematical expression")

            number = stack.pop()
            stack.append(-number)

        else:
            if len(stack) < 2:
                raise ValueError("Invalid mathematical expression")

            b = stack.pop()
            a = stack.pop()

            if token == '+':
                result = a + b
            elif token == '-':
                result = a - b
            elif token == '*':
                result = a * b
            elif token == '/':
                result = a / b
            elif token == '^':
                result = a ** b

            stack.append(result)

    if len(stack) != 1:
        raise ValueError("Invalid mathematical expression")

    return stack[0]

def main():
    expression = input("Enter a mathematical expression: ")

    try:
        rpn = infix_to_rpn(expression)
        result = calculate_rpn(rpn)

        print("Reverse Polish notation:", ' '.join(rpn))
        print("Calculation result:", result)

    except ZeroDivisionError:
        print("Error: division by 0!")

    except (ValueError, OverflowError) as error:
        print("Error:", error)

if __name__ == "__main__":
    main()