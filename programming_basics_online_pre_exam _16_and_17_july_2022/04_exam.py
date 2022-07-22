number_of_students = int(input())

students_between_2_and_3 = 0
students_between_3_and_4 = 0
students_between_4_and_5 = 0
students_between_5 = 0
total_grade = 0

for student in range(number_of_students):
    current_student_grade = float(input())

    if 2.00 <= current_student_grade <= 2.99:
        students_between_2_and_3 += 1
    elif 3.00 <= current_student_grade <= 3.99:
        students_between_3_and_4 += 1
    elif 4.00 <= current_student_grade <= 4.99:
        students_between_4_and_5 += 1
    elif current_student_grade >= 5.00:
        students_between_5 += 1
    total_grade += current_student_grade

top_students = (students_between_5 / number_of_students) * 100
good_students = (students_between_4_and_5 / number_of_students) * 100
average_students = (students_between_3_and_4 / number_of_students) * 100
failed_students = (students_between_2_and_3 / number_of_students) * 100

print(f'Top students: {top_students:.2f}%')
print(f'Between 4.00 and 4.99: {good_students:.2f}%')
print(f'Between 3.00 and 3.99: {average_students:.2f}%')
print(f'Fail: {failed_students:.2f}%')
average_grade = total_grade / number_of_students
print(f'Average: {average_grade:.2f}')


