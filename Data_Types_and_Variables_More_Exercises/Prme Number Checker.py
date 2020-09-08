number = int(input())

is_prime = True

for n in range(2, number):
    if number % n == 0:
        is_prime = False
        break

print(is_prime)