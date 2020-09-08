data = input()

longest_palindrome = ""

for index, ch in enumerate(data):
    current_string = ""
    for i in range(index, len(data)):
        current_character = data[i]
        current_string += current_character
        if ch == current_character:
            if len(current_string) > len(longest_palindrome):
                longest_palindrome = current_string

print(len(longest_palindrome))