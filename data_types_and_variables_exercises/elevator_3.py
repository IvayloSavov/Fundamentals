people_count = int(input())
capacity = int(input())

if people_count % capacity == 0:
    result = people_count // capacity
else:
    result = people_count // capacity + 1

print(result)