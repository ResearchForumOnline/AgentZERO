"""
Example script demonstrating usage of the quantum‑inspired models.

This script imports functions from the other projects in the `big_projects` collection
and evaluates them on sample inputs.  The results illustrate how the models can be
used together to analyse complex systems.

To run this script directly, ensure that the parent directories are on your
Python path (e.g. by running from the root of the repository or modifying
`sys.path` accordingly).
"""

import sys
import os

# Add parent directories to sys.path so that imports work when running this script
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.append(parent_dir)

try:
    from big_projects.adaptive_decision_framework.adaptive_model import adaptive_decision
    from big_projects.genetic_adaptation_simulator.simulator import genetic_adaptation
    from big_projects.quantum_key_solver.quantum_key import quantum_key
    from big_projects.cognitive_optimization_engine.cognitive_optimization import cognitive_optimization
except ImportError as e:
    raise ImportError(
        "Failed to import modules. Make sure the other projects are accessible on the PYTHONPATH."
    ) from e



def main() -> None:
    print("Quantum AI Examples\n====================\n")

    # Adaptive Decision example
    xs = [0.5, 1.0, 1.5]
    z_values = adaptive_decision(xs, y=1.0, psi=1.0, Omega=0.5, b1=1.0, b2=2.0,
                                alpha=1.0, beta=0.4, gamma=0.2, nu=0.1,
                                eta=1.0, theta=0.5, Q=1.0, lam=0.1)
    print("Adaptive Decision (Z) values:")
    for x, z in zip(xs, z_values):
        print(f"  Z({x:.2f}) = {z:.4f}")
    print()

    # Genetic Adaptation example
    xs_ga = [-1.0, 0.0, 1.0]
    g_values = genetic_adaptation(xs_ga, Q=1.0, b1=1.0, b2=1.5, alpha=0.5, beta=0.5,
                                  gamma=0.3, eta=1.0, theta=0.5, lam=0.0)
    print("Genetic Adaptation (G) values:")
    for x, g in zip(xs_ga, g_values):
        print(f"  G({x:.2f}) = {g:.4f}")
    print()

    # Quantum Key example
    xs_qk = [-0.5, 0.0, 0.5]
    f_values = quantum_key(xs_qk, Q=1.0, b1=1.0, b2=1.0, alpha=0.2, beta=0.3,
                           gamma=0.1, eta=1.0, theta=0.5, lam=0.0)
    print("Quantum Key (F) values:")
    for x, f in zip(xs_qk, f_values):
        print(f"  F({x:.2f}) = {f:.4f}")
    print()

    # Cognitive Optimization example
    xs_co = [0.0, 0.5]
    ys_co = [0.0, 0.5]
    co_matrix = cognitive_optimization(xs_co, ys_co, Z=1.0, Q=1.0, b1=1.0, b2=1.0,
                                       eta=0.5, chi=0.5, lam=0.1, psi=0.1,
                                       xi=1.0, alpha=1.0, beta=0.2, gamma=0.1,
                                       phi=1.0, theta=0.2, nu=0.2,
                                       omega=1.0, tau=0.1)
    print("Cognitive Optimization (C) matrix:")
    for i, x in enumerate(xs_co):
        for j, y in enumerate(ys_co):
            print(f"  C({x:.2f}, {y:.2f}) = {co_matrix[i][j]:.4f}")
    print()

    print("Example complete.")


if __name__ == "__main__":
    main()