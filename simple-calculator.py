import re


def calculate(number_one, operator, number_two):
    operator = normalize_operator(operator)

    if operator == "+":
        return number_one + number_two
    if operator == "-":
        return number_one - number_two
    if operator == "*":
        return number_one * number_two
    if operator == "/":
        if number_two == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        return number_one / number_two

    raise ValueError("Invalid operator. Use +, -, *, or /.")


def normalize_operator(operator):
    return {
        "\u2212": "-",
        "\u00d7": "*",
        "\u00f7": "/",
    }.get(operator, operator)


def parse_expression(expression):
    expression = expression.strip().replace(" ", "")
    match = re.fullmatch(
        r"([+-]?(?:\d+(?:\.\d*)?|\.\d+))"
        r"([+\-\u2212\u00d7\u00f7*/])"
        r"([+-]?(?:\d+(?:\.\d*)?|\.\d+))",
        expression,
    )
    if not match:
        raise ValueError("Enter a calculation such as 12 + 3.")

    number_one = float(match.group(1))
    operator = normalize_operator(match.group(2))
    number_two = float(match.group(3))
    return number_one, operator, number_two


def format_result(result):
    if result.is_integer():
        return str(int(result))
    return str(result)


def clear_calculator():
    return None


def main():
    print("Simple Calculator")
    print("Enter a calculation (for example: 12 + 3)")
    print("Operators: +, -, \u2212, *, \u00d7, /, \u00f7")
    print("Clear the calculator by typing 'clear'.")
    print("Exit by typing 'exit' or 'q'.")

    current_result = None

    while True:
        expression = input("Calculation: ").strip()
        if expression.lower() in ("exit", "q"):
            print("Goodbye!")
            break
        if expression.lower() == "clear":
            current_result = clear_calculator()
            print("Calculator cleared.")
            continue

        try:
            number_one, operator, number_two = parse_expression(expression)
            result = calculate(number_one, operator, number_two)
            current_result = result
            print(f"Result: {format_result(result)}")
        except ZeroDivisionError as error:
            print(f"Error: {error}")
        except ValueError as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()

