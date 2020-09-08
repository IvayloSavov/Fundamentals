MIN_NUMBER = 1
MAX_NUMBER = 100
number = float(input())
while number < 1 or number > 100:
    number = float(input())
print(f"The number {number} is between {MIN_NUMBER} and {MAX_NUMBER}")
