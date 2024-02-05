import lc20
import pytest

@pytest.mark.parametrize(
    ("input_1", "output"),
    [
        ("()", True),
        ('()[]{}', True),
        ("(]", False),
    ]
)

def test_isValid(input_1, output):
    s = lc20.Solution()
    calculated_res = s.isValid(input_1)
    assert calculated_res == output
