
number_of_people_in_jury = int(input())
number_of_presentations = 0
students_final_assessment = 0

command = input()
while command != "Finish":
    current_presentation_name = command
    number_of_presentations += 1
    current_presentation_grade = 0
    for grade in range(number_of_people_in_jury):
        current_grade = float(input())
        current_presentation_grade += current_grade
    current_presentation_grade /= number_of_people_in_jury
    print(f'{current_presentation_name} - {current_presentation_grade:.2f}.')
    students_final_assessment += current_presentation_grade

    command = input()
students_final_assessment /= number_of_presentations
print(f"Student's final assessment is {students_final_assessment:.2f}.")

