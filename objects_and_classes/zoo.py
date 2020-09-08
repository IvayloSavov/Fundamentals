class Animal:
    def __init__(self, name):
        self.name = name


class Species:
    MAMMALS = "mammal"
    FISHES = "fish"
    BIRDS = 'bird'


class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == Species.MAMMALS: # = "mammals"
            self.mammals.append(name)
        elif species == Species.FISHES:
            self.fishes.append(name)
        elif species == Species.BIRDS:
            self.birds.append(name)
        self.__animals += 1

    def get_info(self, species):
        zoo_name = self.name
        animals = ""
        species_name_plural = ""
        if species == Species.MAMMALS:
            animals = self.mammals
            species_name_plural = "Mammals"

        elif species == Species.FISHES:
            animals = self.fishes
            species_name_plural = "Fishes"

        elif species == Species.BIRDS:
            animals = self.birds
            species_name_plural = "Birds"
        return f'{species_name_plural} in {zoo_name}: {", ".join([animal.name for animal in animals])}'

    def get_total(self):
        return f"Total animals: {self.__animals}"

zoo_name = input()
zoo = Zoo(zoo_name)

animals_count = int(input())

for _ in range(animals_count):
    species, animal_name = input().split(" ", maxsplit=1)
    animal = Animal(animal_name)
    zoo.add_animal(species, animal)

species = input()

print(zoo.get_info(species))
print(zoo.get_total())