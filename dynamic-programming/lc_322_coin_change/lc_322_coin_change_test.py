import lc_322_coin_change
import pytest

@pytest.mark.parametrize(
    ("coins", "amount", "output"),
    [
        ([1,2,5], 11, 3),
        ([2], 3, -1),
        ([4,4,5,2,3,1], 10, 2),
    ]
)

# This test will run once per test case
def test_problem(coins, amount, output):
    s = lc_322_coin_change.Solution()
    calculated_res = s.coinChange(coins, amount)
    assert calculated_res == output
