pair_of_words_and_descriptions = input().split(" | ")
words_to_print = input().split(" | ")
command = input()

dictionary = {}

for pair_word_description in pair_of_words_and_descriptions:
    pair_word_description = pair_word_description.split(": ")
    word = pair_word_description[0]
    description = pair_word_description[1]

    if word not in dictionary:
        dictionary[word] = []

    if description not in dictionary[word]:
        dictionary[word].append(description)

for word in words_to_print:
    if word in dictionary.keys():
        print(f"{word}")
        description_to_print = sorted(dictionary[word], key=lambda element: -len(element))
        while len(description_to_print) > 0:
            print(f" -{description_to_print.pop(0)}")

if command == "End":
    pass
elif command == "List":
    words_to_print = sorted(dictionary.keys(), key=lambda word_: word_)
    print(" ".join(words_to_print))
