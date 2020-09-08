TIMES_TO_DOUBLE_CHAR = 2

text = input()
len_text = len(text)

for char in range(len_text):
    current_char = text[char]
    print(current_char * TIMES_TO_DOUBLE_CHAR, end="")