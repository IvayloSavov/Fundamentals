party_size = int(input())
days = int(input())

coins = 0
for day in range(1, days + 1):
    if day % 10 == 0:
        party_size -= 2

    if day % 15 == 0: # if day % 3 == 0 and if day % 5 == 0:
        party_size += 5
        coins -= 2 * party_size #вместо вложен if при петия ден, защото
        #това ще се изпълни когато на третия ден има парти. Което изнесено
        #означава че трябва да е и пети и трети ден едновременно, което от
        #своя страна означа, че на всеки 15 имаме такова парти, затова и го
        #сливаме при 15-ия ден

    coins += 50 - (2 * party_size)

    if day % 3 == 0:
        coins -= 3 * party_size

    if day % 5 == 0:
        coins += 20 * party_size

print(f"{party_size} companions received {coins // party_size} coins each.")