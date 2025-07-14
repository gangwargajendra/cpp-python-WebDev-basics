from calculatorArt import logo

def add(n1, n2):
    return (n1 + n2)

def subtract(n1, n2):
    return (n1 - n2)

def multiply(n1, n2):
    return round(n1 * n2 , 2)

def divide(n1, n2):
    return round(n1 / n2 , 2)

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}


def calculator() :
    print(logo)
    num1 = float(input("What's the first number?: "))
    for symbol in operations :
        print(symbol)

    isContinue = True
    flag = ""
    result = 0
    while isContinue :
        operation = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))

        function = operations[operation]
        result = function(n1=num1, n2=num2)
        print(f"{num1} {operation} {num2} = {result}")
        flag = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
        if flag == "n" :
            isContinue = False
            calculator()
        elif flag == "y" :
            num1 = result

calculator()