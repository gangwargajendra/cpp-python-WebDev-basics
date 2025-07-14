import math

def paintCalculation(height, width, cover) :
    area = height * width
    numOfCans = math.ceil(area / cover)   # used to round nearest greater interger
    print(f"You'll need {numOfCans} cans of paint.")

testHeight = int(input("Height of wall : "))
testWidth = int(input("Width of wall : "))

coverage = 5

paintCalculation(height=testHeight, width=testWidth, cover=coverage)