import pytest
from fair_sharer import fair_sharer

def test_fair_sharer():
    result = fair_sharer([0, 1000, 800, 0], 1, 0.1)
    expected = [100, 800, 900, 0]
    assert result == pytest.approx(expected, rel=1e-2), f"Expected {expected}, but got {result}"

    result = fair_sharer([0, 1000, 800, 0], 2, 0.1)
    expected = [100, 890, 720, 90]
    assert result == pytest.approx(expected, rel=1e-2), f"Expected {expected}, but got {result}"

    result = fair_sharer([0, 1000, 800, 0], 1, 0.0)
    expected = [0, 1000, 800, 0]
    assert result == pytest.approx(expected, rel=1e-2), f"Expected {expected}, but got {result}"

    result = fair_sharer([-100, 200, -50, 0], 1, 0.1)
    expected = [-100, 180, -50, 20]
    assert result == pytest.approx(expected, rel=1e-2), f"Expected {expected}, but got {result}"

if __name__ == "__main__":
    pytest.main()
