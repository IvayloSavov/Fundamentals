first_n = int(input())
second_n = int(input())
third_n = int(input())

if first_n > second_n and first_n > third_n:
    print(first_n)
elif second_n > first_n and second_n > third_n:
    print(second_n)
elif third_n > first_n and third_n > second_n:
    print(third_n)
