def save_the_prisoner(prisoner_data):

    number_prisoners = prisoner_data[0]
    number_of_sweets = prisoner_data[1]
    start_chair = prisoner_data[2]

    busted_chair = start_chair

    while True:
        number_of_sweets -= 1

        if number_of_sweets == 0:
            break

        if busted_chair == number_prisoners:
            busted_chair = 1
        else:
            busted_chair += 1

    return busted_chair


number_of_test_cases = int(input())
busted_chairs = []

for _ in range(number_of_test_cases):
    prisoners_data = list(map(int, input().split()))
    busted_chairs.append(save_the_prisoner(prisoners_data))

print("\n".join(list(map(str, busted_chairs))))
