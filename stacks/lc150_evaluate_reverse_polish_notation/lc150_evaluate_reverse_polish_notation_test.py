import lc150_evaluate_reverse_polish_notation
import pytest

@pytest.mark.parametrize(
    ("rpn", "output"),
    [
        (["2","1","+","3","*"], 9),
        (["4","13","5","/","+"], 6),
        (["10","6","9","3","+","-11","*","/","*","17","+","5","+"], 22),
    ]
)

def test_problem(rpn, output):
    s = lc150_evaluate_reverse_polish_notation.Solution()
    assert s.evalRPN(rpn) == output
