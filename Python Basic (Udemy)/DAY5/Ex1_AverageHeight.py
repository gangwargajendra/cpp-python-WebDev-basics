studentHeights = input("Enter the heights of different sudents : ").split(" ")

# in studentHeights list the numbers will be in string form
for n in range(0 , len(studentHeights)) :
    studentHeights[n] = int(studentHeights[n])

print(studentHeights)

sumHeight = 0
# for loop for the list
for height in studentHeights :
    # print(type(height))
    sumHeight += height

averageHeight = round (sumHeight / len(studentHeights))

print(f"Average height of student {averageHeight}.")

# second methods
totalSum = sum(studentHeights)
totalStudent = len(studentHeights)
averageHeight = round (totalSum / totalStudent)

print(f"Average height of student {averageHeight}.")