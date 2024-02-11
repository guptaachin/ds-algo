import lc70_climbing_stairs
import pytest

@pytest.mark.parametrize(
    ("num_stairs", "num_ways"),
    [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 5),
    ]
)

def test_problem(num_stairs, num_ways):
    s = lc70_climbing_stairs.Solution()
    assert num_ways == s.climbStairs(num_stairs)
