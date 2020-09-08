def all_digits(text):
    return get_all_characters_matching_condition(text, lambda char: char.isdigit())


def all_letters(text):
    return get_all_characters_matching_condition(text, lambda char: char.isalpha())


def all_other_characters(text):
    return get_all_characters_matching_condition(text, lambda char: not char.isdigit() and not char.isalpha())


def get_all_characters_matching_condition(text, condition_fn):
    result = ''
    for char in text:
        if condition_fn(char):
            result += char
    return result


text = input()

print(all_digits(text))
print(all_letters(text))
print(all_other_characters(text))