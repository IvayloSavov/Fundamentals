divisor = int(input())
bound = int(input())
greatest_number = 0
for n in range(1, bound+1):
    if n % divisor == 0 and bound >= n > 0:
        greatest_number = n

print(greatest_number)

