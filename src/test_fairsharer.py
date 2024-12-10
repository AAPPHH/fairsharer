import pytest
import numpy as np
from fair_sharer import fair_sharer

test_cases = [
    ([0, 1000, 800, 0], 1, 0.1, [100, 800, 900, 0]),  # Testfall 1
    ([0, 1000, 800, 0], 2, 0.1, [100, 890, 720, 90]),  # Testfall 2
    ([0, 1000, 800, 0], 3, 0.1, [189, 712, 809, 90]),  # Testfall 3
    ([0, 1000, 800, 0], 0, 0.1, [0, 1000, 800, 0]),  # Testfall 4
    ([100, 100, 100, 100], 5, 0.1, [82.488, 109.411, 100.91, 107.191]),  # Testfall 5 (korrigiert)
    ([0, 1000, 800, 0], 1, 0.2, [200, 600, 1000, 0]),  # Testfall 6 (korrigiert)
]


@pytest.mark.parametrize("values, num_iterations, share, expected", test_cases)
def test_fair_sharer(values, num_iterations, share, expected):
    result = fair_sharer(values, num_iterations, share)
    assert np.allclose(result, expected), f"Expected {expected}, got {result}"

if __name__ == "__main__":
    pytest.main(["-v"])
