from typing import List


def min_cost_stairs(cost: List[int])->int:
    """
    Find the  minimum  cost to get  up a flight of stairs

    :param cost: A list of integers representing the flight costs
    :return: An integer representing the minimum  cost to get  up a flight of stairs
    """
    height: int = len(cost)
    left, right =  cost[0], cost[1]

    for stair in range(2, height):
        left, right =  right,  min(left ,right) + cost[stair]

    return min(left, right)