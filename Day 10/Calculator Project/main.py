from art import logo

def add(n1, n2):
    return n1 + n2

# my_favorite_calculation = add
#
# print(my_favorite_calculation(3,5))

# TODO: Write out the other three functions - subtraction, multiplication and division

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(logo)
    continue_calculation = True
    first_number = float(input("Please enter the first number. "))
    for symbol in operations:
        print(symbol)

    while continue_calculation:
        operation_sign = input("Please enter an operation: ")
        second_number = float(input("Please enter the second number. "))
        result = operations[operation_sign](first_number, second_number)
        print(f"{first_number} {operation_sign} {second_number} = {result}")
        to_continue = input("Do you want continue calculation with previous result? Type YES or NO? ").lower()
        if to_continue == "yes":
            first_number = result
        else:
            continue_calculation = False
            print("\n" * 20)
            calculator()

calculator()