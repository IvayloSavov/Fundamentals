def is_palindrome(element):
    if element == element[::-1]:
        return True

# def is_palindrome(word):
#   return word == ''.join(reversed(word))

string = input().split(" ")
searched_palindrome = input()
palindromes = []

count_searched_palindrome = 0

for element in string:
    if element == searched_palindrome:
        count_searched_palindrome += 1
        palindromes.append(element)
    else:
        if is_palindrome(element):
            palindromes.append(element)

print(palindromes)
print(f"Found palindrome {count_searched_palindrome} times")



