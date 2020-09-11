def print_the_bit_at_position_one(number):
    push_to_position_one = number >> 1
    number_at_position_one = push_to_position_one & 1
    return number_at_position_one

n = int(input())
print(print_the_bit_at_position_one(n))