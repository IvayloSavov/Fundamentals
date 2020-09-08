people = int(input())
capacity = int(input())
people_elevated = 0
courses = 0

while people_elevated < people:
    courses += 1
    people_elevated += capacity

print(courses)