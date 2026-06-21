"""
Simplified implementation of the Genetic Adaptation Equation (G function).

This module defines `genetic_adaptation`, a function that computes the G equation
for one or more input values.  The delta functions are approximated using
Heaviside step functions to trigger discrete shifts when the input crosses
zero.  A demonstration in the `__main__` block iterates the function over a
range of `x` values and prints the results.
"""

from __future__ import annotations

import math
from typing import Union, Sequence

Number = Union[int, float]

def heaviside(x: Number) -> int:
    """Return 1 if x > 0, 0 if x <= 0. Used to approximate delta-positive and delta-negative."""
    return 1 if x > 0 else 0


def genetic_adaptation(
    x: Number | Sequence[Number],
    y: Number = 0.0,
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
    """Compute the Genetic Adaptation (G) function.

    Parameters
    ----------
    x : scalar or sequence of scalars
        Independent variable (e.g. time).
    y : scalar, unused in this simplified form but kept for potential extensions.
    Q : scalar, modulates the scale of adaptation.
    b1, b2 : scalars, control the logarithmic term and amplitude.
    alpha, beta, gamma : scalars, control negative and positive adaptation and exponential decay.
    eta, theta : scalars, scale the log and exponential decay terms.
    lam : scalar, exponential growth rate.

    Returns
    -------
    list[float]
        Computed G values for each input `x`.
    """
    xs = [x] if isinstance(x, (int, float)) else list(x)
    results: list[float] = []
    for xi in xs:
        # Compute logarithmic term with small epsilon to prevent log(<=0)
        arg_log = b1 + eta * Q * xi
        if arg_log <= 0:
            arg_log = 1e-12
        log_term = math.log(arg_log)

        # Exponential growth factor
        exp_term = math.exp(lam * xi)

        # Discrete shifts approximated using Heaviside step functions
        delta_neg = heaviside(-xi)  # 1 if xi < 0
        delta_pos = heaviside(xi)   # 1 if xi > 0

        # Adaptation factor
        adapt = 1 + alpha * delta_neg + beta * delta_pos + gamma * math.exp(-theta * Q * xi * xi)

        g_value = b2 * log_term * exp_term * adapt
        results.append(g_value)
    return results


if __name__ == "__main__":
    import numpy as np
    xs = np.linspace(-2.0, 2.0, num=9)
    values = genetic_adaptation(xs, Q=1.0, b1=1.0, b2=2.0, alpha=0.5, beta=0.7, gamma=0.3,
                                eta=0.8, theta=0.4, lam=0.1)
    for x_val, g_val in zip(xs, values):
        print(f"x={x_val:.2f}\tG={g_val:.4f}")