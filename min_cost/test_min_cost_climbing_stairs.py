from typing import List
from min_cost_climbing_stairs import min_cost_stairs
import pytest

@pytest.mark.parametrize('cost, min_cost',[
    ([10, 15, 28], 15),
    ([1, 100, 1, 1, 1, 100, 1, 1, 100, 1], 6)
])

def test_min_cost(cost: List[int], min_cost: int)->None:
    assert min_cost_stairs(cost) == min_cost