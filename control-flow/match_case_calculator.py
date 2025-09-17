number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

match operation:
    case "+":
        result = number1 + number2
    case "-":
        result = number1 - number2
    case "*":
        result = number1 * number2
    case "/":
        if number2 != 0:
            result = number1 / number2
        else:
            result = "Cannot divide by zero."
    case _:
        result = "Invalid operation selected."
if isinstance(result, str):
    print(result)
else:
    print(f"The result is {result}.")