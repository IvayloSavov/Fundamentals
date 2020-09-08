n = int(input())
train = [0] * n


def add_to_train(train, number):
    train[-1] += number


def insert_in_train(train, index, number):
    train[index] += number


def leave_in_train(train, index, num):
    train[index] -= num


while True:
    command = input()
    if command == "End":
        break
    tokens = command.split(" ")
    command = tokens[0]

    if command == "add":
        add_to_train(train, int(tokens[1]))

    elif command == "insert":
        index = int(tokens[1])
        people_to_insert = int(tokens[2])
        insert_in_train(train, index, people_to_insert)

    elif command == "leave":
        index = int(tokens[1])
        people_to_leave = int(tokens[2])
        leave_in_train(train, index, people_to_leave)

print(train)