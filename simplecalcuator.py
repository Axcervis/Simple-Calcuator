#A Basic Calculator that supports +, -, *, / and pow
# Created by Axcervis

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

def pow(a, b):
    return a ** b

if __name__ == "__main__":
    while True:
        try:
            number1 = float(input("Enter the first number: "))
            number2 = float(input("Enter the second number: "))
        except:
            print("That is not a number!")
            continue

        operator = input("Enter an operator (valid operators are +, -, *, / and pow): ")

        #Check if user operator is a valid one
        if operator == "+":
            func = add
        elif operator == "-":
            func = sub
        elif operator == "*":
            func = mul
        elif operator == "/":
            func = div
        elif operator == "pow":
            func = pow
        else:
            print("Invalid operator!")
            continue

        #Print result
        print(func(number1, number2))
