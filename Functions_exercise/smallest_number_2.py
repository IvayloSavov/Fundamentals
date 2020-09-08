def smallest_number(a, b, c):
    smallest = c # ако тук напишем, че е равно на 0, тогава имаме нужда от
    # else, а ако е така нямаме нужда от него

    if a < b and a < c:
        smallest = a
    elif b < a and b < c:
        smallest = b
    # else:
    #     smallest = c
    return smallest


num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

print(smallest_number(num_1, num_2, num_3))

