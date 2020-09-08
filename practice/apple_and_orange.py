def fallen_fruits_near_the_house(house: list, position_tree: int, distance_fruits: list):
    fruits_count = 0
    for fruit in distance_fruits:
        if house[0] <= (position_tree + fruit) <= house[1]:
            fruits_count += 1

    return fruits_count


def count_apple_and_oranges(house, position_trees, distance_apples, distance_oranges):
    count_apples = fallen_fruits_near_the_house(house, position_trees[0], distance_apples)
    count_oranges = fallen_fruits_near_the_house(house, position_trees[1], distance_oranges)

    return [count_apples, count_oranges]


sam_house = list(map(int, input().split()))
position_apple_and_orange_trees = list(map(int, input().split()))
count_apples_and_oranges = list(map(int, input().split()))
distance_fallen_apples = list(map(int, input().split()))
distance_fallen_oranges = list(map(int, input().split()))

res = list(map(str, count_apple_and_oranges(sam_house, position_apple_and_orange_trees, distance_fallen_apples, distance_fallen_oranges)))

print("\n".join(res))

# print(sum([1 for x in apple if (x + a) >= s and (x + a) <= t]))
# print(sum([1 for x in orange if (x + b) >= s and (x + b) <= t]))