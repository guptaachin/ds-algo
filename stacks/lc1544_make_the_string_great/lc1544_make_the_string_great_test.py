import lc1544_make_the_string_great
import pytest

@pytest.mark.parametrize(
    ("input_1", "output"),
    [
        # parametrized test case 1
        ("leEeetcode","leetcode"),
        # parametrized test case 2
        ("abBAcC",""),
    ]
)

# This test will run once per test case
def test_problem(input_1, output):
    s = lc1544_make_the_string_great.Solution()
    assert s.makeGood(input_1) == output
