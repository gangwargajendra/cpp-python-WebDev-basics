twoDigitNumber = input("Type a two digit number : ")
print( type(twoDigitNumber)) 

intTotalDigitSum = int(twoDigitNumber[0]) + int(twoDigitNumber[1])

strTotalDigitSum = str(intTotalDigitSum)

print("sum of the digits of " + twoDigitNumber + " is : " + strTotalDigitSum)