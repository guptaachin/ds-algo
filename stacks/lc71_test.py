import lc71

import pytest

@pytest.mark.parametrize(
    ("input_1", "output"),
    [
        ("/home/", "/home"),
        ("/../", "/"),
    ]
)

def test_problem(input_1, output):
    s = lc71.Solution()
    cal = s.simplifyPath(input_1)
    assert cal == output