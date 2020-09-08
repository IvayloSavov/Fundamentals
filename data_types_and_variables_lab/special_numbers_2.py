n = int(input())

for number in range(1,n+1):
    sum_of_digits = 0

    number_copy = number
    while number_copy > 0:
        digit = number_copy % 10
        sum_of_digits += digit
        number_copy = number_copy//10 #ако напишем без cast към инт ще влезе ако е 0.9 или 0.8 и т.н. или с //

    is_special = sum_of_digits in (5, 7, 11)
    # is_special = sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11
    print(f"{number} -> {is_special}")