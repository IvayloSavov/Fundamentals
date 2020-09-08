class Animal:
    def __init__(self, animal):
        self.name = animal

class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)
        Zoo.__animals += 1

    def get_info(self, species):
        global animals, name_species
        if species == "mammal":
            animals = self.mammals
            name_species = "Mammals"
        elif species == "fish":
            animals = self.fishes
            name_species = "Fishes"
        elif species == "bird":
            animals = self.birds
            name_species = "Birds"
        animals = ", ".join([animal.name for animal in animals])
        return f"{name_species} in {self.name}: {animals}\nTotal animals: {Zoo.__animals}"


name_of_zoo = input()
n = int(input())

zoo = Zoo(name_of_zoo)

for _ in range(n):
    species, name = input().split()
    animal = Animal(name)
    zoo.add_animal(species, animal)

species_input = input()

print(zoo.get_info(species_input))