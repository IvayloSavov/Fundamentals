lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

sword_broken_times = 0
helmet_broken_times = 0
shield_broken_times = 0
armour_broken_times = 0
expenses_new_equipment = 0

for lost_fight in range(1, lost_fights_count + 1):
    is_helmet_broken = False
    is_sword_broken = False
    if lost_fight % 2 == 0:
        expenses_new_equipment += helmet_price
        is_helmet_broken = True
        helmet_broken_times += 1
    if lost_fight % 3 == 0:
        expenses_new_equipment += sword_price
        is_sword_broken = True
        sword_broken_times += 1
    if is_sword_broken and is_helmet_broken:
        expenses_new_equipment += shield_price
        shield_broken_times += 1
    if shield_broken_times % 2 == 0 and shield_broken_times > 0:
        expenses_new_equipment += armor_price
        armour_broken_times += 1
        shield_broken_times = 0 #зануляваме, защото това не е вързано към цикъл и да расте след всеки оборот на цикъла, а
        #си остава една и съща стойност. Ако не го занолим това означава, че на то и на следващия оборот ще си е 2, а няма
        #да е 3. И тогава пак ще добави стойността, а не трябва. За това зануляваме, тъй като то не расте автоматично. Също
        #така зануляването не трябва да е автоматично на всяка загубена битка, защото така пък ще загубим правилната бройка
        #на счупванията.

print(f"Gladiator expenses: {expenses_new_equipment:.2f} aureus")