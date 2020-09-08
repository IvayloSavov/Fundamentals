n = int(input())

for num in range(1, n+1):
    num = str(num)
    sum_of_digits = 0
    length_num = len(str(num))
    for digit in range(length_num):
        current_digit = num[digit]
        sum_of_digits += int(current_digit)
    if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
        # is_special = True
        print(f"{num} -> True")
    else:
        # is_special = False
        print(f"{num} -> False")

    # print(f"{num} -> {is_special}")