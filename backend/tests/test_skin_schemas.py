import pytest

@pytest.mark.parametrize("value",[0.0,0.5,1.0])
def test_valid_float(value):
  assert 0 <= value <= 1