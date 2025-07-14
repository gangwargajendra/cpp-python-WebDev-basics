StudentScore = input("Enter the students marks : ").split()

for n in range(0 , len(StudentScore)) : 
    StudentScore[n] = int(StudentScore[n])

print(StudentScore)

maxScore = 0
for mark in StudentScore:
    if maxScore < mark :
        maxScore = mark

print(f"The highest score in the class is : {maxScore}.")

# second method

print(f"maximum marks = {max(StudentScore)}.")
print(f"Minimum marks : {min(StudentScore)}.")