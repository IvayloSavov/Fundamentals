def is_valid_length(word):
    return 3 <= len(word) <= 16


def is_valid_character(character):
    return character.isalpha() or character.isdigit() or character == "-" or character == "_"


def is_username_valid(user_names):
    valid_usernames = []

    for user_name in user_names:
        if is_valid_length(user_name):
            is_break = False
            for ch in user_name:
                if is_valid_character(ch):
                    pass
                else:
                    is_break = True
                    break
            if not is_break:
                valid_usernames.append(user_name)

    return valid_usernames


user_names = input().split(", ")
print(f"\n".join(is_username_valid(user_names)))