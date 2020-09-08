population = input().split(", ")
population = list(map(int, population))
minimum_wealth = int(input())
no_equal = False

for index, person in enumerate(population):
    wealthiest_person = max(population)
    if person < minimum_wealth:
        money_to_give = minimum_wealth - person
        if wealthiest_person - money_to_give < minimum_wealth:
            print("No equal distribution possible")
            no_equal = True
            break
        wealthiest_person_index = population.index(wealthiest_person)
        population[index] += money_to_give
        population[wealthiest_person_index] -= money_to_give

if not no_equal:
    print(population)
