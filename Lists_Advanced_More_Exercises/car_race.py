from math import floor


def time_racer(time_list):
    total_time = 0

    for t in time_list:
        if t == 0:
            total_time *= 80/100
            continue
        total_time += t

    return total_time


time = list(map(int, input().split()))
middle_index = floor(len(time) / 2)

first_racer = time[:middle_index]
second_racer = time[len(time):middle_index:-1]

# second_racer.reverse()
# second_racer = time[:middle_index:-1]
# second_racer = time[middle_index + 1:]
# second_racer.reverse()


time_first_racer = time_racer(first_racer)
time_second_racer = time_racer(second_racer)

if time_first_racer < time_second_racer:
    winner = time_first_racer
    left_right = "left"
    print(f"The winner is {left_right} with total time: {winner:.1f}")

elif time_second_racer < time_first_racer:
    winner = time_second_racer
    left_right = "right"
    print(f"The winner is {left_right} with total time: {winner:.1f}")

