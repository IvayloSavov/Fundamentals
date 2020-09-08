n = int(input())

string = []
is_unbalanced = False

for _ in range(n):
    tokens = input()
    string.append(tokens)

matches = list(filter((lambda ch: ch == "(" or ch == ")"), string))

if len(matches) % 2 != 0:
    is_unbalanced = True
    print("UNBALANCED")
else:
    for index, element in enumerate(matches):

        if index + 1 == len(matches):
            break

        if element == "(":
            if matches[index + 1] == "(":
                print("UNBALANCED")
                is_unbalanced = True
                break

        elif element == ")":
            if matches[index + 1] == ")":
                print("UNBALANCED")
                is_unbalanced = True
                break

if not is_unbalanced:
    print("BALANCED")