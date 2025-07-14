print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? y or N ")

totalBill = 0

# cost for size of pizza
if(size == "S"):
    totalBill += 15
elif(size == "M"):
    totalBill += 20
else:
    totalBill += 25

# for the cost of pepperoni
if add_pepperoni == "Y":
    if size == "S":
        totalBill += 2
    else :
        totalBill += 3

# for the cost of extra cheese
if(extra_cheese == "Y"):
    totalBill += 1


print(f"Total bill for your pizza is ${totalBill} .")