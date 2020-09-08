from math import ceil

days_of_trip = int(input())
budget = float(input())
group_of_people = int(input())
price_fuel_per_kilometer = float(input())
food_expenses_per_person_for_a_day = float(input())
price_room_for_one_night_per_person = float(input())
not_enough_money = False

food_expenses = food_expenses_per_person_for_a_day * group_of_people * days_of_trip
total_hotel_expenses = price_room_for_one_night_per_person * group_of_people * days_of_trip

if group_of_people > 10:
    total_hotel_expenses *= 75/100

expenses = total_hotel_expenses + food_expenses

for day in range(1, days_of_trip + 1):
    distance = float(input())
    travel_cost_current_day = distance * price_fuel_per_kilometer
    expenses += travel_cost_current_day

    if day % 3 == 0 or day % 5 == 0:
        additional_expenses = expenses * 40/100
        expenses += additional_expenses

    if budget < expenses:
        needed_money = (expenses - budget)
        print(f"Not enough money to continue the trip. You need {needed_money:.2f}$ more.")
        not_enough_money = True
        break

    if day % 7 == 0:
        receive_money = expenses / group_of_people
        expenses -= receive_money


if not not_enough_money:
    print(f"You have reached the destination. You have {(budget - expenses):.2f}$ budget left.")
