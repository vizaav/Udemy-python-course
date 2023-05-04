from art import logo


def add(n1, n2):
    """Add two numbers"""
    return n1 + n2


def subtract(n1, n2):
    """Subtract two numbers"""
    return n1 - n2


def multiply(n1, n2):
    """Multiply two numbers"""
    return n1 * n2


def divide(n1, n2):
    """Divide two numbers"""
    if n2 == 0:
        return "Divide by zero"
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    num1 = float(input("What's the first number?: "))
    num2 = float(input("What's the second number?: "))
    for symbol in operations:
        print(symbol)
    looping = True
    while looping:
        operation_symbol = input("Pick an operation from the line above: ")
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        choice = input("Do you want to continue calculating with the result? Type 'y' or 'n':  \n Type 'e' to exit: ")
        if choice == "y":
            num1 = answer
            num2 = float(input("What's the next number?: "))
        elif choice == "n":
            looping = False
            calculator()
        elif choice == "e":
            looping = False
            print("Goodbye")
        else:
            print("Invalid choice")
            looping = False


print(logo)
calculator()
