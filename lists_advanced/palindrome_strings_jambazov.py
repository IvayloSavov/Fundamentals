def is_palindrome(word):
    return word == word[::-1]

# is_palindrome = lambda word: word == word[::-1]


words = input().split(' ')
searched_palindrome = input()
palindromes = [word for word in words if is_palindrome(word)]

print(palindromes)
print(f"Found palindrome {palindromes.count(searched_palindrome)} times")
