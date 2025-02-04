from ..extended_utils import get_volume
import pytest

@pytest.mark.parametrize("height, width, depth, expected", [
    (2,3,4,24),
    (1,2,3,6),
    (3,4,5,60)
])
def test_get_volume(height, width, depth, expected):
    assert get_volume(height, width, depth) == expected
