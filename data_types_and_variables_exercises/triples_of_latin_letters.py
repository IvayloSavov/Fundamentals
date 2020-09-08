n = int(input())

for first_letter in range(97, 97+n):
    for second_letter in range(97, 97+n):
        for third_letter in range(97, 97+n):
            print(chr(first_letter) + chr(second_letter) + chr(third_letter))

