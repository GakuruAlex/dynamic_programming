from typing import List

def max_loot(houses: List[int])-> int:
    houses_len = len(houses)
    if houses_len <1:
        return 0
    if houses_len <= 2:
        return max(houses)
    prev_2 = houses[0]
    prev_1 = max(houses[0], houses[1])

    for i in range(2, houses_len):
        current = max(prev_1, prev_2 + houses[i])
        prev_2 , prev_1= prev_1, current
    return prev_1