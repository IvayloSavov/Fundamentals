def index_is_valid(index, message):
    return 0 <= index < len(message)


def word_is_valid(word, message):
    return word in message


disordered_message = input().split()

command_input = input()

while command_input != "Stop":
    instruction = command_input.split()
    command = instruction[0]

    if command == "Delete":
        index = int(instruction[1])
        if index_is_valid(index + 1, disordered_message):
            disordered_message.pop(index + 1)

    elif command == "Swap":
        word_1 = instruction[1]
        word_2 = instruction[2]
        if word_is_valid(word_1, disordered_message) and word_is_valid(word_2, disordered_message):
            word_1_index = disordered_message.index(word_1)
            word_2_index = disordered_message.index(word_2)

            disordered_message[word_1_index], disordered_message[word_2_index] = disordered_message[word_2_index], \
                disordered_message[word_1_index]

    elif command == "Put":
        # index, word = int(instruction[2]) - 1, instruction[1]
        # if index - 1 in range(len(disordered_message)):
        #     disordered_message.insert(index, word)
        word = instruction[1]
        index = int(instruction[2]) - 1

        # if 0 <= index <= len(disordered_message):
        #     disordered_message.insert(index, word)

        if index == len(disordered_message):
            disordered_message.append(word)
        elif index_is_valid(index, disordered_message):
            disordered_message.insert(index, word)
    elif command == "Sort":
        disordered_message.sort(reverse=True)

    elif command == "Replace":
        word_1 = instruction[1]
        word_2 = instruction[2]
        if word_is_valid(word_2, disordered_message):
            word_2_index = disordered_message.index(word_2)
            disordered_message[word_2_index] = word_1

    command_input = input()

print(" ".join(disordered_message))