cost_journey = float(input())
number_months = int(input())

collected_money = 0

for month in range(1, number_months + 1):
    if month % 4 == 0:
        collected_money *= 125/100
    if month % 2 != 0 and month > 1:
        collected_money *= 84/100

    collected_money += (cost_journey * 25/100)

needed_left_money = abs(collected_money - cost_journey)
if collected_money >= cost_journey:
    print(f"Bravo! You can go to Disneyland and you will have {needed_left_money:.2f}lv. for souvenirs.")
else:
    print(f"Sorry. You need {needed_left_money:.2f}lv. more.")
