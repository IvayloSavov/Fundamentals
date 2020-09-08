age = int(input())

print("drink", end=" ")
if age <= 14:
    print("toddy")
elif age <= 18:
    print("coke")
elif age <= 21:
    print("beer")
else:
    print("whisky")