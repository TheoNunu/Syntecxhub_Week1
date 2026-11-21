var = input(" What do you want to solve? ")
operator = ""
value_1 = ""
value_2 = ""

if var == "+" or var == "addition":
    operator = "+"
    value_1 = float(input("Enter the first number: "))
    value_2 = float(input("Enter the second number: "))
    result = value_1 + value_2
    print(f"The result of {value_1} + {value_2} is: {result}")
elif var == "-" or var == "subtraction":
    operator = "-"
    value_1 = float(input("Enter the first number: "))
    value_2 = float(input("Enter the second number: "))
    result = value_1 - value_2
    print(f"The result of {value_1} - {value_2} is: {result}")
elif var == "*" or var == "multiplication":
    operator = "*"
    value_1 = float(input("Enter the first number: "))
    value_2 = float(input("Enter the second number: "))
    result = value_1 * value_2
    print(f"The result of {value_1} * {value_2} is: {result}")
elif var == "/" or var == "division":
    operator = "/"
    value_1 = float(input("Enter the first number: "))
    value_2 = float(input("Enter the second number: "))
    if value_2 != 0:
        result = value_1 / value_2
        print(f"The result of {value_1} / {value_2} is: {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operator. Please choose from +, -, *, or /.")
 

