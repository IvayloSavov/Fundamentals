n = int(input())
positive_int = []
negative_int = []

for _ in range(n):
    integer = int(input())
    positive_int.append(integer) if integer >= 0 else negative_int.append(integer)

print(positive_int)
print(negative_int)
print(f"Count of positives: {len(positive_int)}. Sum of negatives: {sum(negative_int)}")