from typing import List

import pytest
from house_robber import max_loot

@pytest.mark.parametrize("houses, maximum_loot",[
    ([1, 2, 3, 1], 4),
    ([2, 7, 9, 3, 1], 12),
    ([2, 1, 1, 2], 4),
    ([5, 3, 4, 11, 2], 16),
    ([10, 1, 2, 10, 5, 1], 21),
    ([1, 20, 3], 20),
    ([], 0),
    ([100], 100),

])

def test_max_loot(houses: List[int], maximum_loot: int):
    assert max_loot(houses) == maximum_loot