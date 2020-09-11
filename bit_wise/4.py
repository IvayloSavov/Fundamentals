def bit_destroyer(number, position):
    shifted_number = 1 << position
    mask = ~shifted_number

    result = number & mask
    return result


n = int(input())
p = int(input())

print(bit_destroyer(n, p))
