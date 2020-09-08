from sys import maxsize


def kangaroo(arr):
    tries = 0
    is_yes = False
    k1_start, k_1_jump, k2_start, k_2_jump = int(arr[0]), int(arr[1]), int(arr[2]), int(arr[3])
    position_first_kangaroo = k1_start
    position_second_kangaroo = k2_start

    if (k1_start < k2_start and k_1_jump < k_2_jump) or (k2_start < k1_start and k_2_jump < k_1_jump):
        is_yes = False
    else:
        for _ in range(2500):
            if position_first_kangaroo == position_second_kangaroo:
                is_yes = True
                break
            else:
                position_first_kangaroo += k_1_jump
                position_second_kangaroo += k_2_jump

    if is_yes:
        return "YES"
    else:
        return "NO"


data = input().split()
print(kangaroo(data))