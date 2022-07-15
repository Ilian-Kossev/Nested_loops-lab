destination = input()
while destination != "End":
    necessary_budget = float(input())
    saved_money = 0
    while saved_money < necessary_budget:
        input_sum = float(input())
        saved_money += input_sum
    print(f"Going to {destination}!")
    destination = input()
