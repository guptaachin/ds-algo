import pytest
import lc2966

@pytest.mark.parametrize(
    ("input_nums", "input_k", "output_matrix"),
    [
        ([1, 3, 4, 8, 7, 9, 3, 5, 1], 2, [[1, 1, 3], [3, 4, 5], [7, 8, 9]]),
        ([1,3,3,2,7,3], 2, []),
    ]
)

def test_divideArray(input_nums, input_k, output_matrix):
    s = lc2966.Solution()
    calculated_res = s.divideArray(input_nums, input_k)
    assert calculated_res == output_matrix
