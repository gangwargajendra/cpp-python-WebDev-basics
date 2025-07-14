height = input("Enter your height in m : ")
weight = input("Enter your weight in kg : ")

BMI = int(weight) / (float(height) ** 2)
IntBMI = int(BMI)

print("your BMI is : " + str(IntBMI))