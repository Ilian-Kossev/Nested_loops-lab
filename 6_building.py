floor_number = int(input())
room_number = int(input())


for floors in range(floor_number, 0, -1):
    for rooms in range(0, room_number):
        if floors == floor_number:
            room_type = "L"
        elif floors % 2 == 0:
            room_type = "O"
        else:
            room_type = "A"
        print(f"{room_type}{floors}{rooms}", end=" ")
    print()