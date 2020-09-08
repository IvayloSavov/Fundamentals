treasure_chest = input().split("|")
count = int(input())
if count > len(treasure_chest):
    del treasure_chest[::]
    print(" ".join(treasure_chest[:]))
else:
    print(" ".join(treasure_chest[-count:]))