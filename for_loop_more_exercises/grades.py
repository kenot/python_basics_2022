number_of_students = int(input())

grade_counter = 0
top_students_counter = 0
very_good_students_counter = 0
good_students_counter = 0
failed_students_counter = 0

for current_student in range(number_of_students):
    student_grade = float(input())
    grade_counter += student_grade
    if student_grade >= 5.00:
        top_students_counter += 1
    elif 4.00 <= student_grade <= 4.99:
        very_good_students_counter += 1
    elif 3.00 <= student_grade <= 3.99:
        good_students_counter += 1
    elif student_grade < 3:
        failed_students_counter += 1

percent_top_students = (top_students_counter / number_of_students) * 100
percent_very_good_students = (very_good_students_counter / number_of_students) * 100
percent_good_students = (good_students_counter / number_of_students) * 100
percent_failed_students = (failed_students_counter / number_of_students) * 100
average_grade = grade_counter / number_of_students

print(f'Top students: {percent_top_students:.2f}%')
print(f'Between 4.00 and 4.99: {percent_very_good_students:.2f}%')
print(f'Between 3.00 and 3.99: {percent_good_students:.2f}%')
print(f'Fail: {percent_failed_students:.2f}%')
print(f'Average: {average_grade:.2f}')