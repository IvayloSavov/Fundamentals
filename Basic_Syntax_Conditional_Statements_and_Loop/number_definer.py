n = float(input())

if n == 0:
    print("zero")
else:
    if n > 0:
        if abs(n) < 1:
            print("small", end=" ")
        elif abs(n) > 1_000_000:
            print("large", end=" ")
        print("positive")
    elif n < 0:
        if abs(n) < 1:
            print("small", end=" ")
        elif abs(n) > 1000000:
            print("large", end=" ")
        print("negative")

