n = int(input())
m = int(input())
magic_number = int(input())
combination_found = False
counter = 0
number_1 = 0
number_2 = 0
result = 0
for number_1 in range(n, m + 1):
    for number_2 in range(n, m + 1):
        result = number_1 + number_2
        counter += 1
        if result == magic_number:
            combination_found = True
            break
    if combination_found:
        break
if combination_found:
    print(f"Combination N:{counter} ({number_1} + {number_2} = {result})")
else:
    print(f"{counter} combinations - neither equals {magic_number}")
