"""
Unit tests for quantum‑inspired models.

These tests verify that the core functions defined in the projects return
expected types and produce consistent values for known inputs.  The tests
use simple assertions to avoid dependencies on external testing frameworks.

To run these tests with pytest, install pytest (``pip install pytest``) and run

```
pytest -q big_projects/tests
```
"""

import math

from big_projects.adaptive_decision_framework.adaptive_model import adaptive_decision
from big_projects.genetic_adaptation_simulator.simulator import genetic_adaptation
from big_projects.quantum_key_solver.quantum_key import quantum_key
from big_projects.cognitive_optimization_engine.cognitive_optimization import cognitive_optimization


def test_adaptive_decision_returns_float_list() -> None:
    result = adaptive_decision([1.0, 2.0], y=1.0, psi=0.5, Omega=0.5)
    assert isinstance(result, list), "adaptive_decision should return a list"
    assert all(isinstance(v, float) for v in result), "adaptive_decision values should be floats"


def test_genetic_adaptation_signs() -> None:
    values = genetic_adaptation([-1.0, 0.0, 1.0], Q=1.0, alpha=0.5, beta=0.7, gamma=0.3, eta=0.8)
    # Negative x should include alpha contribution, positive x should include beta
    assert values[0] < values[2], "G(x) should reflect negative vs positive adaptation"  # rough comparison


def test_quantum_key_continuity() -> None:
    # F(0) should be near zero because log(b1) * base(x) and base includes x
    result = quantum_key([0.0], Q=1.0, b1=1.0, b2=1.0, alpha=0.3, beta=0.6, gamma=0.2)
    assert abs(result[0]) < 1e-6, "Quantum key value at zero should be approximately zero"


def test_cognitive_optimization_matrix_shape() -> None:
    xs = [-0.5, 0.0, 0.5]
    ys = [-0.5, 0.0, 0.5]
    matrix = cognitive_optimization(xs, ys, Z=1.0, Q=1.0, b1=1.0, b2=1.0,
                                   eta=0.5, chi=0.5, lam=0.1, psi=0.1,
                                   xi=1.0, alpha=1.2, beta=0.3, gamma=0.2,
                                   phi=1.0, theta=0.2, nu=0.2,
                                   omega=1.0, tau=0.1)
    assert len(matrix) == len(xs), "C matrix should have as many rows as xs"
    for row in matrix:
        assert len(row) == len(ys), "C matrix should have as many columns as ys"