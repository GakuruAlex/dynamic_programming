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
    ([2,4,6,2,5,8,3,7,9,4,1,6,8,2,5,9,3,7,4,6], 57),
    ([10,2,30,5,1,40,3,50,2,60,1,70,5,80,2,90,3,100,4,110], 640),
    ([100,200,300,400,500,600,700,800,900,1000], 3000)
])

def test_max_loot(houses: List[int], maximum_loot: int):
    assert max_loot(houses) == maximum_loot