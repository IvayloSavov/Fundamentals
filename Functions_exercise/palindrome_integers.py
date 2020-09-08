def palindrome_integers(positive_integers):
    for integer in positive_integers:
        forward_integer = ""
        backward_integer = ""
        for digit_forward in integer:
            forward_integer += digit_forward
        for digit_backward in reversed(integer):
            backward_integer += digit_backward
        if forward_integer == backward_integer:
            print("True")
        else:
            print("False")


positive_integers = input().split(", ")

palindrome_integers(positive_integers)

