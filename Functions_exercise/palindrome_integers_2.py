def is_palindrome(text):
    range_1 = len(text)//2 # Делим на 2, защото ако имаме 1001, така ще проверим 10 с 01
    is_palindrome = True

    for i in range(range_1):
        index = len(text) - 1 - i # вадим 1 и i, защото така достъпваме отзад напред елементите
        if text[i] != text[index]:
            is_palindrome = False
            break

    return is_palindrome


def solve(items):
    for item in items:
        print(is_palindrome(item))


items = input().split(", ")

