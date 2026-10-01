student_grades = {
    "Marry": 9.1,
    "Sim": 8.8,
    "John": 7.5
}

print(student_grades)

print(student_grades.keys())
print(student_grades.values())

print("\n-------- sum of all values --------------\n")

total = sum(student_grades.values())
count = len(student_grades)
average = total / count

print(average)