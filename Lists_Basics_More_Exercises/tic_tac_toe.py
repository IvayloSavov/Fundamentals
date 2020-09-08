first_row = input().split(' ')
second_row = input().split(' ')
third_row = input().split(' ')

if first_row[0] == second_row[0] and second_row[0] == third_row[0]:
    if first_row[0] == '1':
        print("First player won")
    elif first_row[0] == '2':
        print("Second player won")
    else:
        print('Draw!')
elif first_row[0] == second_row[1] and second_row[1] == third_row[2]:
    if first_row[0] == '1':
        print("First player won")
    elif first_row[0] == '2':
        print("Second player won")
    else:
        print('Draw!')
elif first_row[1] == second_row[1] and second_row[1] == third_row[1]:
    if first_row[1] == '1':
        print("First player won")
    elif first_row[1] == '2':
        print("Second player won")
    else:
        print('Draw!')
elif first_row[2] == second_row[2] and second_row[2] == third_row[2]:
    if first_row[2] == '1':
        print("First player won")
    elif first_row[2] == '2':
        print("Second player won")
    else:
        print('Draw!')
elif first_row[2] == second_row[1] and second_row[1] == third_row[0]:
    if first_row[2] == '1':
        print("First player won")
    elif first_row[2] == '2':
        print("Second player won")
    else:
        print('Draw!')
elif first_row[0] == first_row[1] == first_row[2]:
    if first_row[0] == '1':
        print("First player won")
    elif first_row[0] == '2':
        print("Second player won")
    else:
        print('Draw!')
elif second_row[0] == second_row[1] == second_row[2]:
    if second_row[0] == '1':
        print("First player won")
    elif second_row[0] == '2':
        print("Second player won")
    else:
        print('Draw!')
elif third_row[0] == third_row[1] == third_row[2]:
    if third_row[0] == '1':
        print("First player won")
    elif third_row[0] == '2':
        print("Second player won")
    else:
        print('Draw!')
else:
    print('Draw!')