film_name = input()
counter_total_tickets = 0
counter_kid = 0
counter_student = 0
counter_standard = 0
no_free_seats = False
while film_name != "Finish":
    available_seats = int(input())
    ticket_type = input()
    counter_current_tickets = 0
    occupied_percent = 0
    while ticket_type != "End":
        counter_total_tickets += 1
        counter_current_tickets += 1
        if ticket_type == "kid":
            counter_kid += 1
        elif ticket_type == "student":
            counter_student += 1
        elif ticket_type == "standard":
            counter_standard += 1
        if counter_current_tickets == available_seats:
            no_free_seats = True
            break
        ticket_type = input()
    occupied_percent = counter_current_tickets / available_seats * 100
    print(f"{film_name} - {occupied_percent:.2f}% full.")
    film_name = input()
kid_tickets_percent = counter_kid / counter_total_tickets * 100
student_tickets_percent = counter_student / counter_total_tickets * 100
standard_tickets_percent = counter_standard / counter_total_tickets * 100
print(f"Total tickets: {counter_total_tickets}")
print(f"{student_tickets_percent:.2f}% student tickets.")
print(f"{standard_tickets_percent:.2f}% standard tickets.")
print(f"{kid_tickets_percent:.2f}% kids tickets.")




