weight = int( input ("Enter your weight (kg): "))
height = float( input("Enter your height (m): "))


BMI = round (weight / height ** 2  , 2)

print(f"Your BMI is : {BMI}")

if(BMI < 18.5) :
    print("He is Under-weight...")
elif(BMI < 25) :
    print("Hi is normal weight...")
elif(BMI < 30) :
    print("he is OverWeight...")
elif(BMI < 35) :
    print("He is obses...")
else :
    print("He is clinically obese...")