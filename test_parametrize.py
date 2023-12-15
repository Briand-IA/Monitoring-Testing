
import pytest
from fonction_math import add


@pytest.mark.parametrize("input1, input2, expected", [(1, 2, 3), (-1, 1, 0), (-1, -1, -2)])
def test_addition(input1, input2, expected):
    result = add(input1, input2)
    assert result == expected
