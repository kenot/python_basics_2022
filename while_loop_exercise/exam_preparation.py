maximum_bad_grades = int(input())
average_grade = 0
total_problems_solved = 0
last_problem = ''
bad_grades_counter = 0
is_expelled = False

current_problem = input()
while current_problem != "Enough":
    current_grade = int(input())
    if current_grade <= 4:
        bad_grades_counter += 1
        if bad_grades_counter == maximum_bad_grades:
            is_expelled = True
            break
    average_grade += current_grade
    total_problems_solved += 1
    last_problem = current_problem

    current_problem = input()
if is_expelled:
    print(f'You need a break, {bad_grades_counter} poor grades.')
else:
    average_grade /= total_problems_solved
    print(f'Average score: {average_grade:.2f}')
    print(f'Number of problems: {total_problems_solved}')
    print(f'Last problem: {last_problem}')