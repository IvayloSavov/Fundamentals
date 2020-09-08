def repeat_string(string_to_repeat: str, number_of_repetitions: int):
    return string_to_repeat * number_of_repetitions


string_to_repeat: str = input()
number_of_repetitions: int = int(input())

print(repeat_string(string_to_repeat, number_of_repetitions))

