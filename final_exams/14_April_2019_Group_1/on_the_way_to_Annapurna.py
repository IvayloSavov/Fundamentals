from _collections import defaultdict

stores = defaultdict(list)

while True:
    tokens = input()
    if tokens == "END":
        break
    tokens = tokens.split("->")
    command = tokens[0]
    store = tokens[1]

    if command == "Add":
        items = tokens[2]
        if "," in items:
            items = items.split(",")
            stores[store].extend(items)
        else:
            stores[store].append(items)

    elif command == "Remove":
        if store in stores.keys():
            stores.pop(store)


stores = dict(sorted(stores.items(), key=lambda s: (len(s[1]), s[0]), reverse=True))
print("Stores list:")

for store, items in stores.items():
    print(store)
    while len(items) > 0:
        item = items.pop(0)
        print(f"<<{item}>>")
