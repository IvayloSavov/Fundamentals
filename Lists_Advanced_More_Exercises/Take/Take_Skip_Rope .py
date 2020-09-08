import math
string = input()
index = 0

digits = [int(ch) for ch in string if ch.isdigit()]
string_list = [ch for ch in string if not ch.isdigit()]

take_list = [int(ch) for index, ch in enumerate(digits) if index % 2 == 0]
skip_list = [int(ch) for index, ch in enumerate(digits) if index % 2 != 0]

decrypted_msg = []

while index < len(skip_list):
    taker = take_list[index]
    skipper = skip_list[index]
    take_ch = string_list[0:taker]
    decrypted_msg.extend(string_list[0:taker]) # със сласинг от лист ти го връща като лист, а със слайсинг от текст ще го върне като текст
    del string_list[0:taker]
    del string_list[0:skipper]
    index += 1

print("".join(decrypted_msg))