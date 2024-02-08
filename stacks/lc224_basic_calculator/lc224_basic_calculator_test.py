# This code was AUTOGENERATED.
# Change it to fit your test case.
import lc224_basic_calculator
import pytest

@pytest.mark.parametrize(
    ("input_1", "output"),
    [
        ("1 + 1", 2),
        (" 2-1 + 2", 3),
        ("(1+(4+5+2)-3)+(6+8)", 23),
    ]
)

def test_problem(input_1, output):
    s = lc224_basic_calculator.Solution()
    calculated_res = s.calculate(input_1)
    assert calculated_res == output
