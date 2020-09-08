text = input()
data = input()
while data != "Done":
    tokens = data.split(' ')
    command = tokens[0]
    if command == "TakeOdd":
        new_str = ''
        for ch in range(len(text)):
            if ch % 2 != 0:
                new_str += text[ch]
        text = new_str
        print(text)
    elif command == "Cut":
        index = int(tokens[1])
        length = int(tokens[2])
        substring = text[index:index+length]
        text = text.replace(substring, '', 1)
        print(text)
    elif command == "Substitute":
        substring = tokens[1]
        substitute = tokens[2]
        if substring in text:
            text = text.replace(substring, substitute)
            print(text)
        else:
            print("Nothing to replace!")
    data = input()
print(f"Your password is: {text}")