import pytest

import climbing_stairs.climbing_stairs as climbing_stairs
@pytest.mark.parametrize('num_stairs, ways', [
    (2,2),
    (1,2),
    (3,3),
    (8,34),
    (10,89)
])
def test_climbing_stairs(num_stairs: int, ways: int)->None:
    assert climbing_stairs.climbing_stairs(num_stairs) == ways



