class Person:
    def __init__(self, name):
        self.name = name


class Party:
    def __init__(self):
        self.people = []

    def add_person(self, person):
        self.people.append(person)

    def __repr__(self):
        result = f"Going: {', '.join([person.name for person in self.people])}\n" f"Total: {len(self.people)}"
        return result


party = Party()

while True:
    command = input()
    if command == "End":
        break
    name = command
    person = Person(name)
    party.add_person(person)

print(party)