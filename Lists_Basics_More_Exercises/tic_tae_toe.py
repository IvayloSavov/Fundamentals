line_1 = input().split()
line_2 = input().split()
line_3 = input().split()


def if_won(n):
    if line_1[1] == line_1[2] == line_1[0] == n or \
            line_2[1] == line_2[2] == line_2[0] == n or \
            line_3[1] == line_3[2] == line_3[0] == n or \
 \
            line_1[1] == line_2[1] == line_3[1] == n or \
            line_1[2] == line_2[2] == line_3[2] == n or \
            line_1[0] == line_2[0] == line_3[0] == n or \
 \
            line_1[0] == line_2[1] == line_3[2] == n or \
            line_1[2] == line_2[1] == line_3[0] == n:
        return True


if if_won("1"):
    print("First player won")
elif if_won("2"):
    print("Second player won")
else:
    print("Draw!")