#2.1
student = {'name': 'Adam', 'assignment': [82, 56, 44, 30], 'lab': [78.2, 77.2], 'test': [78, 77]}
print(student)

#2.2
submission_check = {student['name']: len(student['assignment']) + len(student['lab']) + len(student['test'])}
print(submission_check)

#2.3
student['final_grade'] = (
    0.3 * sum(student['assignment']) + 0.4 * sum(student['lab']) + 0.3 * sum(student['test'])
    if submission_check[student['name']] >= 4 else 0
)
print(student)

#2.4
student2 = {'name': 'Kevin', 'assignment': [82, 30], 'lab': [78.2], 'test': [], 'final_grade': 0}
students = {s['name']: s for s in [student, student2]}
print(students)
