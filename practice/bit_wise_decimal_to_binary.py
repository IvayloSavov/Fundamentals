# from decimal to binary

n = int(input())
b = int(input())
remainders = []
# count = 0

while n != 0:
    remainder = n % 2
    # if remainder == b:
    #     count += 1
    remainders.append(remainder)
    n //= 2

remainders.reverse()
count_b = remainders.count(b)
print(count_b)