import re

text = input()
pattern = r"(@|#)([A-Za-z]{3,})\1\1([A-Za-z]{3,})\1"

valid_words = list(re.finditer(pattern, text))
mirror_words = []

if valid_words:
    for match in valid_words:
        word_one = match.group(2)
        word_two = match.group(3)
        if word_one == word_two[::-1]:
            mirror_words.append(word_one + " <=> " + word_two)
    print(f"{len(valid_words)} word pairs found!")

    if len(mirror_words) == 0:
        print("No mirror words!")
    else:
        print("The mirror words are:")
        print(", ".join(mirror_words))

else:
    print("No word pairs found!")
    print("No mirror words!")
