students = {
    'Alice': 90,
    'Bob': 85,
    'Clara': 95,
    'David': 80
}
print (students.items())
for name, grade in students.items():
    print(f'{name}: {grade}')

average_grade = sum(students.values()) / len(students)
print(f'Průměrná známka: {average_grade}')

top_student = max(students, key=students.get)
print(f'Student s nejvyšší známkou: {top_student} s {students[top_student]} body')



