print("Welcome to the rollcoaster")
height = int( input("What is your height in cm : "))
TotalBill = 0

if height >=   120 :
    print("You can ride the rollcoaster!")
    age = int (input("Enter your age : "))
    if(age < 12) :
        # print("You need to pay 5$.....")
        TotalBill = 5
    elif(age <= 18) :
        # print("You neeed to pay 7$..")
        TotalBill = 7
    elif age >= 45 and age <= 55 :
        print("EneryThing is going to be ok. Have a free ride on us.")
    else :
        # print("You need to pay only 12$....")
        TotalBill = 12


    want_Photo = (input ("Are you want photos : Y or N. "))
    if(want_Photo == "Y") :
        TotalBill += 3
    
    print(f"your total bill is ${TotalBill} .")

else :
    print("sorry, you have to grow taller before you can ride.")