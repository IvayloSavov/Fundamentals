def bit_at_p_position(number, p):
    shifted_number = number >> p
    bit_to_print = shifted_number & 1

    return bit_to_print


n = int(input())
position = int(input())

print(bit_at_p_position(n, position))