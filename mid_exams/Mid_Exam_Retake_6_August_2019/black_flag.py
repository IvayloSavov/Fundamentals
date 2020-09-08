days = int(input())
daily_plunder = int(input())
expected_plunder = int(input())

gained_plunder = 0

for day in range(1, days + 1):
    gained_plunder += daily_plunder
    if day % 3 == 0:
        additional_plunder = daily_plunder * 50/100
        gained_plunder += additional_plunder
    if day % 5 == 0:
        loosed_plunder = gained_plunder * 30/100
        gained_plunder -= loosed_plunder


if gained_plunder >= expected_plunder:
    print(f"Ahoy! {gained_plunder:.2f} plunder gained.")
else:
    percentage = gained_plunder / expected_plunder * 100
    print(f"Collected only {percentage:.2f}% of the plunder.")
