# This code was AUTOGENERATED.
# Change it to fit your test case.
import lc198_house_robber
import pytest

@pytest.mark.parametrize(
    ("nums", "output"),
    [
        ([1,2,3,1], 4),
        ([2,7,9,3,1], 12),
    ]
)

# This test will run once per test case
def test_problem(nums, output):
    s = lc198_house_robber.Solution()
    calculated_res = s.rob(nums)
    assert calculated_res == output
