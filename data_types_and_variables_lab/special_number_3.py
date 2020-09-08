n = int(input())

for num in range(1, n+1):
    sum_of_digits = 0
    for c in str(num):
        sum_of_digits += int(c)
    is_special = sum_of_digits in (5, 7, 11)
    print(f"{num} -> {is_special}")
