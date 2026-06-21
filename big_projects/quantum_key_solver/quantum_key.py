"""
Quantum Key Equation (F function) implementation.

The F function models multi‑dimensional problem solving using a combination
of logarithmic, exponential and piecewise components.  Discrete shifts
are approximated using Heaviside step functions to indicate when the
independent variable crosses zero.  A demonstration in the `__main__`
section illustrates how to compute F for a range of values.
"""

from __future__ import annotations

import math
from typing import Union, Sequence

Number = Union[int, float]

def heaviside(x: Number) -> int:
    return 1 if x > 0 else 0

def quantum_key(
    x: Number | Sequence[Number],
    Q: Number = 1.0,
    b1: Number = 1.0,
    b2: Number = 1.0,
    alpha: Number = 0.0,
    beta: Number = 0.0,
    gamma: Number = 0.0,
    eta: Number = 1.0,
    theta: Number = 1.0,
    lam: Number = 0.0,
) -> list[float]:
    """Compute the Quantum Key (F) function.

    Parameters mirror those of the Z and G functions but with a simpler structure:

    - `x`: scalar or sequence, the independent variable.
    - `Q`: scaling parameter.
    - `b1`, `b2`: coefficients for the log term and amplitude.
    - `alpha`, `beta`, `gamma`: weights for the negative shift, positive shift and Gaussian decay terms.
    - `eta`, `theta`: scaling for the logarithm and Gaussian decay.
    - `lam`: exponent for the exponential growth term.

    Returns a list of computed F values.
    """
    xs = [x] if isinstance(x, (int, float)) else list(x)
    results: list[float] = []
    for xi in xs:
        # Logarithmic part with epsilon
        arg_log = b1 + eta * Q * xi
        if arg_log <= 0:
            arg_log = 1e-12
        log_term = math.log(arg_log)

        # Exponential growth
        exp_term = math.exp(lam * xi)

        # Piecewise term: base x plus adjustments
        delta_neg = heaviside(-xi)
        delta_pos = heaviside(xi)
        base = xi + alpha * delta_neg + beta * delta_pos + gamma * math.exp(-theta * Q * xi * xi)

        f_val = b2 * log_term * exp_term * base
        results.append(f_val)
    return results


if __name__ == "__main__":
    import numpy as np
    xs = np.linspace(-1.5, 1.5, num=7)
    values = quantum_key(xs, Q=1.0, b1=1.0, b2=1.5, alpha=0.3, beta=0.6, gamma=0.2,
                         eta=1.0, theta=0.5, lam=0.1)
    for x_val, f_val in zip(xs, values):
        print(f"x={x_val:.2f}\tF={f_val:.4f}")