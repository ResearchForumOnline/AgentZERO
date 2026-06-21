"""
Implementation of the Adaptive Learning and Decision Equation (Z function).

This module defines a function `adaptive_decision` that computes the value of the
Z equation for given input variables and parameters.  The equation blends
logarithmic and exponential growth with trigonometric and Gaussian terms to
model adaptive learning and decision processes.  For numerical stability the
logarithmic term uses a small epsilon if the argument becomes non‑positive.

The implementation treats the discrete delta term (\(\delta_{\infty}(x)\)) as zero,
which is appropriate for continuous simulations.  Users requiring specific
behaviour at integer thresholds can extend the function accordingly.

Example usage is provided in the `__main__` block at the end of the file.
"""

from __future__ import annotations

import math
from typing import Union, Sequence

Number = Union[int, float]

def adaptive_decision(
    x: Number | Sequence[Number],
    y: Number = 1.0,
    psi: Number = 1.0,
    Omega: Number = 1.0,
    b1: Number = 1.0,
    b2: Number = 1.0,
    alpha: Number = 1.0,
    beta: Number = 0.0,
    gamma: Number = 0.0,
    delta: Number = 0.0,
    eta: Number = 1.0,
    theta: Number = 1.0,
    Q: Number = 1.0,
    lam: Number = 0.0,
    nu: Number = 0.0,
) -> list[float]:
    """Compute the Adaptive Decision (Z) function.

    Parameters
    ----------
    x : scalar or sequence of scalars
        The primary independent variable.  If a sequence is provided, the function
        returns a list of results for each element.
    y : scalar, optional
        Secondary variable influencing sinusoidal and power terms.
    psi : scalar, optional
        Frequency coefficient for the sine term.
    Omega : scalar, optional
        Frequency coefficient for the cosine term.
    b1, b2 : scalars, optional
        Coefficients controlling the logarithmic pre‑factor.
    alpha : scalar, optional
        Exponent for the power term on (x + y).
    beta, gamma, nu : scalars, optional
        Amplitude coefficients for the sine, exponential decay, and cosine terms.
    delta : scalar, optional
        Placeholder for discrete delta contributions.  Currently unused.
    eta, theta, Q, lam : scalars, optional
        Parameters modulating the decay and growth terms.

    Returns
    -------
    list[float]
        Computed Z values corresponding to each element of `x`.
    """
    # Convert single value into an iterable for unified processing
    xs = [x] if isinstance(x, (int, float)) else list(x)
    results: list[float] = []

    for xi in xs:
        # Ensure argument for log is positive; add a small epsilon if needed
        arg_log = b1 + eta * Q * xi
        if arg_log <= 0:
            arg_log = 1e-12
        try:
            log_term = math.log(arg_log)
        except ValueError:
            log_term = -math.inf  # Should not occur with epsilon

        # Exponential growth factor
        exp_term = math.exp(lam * xi)

        # Numerator: combination of power, sine, gaussian decay and cosine terms
        power_term = (xi + y) ** alpha
        sine_term = beta * math.sin(psi * xi)
        gaussian_term = gamma * math.exp(-theta * Q * xi * xi)
        cosine_term = nu * math.cos(Omega * y)
        numerator = power_term + sine_term + gaussian_term + cosine_term

        # Denominator: currently 1 because delta_infinity is ignored in continuous domain
        denominator = 1.0

        # Combine components
        z_value = b2 * log_term * exp_term * numerator / denominator
        results.append(z_value)

    return results


if __name__ == "__main__":
    # Demonstrate function usage with default parameters
    import numpy as np

    # Generate a range of x values
    xs = np.linspace(0.1, 2.0, num=10)
    # Compute Z for each x
    zs = adaptive_decision(xs, y=1.0, psi=1.5, Omega=0.8, b1=1.0, b2=2.0,
                            alpha=1.2, beta=0.5, gamma=0.3, nu=0.2,
                            eta=0.8, theta=0.5, Q=1.0, lam=0.1)
    # Display results
    for x_val, z_val in zip(xs, zs):
        print(f"x={x_val:.2f}\tZ={z_val:.4f}")