import lc861
import pytest

@pytest.mark.parametrize(
    ("grid", "output"),
    [
        ([[0,0,1,1],[1,0,1,0],[1,1,0,0]], 39),
        ([[0]], 1),
    ]
)

def test_problem(grid, output):
    s = lc861.Solution()
    # Call you program here. For example:
    calculated_res = s.matrixScore(grid)
    assert calculated_res == output
