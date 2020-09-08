str_1 = input() #toby
str_2 = input() #ivon
length_str = len(str_1)

for i in range(length_str):
    if str_1[i] != str_2[i]:
        for chr_2 in range(0, i+1):
            print(str_2[chr_2], end="")

        for chr_1 in range(i+1, length_str):
            print(str_1[chr_1], end="")

        print()


# text_1 = input()
# text_2 = input()
# len_texts = len(text_1)
#
# for i in range(len_texts):
#     old_character = str(text_1[i])
#     replace_character = str(text_2[i])
#     if old_character != replace_character:
#         text_1 = text_1.replace(old_character, replace_character, 1)
#         print(text_1)
#     else:
#         continue
