print("Calculator")
print("----------")
print('')
def calculator():
    num1 = float(input("Enter the first number: "))
    operator = input("Enter an operator (+, -, *, /, %): ")

    num2 = float(input("Enter the second number: "))
    
    if operator == '+':
        result = int(num1 + num2)
    elif operator == '-':
        result = int(num1 - num2)
    elif operator == '*':
        result = int(num1 * num2)
    elif operator == '/':
        if num2 != 0:
            result = int(num1 / num2)
        else:
            result = "Error! Division by zero."
    elif operator == '%':
        result = int(num1 % num2)
    else:
        result = "Invalid operator!"
    
    print(f"The result is: {result}")

calculator()
