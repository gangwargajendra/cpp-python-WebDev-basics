age = input("What is your current age : ")

yearsLeft = 90 - int(age)

monthsLeft = yearsLeft * 12
WeeksLeft = yearsLeft * 52
daysLeft = yearsLeft * 365

message = f"you have {daysLeft} days, {WeeksLeft} weeks, and {monthsLeft} months left."

print(message)

# also can do

print(f"you have {daysLeft} days, {WeeksLeft} weeks, and {monthsLeft} months left.")