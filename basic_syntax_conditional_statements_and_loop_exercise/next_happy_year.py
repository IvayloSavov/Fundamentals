from sys import maxsize
year = input()
is_found = False

for current_year in range(int(year) + 1, maxsize):
    all_symbols = len(str(current_year))
    unique_symbols = len(set(str(current_year)))
    if all_symbols == unique_symbols:
        print(current_year)
        break
