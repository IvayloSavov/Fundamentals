numbers = str(input()).split(", ")

numbers_integers = [int(number) for number in numbers]
# numbers_integers = list(map(int, numbers))
# numbers_integers = list(map(lambda n: int(n), numbers))
indices_even_number = [index for index, num in enumerate(numbers_integers) if num % 2 == 0]
print(indices_even_number)



# numbers = str(input()).split(", ")
#
# indices_even_number = [index for index, num in enumerate(numbers) if int(num) % 2 == 0]
#
# print(indices_even_number)
