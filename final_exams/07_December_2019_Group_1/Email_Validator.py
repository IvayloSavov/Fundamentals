email = input()

while True:
    tokens = input()
    if tokens == "Complete":
        break
    tokens = tokens.split()
    command = tokens[0]

    if command == "Make":
        upper_lower = tokens[1]
        if upper_lower == "Upper":
            email = email.upper()
        else:
            email = email.lower()
        print(email)

    elif command == "GetDomain":
        count = int(tokens[1])
        print(email[-count:])

    elif command == "GetUsername":
        if "@" not in email:
            print(f"The email {email} doesn't contain the @ symbol.")
        else:
            ch_to_print = ""
            for ch in email:
                if ch == "@":
                    break
                else:
                    ch_to_print += ch
            print(ch_to_print)

    elif command == "Replace":
        char = tokens[1]
        while char in email:
            email = email.replace(char, "-")
        print(email)

    elif command == "Encrypt":
        values_of_characters = [str(ord(ch)) for ch in email]
        print(" ".join(values_of_characters))
