from ..extended_utils import get_volume
import pytest

def test_get_volume():
    assert get_volume(2, 3, 4) == 24

def test_get_volume_with_negative_values():
    with pytest.raises(ValueError):
        get_volume(12, 3, -5)

def test_get_volume_with_none_values():
    with pytest.raises(TypeError):
        get_volume(None, 3, 4)

@pytest.mark.xfail
def test_get_volume_with_none_values_xfail():
    get_volume(None, 3, 4)