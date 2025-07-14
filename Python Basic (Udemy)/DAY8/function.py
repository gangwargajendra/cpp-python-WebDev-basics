# simple function without parameter
def greet() :
    print("Hello!")
    print("How do you do?")
    print("Isn't the weather nice today?")

greet()

#function that allows for input

def greetWithName(name1) :  # name1 is a parameter
    print(f"Hello {name1}")
    print(f"How do you do {name1}?") 


name = input("Enter your name? ")
greetWithName(name)   # name is an argument


# function that allows more than 1 input

def greetWith(name , feeling) :
    print(f"Hello {name}")
    print(f"How do you do {name}?")
    print(f"you are doing {feeling}.")
 
name = input("Enter your name? ")
feeling = input("how do your feeling? ")

greetWith(name , feeling)

# Positional Parameter

def display(a, b, c) :
    print(f"a = {a}, b = {b}, c = {c}.")

display(1, 2, 3)            # positional Argument
display(a=1, b=2, c=3)      # keyword argument
display(c=3, b=2, a=1)      # keyword argument