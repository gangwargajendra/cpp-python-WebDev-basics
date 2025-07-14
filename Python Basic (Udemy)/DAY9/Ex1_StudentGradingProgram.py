studentScores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

StudentGrades = {}

for student in studentScores :
    score = studentScores[student]
    if score > 90 :
        StudentGrades[student] = "Outstanding"
    elif score > 80 :
        StudentGrades[student] = "Exceeds Expectations"
    elif score > 70 :
        StudentGrades[student] = "Acceptable"
    else :
        StudentGrades[student] = "Fail"

print(StudentGrades)