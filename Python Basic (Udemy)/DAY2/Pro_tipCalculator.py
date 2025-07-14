print("Welcome to the tip calculator.")
amount = input("What was the total bill? $")
people = input("How many people to split the bill? ")
tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
totalAmount = float(amount) + ( float(amount) * int(tip) ) / 100
perPersonAmount = totalAmount / int(people)

finalAmount1 = round(perPersonAmount , 2)
finalAmount2 = "{:.2f}".format(perPersonAmount)

print(f"Each person should pay using round : ${finalAmount1}")
print(f"Each persono should pay using format : ${finalAmount2}")