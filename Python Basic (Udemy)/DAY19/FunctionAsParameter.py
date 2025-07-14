def add(n1, n2) :
    return n1 + n2

# calculator is called higher order function in python
def calculator(n1, n2, func) :
    return func(n1, n2)

result = calculator(3, 5, add)

print(f"addition is : {result}.")