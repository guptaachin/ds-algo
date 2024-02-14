import lc300_longest_increasing_subsequence
import pytest

@pytest.mark.parametrize(
    ("sequence", "output"),
    [
        ([10,9,2,5,3,7,101,18], 4),
        ([0,1,0,3,2,3], 4),
        ([8,8,8,8,8,8,8], 1),
    ]
)

# This test will run once per test case
def test_problem(sequence, output):
    s = lc300_longest_increasing_subsequence.Solution()
    assert s.lengthOfLIS(sequence) == output
