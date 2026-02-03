def climbing_stairs(num_stairs: int)->int:
    """
    Find the number of ways to reach stairs num_stairs
    :param num_stairs:
    Total number of stairs
    :return:
    Number of ways to reach stairs
    """

    stair_one: int = 1
    stair_two: int = 2
    for stair in range(3, num_stairs + 1):

        stair_one,stair_two = stair_two, stair_one + stair_two
    return stair_two