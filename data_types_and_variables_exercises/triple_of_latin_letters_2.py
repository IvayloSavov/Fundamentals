n = int(input())

for fr in range(0, n):
    for scnd in range(0, n):
        for third in range(0, n):
            print(chr(97 + fr) + chr(97+scnd) + chr(97+third))