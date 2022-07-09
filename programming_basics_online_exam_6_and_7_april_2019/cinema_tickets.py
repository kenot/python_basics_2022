name_of_movie = input()

student_ticket_count = 0
standard_ticket_count = 0
kid_ticket_count = 0
total_tickets = 0

while name_of_movie != "Finish":
    free_seats = int(input())
    busy_seats = 0

    for i in range(free_seats):
        current_ticket_type = input()
        if current_ticket_type == "student":
            student_ticket_count += 1
        elif current_ticket_type == "standard":
            standard_ticket_count += 1
        elif current_ticket_type == "kid":
            kid_ticket_count += 1
        elif current_ticket_type == "End":
            break
        total_tickets += 1
        busy_seats += 1

    percent_room = (busy_seats / free_seats) * 100
    total_tickets = standard_ticket_count + student_ticket_count + kid_ticket_count
    print(f'{name_of_movie} - {percent_room:.2f}% full.')

    name_of_movie = input()

print(f'Total tickets: {total_tickets}')
print(f'{(student_ticket_count / total_tickets) * 100:.2f}% student tickets.')
print(f'{(standard_ticket_count / total_tickets) * 100:.2f}% standard tickets.')
print(f'{(kid_ticket_count / total_tickets) * 100:.2f}% kids tickets.')


