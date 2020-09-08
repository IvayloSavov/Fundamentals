from math import floor
DAY_EARN = 50
DAY_SPEND_PER_COMPANION = 2
THIRD_DAY_SPEND_PER_COMPANION = 3
FIFTH_DAY_GAIN_PER_COMPANION = 20
TENTH_DAY_LEFT_COMPANION = 2
ADDITIONAL_PER_COMPANION_IF_IS_FIFTH_DAY_AND_WE_HAVE_MOTIVATIONAL_PARTY_FROM_THIRD_DAY = 2
FIFTEENTH_DAY_JOIN_COMPANION = 5

party_size = int(input())
days_adventure = int(input())
coins = 0


for day in range(1, days_adventure+1):
    motivational_party = False
    if day % 10 == 0:
        party_size -= TENTH_DAY_LEFT_COMPANION
    if day % 15 == 0:
        party_size += FIFTEENTH_DAY_JOIN_COMPANION
    coins += DAY_EARN
    coins -= (DAY_SPEND_PER_COMPANION * party_size)
    if day % 3 == 0:
        coins -= (THIRD_DAY_SPEND_PER_COMPANION * party_size)
        motivational_party = True
    if day % 5 == 0:
        coins += (FIFTH_DAY_GAIN_PER_COMPANION * party_size)
        if motivational_party:
            coins -= (ADDITIONAL_PER_COMPANION_IF_IS_FIFTH_DAY_AND_WE_HAVE_MOTIVATIONAL_PARTY_FROM_THIRD_DAY * party_size)


coins_for_every_companion = floor(coins / party_size)

print(f"{party_size} companions received {coins_for_every_companion} coins each.")