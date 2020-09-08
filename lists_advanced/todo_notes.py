tasks = []

while True:
    command = input()
    if command == "End":
        break
    tokens = command.split("-", maxsplit=1)
    priority = int(tokens[0])
    task = tokens[1]
    tasks.append((priority, task))


def sort_fn(item):  # тази задача може и без key, защото така или иначе е по-първа първата буква
    return item[0]


tasks_in_priority = [task_name for priority, task_name in sorted(tasks, key=sort_fn)]

print(tasks_in_priority)
