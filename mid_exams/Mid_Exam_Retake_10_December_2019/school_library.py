def is_book_on_shelf(book, shelf):
    return book in shelf


shelf_library = input().split("&")

command_input = input()

while command_input != "Done":
    command_input = command_input.split(" | ")
    command = command_input[0]

    if command == "Add Book":
        book_name = command_input[1]
        if not is_book_on_shelf(book_name, shelf_library):
            shelf_library.insert(0, book_name)

    elif command == "Take Book":
        book_name = command_input[1]
        if is_book_on_shelf(book_name, shelf_library):
            shelf_library.remove(book_name)

    elif command == "Swap Books":
        book_1 = command_input[1]
        book_2 = command_input[2]
        if is_book_on_shelf(book_1, shelf_library) and is_book_on_shelf(book_2, shelf_library):
            index_book_1 = shelf_library.index(book_1)
            index_book_2 = shelf_library.index(book_2)
            shelf_library[index_book_1] = book_2
            shelf_library[index_book_2] = book_1

    elif command == "Check Book":
        index = int(command_input[1])
        if 0 <= index < len(shelf_library):
            print(shelf_library[index])

    elif command == "Insert Book":
        book_name = command_input[1]
        shelf_library.append(book_name)

    command_input = input()

print(", ".join(shelf_library))
