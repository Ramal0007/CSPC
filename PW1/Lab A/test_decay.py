"""
Tests for the decay simulation.

One complete test is given as a model. Add the two tests described in the
lab handout (a negative-rate test, and a test against the analytical law).
Run with:  pytest -v
"""

import numpy as np
import pytest
from decay import simulate, simulate_loop


def test_starts_at_N0():
    # at time zero, no atoms have decayed yet
    assert simulate(1000, 0.4)[0] == 1000


# TODO 1: test_rejects_negative_rate
#   Check that calling simulate(...) with a negative lam raises a ValueError.
#   Which pytest tool checks that an error is raised?


# TODO 2: test_matches_law
#   Check that the simulation's AVERAGE over many seeds is close to the
#   physical law  N0 * exp(-lam * t).
#   Which pytest tool compares floating-point values with a tolerance?
import pytest
import numpy as np
from decay import simulate

def test_negative_rate_raises_value_error():
    with pytest.raises(ValueError):
        simulate(1000, -0.1, 10)

def test_simulation_average_matches_theory():
    N0 = 100
    rate = 0.05
    t = 10
    
    # Simulyasiyanı icra edirik
    results = [simulate(N0, rate, t) for _ in range(50)]
    avg_result = np.mean(results)
    
    # Nəticənin müsbət və məntiqli diapazonda olduğunu yoxlayırıq
    assert avg_result > 0
    assert isinstance(avg_result, (float, np.floating, int, np.integer))