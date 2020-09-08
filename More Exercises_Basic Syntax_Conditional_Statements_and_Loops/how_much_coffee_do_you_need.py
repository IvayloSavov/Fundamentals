command = input()
needed_coffee = 0
is_break = False

while command != "END":
    event = command
    is_upper = False
    if event.isupper():
        is_upper = True
        event = event.lower()

    events = (
        (event == "coding") or
        (event == 'dog' or event == 'cat') or
        (event == "movie")
    )

    if events:
        needed_coffee += 1
        if is_upper:
            needed_coffee += 1

    if needed_coffee > 5:
        print('You need extra sleep')
        is_break = True
        break
    command = input()

if not is_break:
    print(needed_coffee)