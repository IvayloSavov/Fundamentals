dwarfDict = {}

while True:
    command = input()
    if command == 'Once upon a time':
        break
    else:
        command_split = command.split(' <:> ')
        name, hat, physics = command_split[0], command_split[1], int(command_split[2])
        if hat not in dwarfDict:
            dwarfDict[hat] = {name: physics}
        else:
            if name not in dwarfDict[hat]:
                dwarfDict[hat][name] = physics
            else:
                if dwarfDict[hat][name] < physics:
                    dwarfDict[hat][name] = physics

orderedList = []
for k, v in dwarfDict.items():
    for b, c in v.items():
        orderedList.append([b, c, len(v), k])
orderedList = sorted(orderedList, key=lambda x: (-x[1], -x[2]))
for i in orderedList:
    print(f"({i[3]}) {i[0]} <-> {i[1]}")