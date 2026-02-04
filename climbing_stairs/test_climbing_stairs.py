import pytest
from climbing_stairs import ways
@pytest.mark.parametrize('num_stairs, num_ways', [
    (2,2),
    (1,1),
    (3,3),
    (8,34),
    (10,89)
])
def test_climbing_stairs(num_stairs: int, num_ways: int)->None:
    assert ways.climbing_stairs(num_stairs) == num_ways



