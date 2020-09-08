from math import floor
DAYS = 30

biscuits_per_day_per_worker = int(input())
workers_in_factory = int(input())
biscuits_per_day_all_workers = biscuits_per_day_per_worker * workers_in_factory
competing_factory = int(input())

production = 0


for day in range(1, DAYS + 1):
    if day % 3 == 0:
        production += floor(biscuits_per_day_all_workers * 75/100)
    else:
        production += biscuits_per_day_all_workers

print(f"You have produced {production} biscuits for the past month.")

difference = abs(production - competing_factory)
percentage = difference/competing_factory * 100
if production > competing_factory:
    print(f"You produce {percentage:.2f} percent more biscuits.")
else:
    print(f"You produce {percentage:.2f} percent less biscuits.")