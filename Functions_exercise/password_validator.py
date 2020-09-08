def length_is_6_to_10(number):
    is_length_is_6_to_10 = False
    if 6 <= number <= 10:
        is_length_is_6_to_10 = True
    return is_length_is_6_to_10


def letters_digit(text):
    only_letters_digit = True
    for character in text:
        if not character.isdigit() and not character.isalpha():
            only_letters_digit = False
            break
    return only_letters_digit


def at_least_2_digits(text):
    is_at_least_2_digits = False
    count_digits = 0
    for character in text:
        if character.isdigit():
            count_digits += 1
    if count_digits >= 2:
        is_at_least_2_digits = True
    return is_at_least_2_digits


def password_validator(password):
    first_validation = at_least_2_digits(password)
    second_validation = length_is_6_to_10(len(password))
    third_validation = letters_digit(password)
    if first_validation and second_validation and third_validation:
        print("Password is valid")
    else:
        if not second_validation:
            print("Password must be between 6 and 10 characters")
        if not third_validation:
            print("Password must consist only of letters and digits")
        if not first_validation:
            print("Password must have at least 2 digits")


password = input()
password_validator(password)

