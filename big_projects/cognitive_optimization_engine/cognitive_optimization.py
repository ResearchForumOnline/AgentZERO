"""
Simplified implementation of the Cognitive Optimization Equation (Skynet‑Zero).

This module defines a function `cognitive_optimization` computing a reduced
form of the cognitive optimization equation.  The implementation focuses on
continuous components and omits the delta function term for discrete shifts.
An example at the bottom demonstrates how to evaluate the function on a
grid of `x` and `y` values.
"""

from __future__ import annotations

import math
from typing import Union, Sequence, Tuple

Number = Union[int, float]

def cognitive_optimization(
    x: Number | Sequence[Number],
    y: Number | Sequence[Number],
    Z: Number = 1.0,
    Q: Number = 1.0,
    b1: Number = 1.0,
    b2: Number = 1.0,
    eta: Number = 1.0,
    chi: Number = 1.0,
    lam: Number = 0.0,
    psi: Number = 0.0,
    xi: Number = 1.0,
    alpha: Number = 1.0,
    beta: Number = 0.0,
    gamma: Number = 0.0,
    phi: Number = 1.0,
    theta: Number = 0.0,
    nu: Number = 0.0,
    omega: Number = 1.0,
    tau: Number = 0.0,
) -> list[list[float]]:
    """Compute the simplified Cognitive Optimization (C) function over a grid of x and y.

    Parameters
    ----------
    x, y : scalar or sequence of scalars
        Independent variables.  If sequences are provided, the function returns a
        matrix of results with shape `(len(x), len(y))`.
    Z, Q : scalars
        Additional variables/parameters.
    b1, b2 : scalars
        Coefficients for the log term and amplitude.
    eta, chi, lam, psi, xi, alpha, beta, gamma, phi, theta, nu, omega, tau : scalars
        Parameters controlling the shape of the equation.

    Returns
    -------
    list[list[float]]
        Matrix of C values for each (x, y) pair.
    """
    xs = [x] if isinstance(x, (int, float)) else list(x)
    ys = [y] if isinstance(y, (int, float)) else list(y)
    result_matrix: list[list[float]] = []

    for xi in xs:
        row: list[float] = []
        for yi in ys:
            # Compute logarithmic pre‑factor
            arg_log = b1 + eta * Q * xi + chi * yi
            if arg_log <= 0:
                arg_log = 1e-12
            log_term = math.log(arg_log)

            # Exponential growth factor
            exp_term = math.exp(lam * xi + psi * yi)

            # Inner combination of terms
            inner = (
                (xi * xi * Z + chi * yi) ** alpha  # (xi*Z + chi*y)^alpha simplified with xi squared to avoid negative domain for non‑integer alpha
                + beta * math.sin(phi * xi + psi * yi)
                + gamma * math.exp(-theta * (Q * xi * xi + chi * yi * yi))
                + nu * math.cos(omega * yi + tau * xi)
            )

            # Combine primary part
            primary = b2 * log_term * exp_term * inner

            # Additional polynomial and linear terms
            additional = theta * (xi * xi + yi * yi) + Q * Q + tau * Z

            c_value = primary + additional
            row.append(c_value)
        result_matrix.append(row)
    return result_matrix


if __name__ == "__main__":
    # Demonstrate usage by computing C on a 3x3 grid
    import numpy as np
    xs = np.linspace(-1.0, 1.0, num=3)
    ys = np.linspace(-1.0, 1.0, num=3)
    grid = cognitive_optimization(xs, ys, Z=1.0, Q=1.0, b1=1.0, b2=1.0,
                                  eta=0.5, chi=0.5, lam=0.2, psi=0.1,
                                  xi=1.0, alpha=1.2, beta=0.4, gamma=0.3,
                                  phi=1.0, theta=0.2, nu=0.2,
                                  omega=1.0, tau=0.1)
    # Print results
    for i, xv in enumerate(xs):
        for j, yv in enumerate(ys):
            print(f"x={xv:.2f}, y={yv:.2f}\tC={grid[i][j]:.4f}")