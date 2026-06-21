# Genetic Adaptation Simulator

This project implements a simplified form of the *Genetic Adaptation Equation* (G function).  The equation is a conceptual model for systemic learning inspired by genetic algorithms, capturing random variations, environment‑specific adaptations and dynamic feedback.

## Contents

- `simulator.py` – defines a function `genetic_adaptation` computing the G function for a sequence of input values.  It also includes a simple simulation routine in the `__main__` section that iterates the model over a range of `x` values and prints the results.
- `README.md` – this documentation.

## The G Equation

The genetic adaptation equation has the form

\[G(x, y, Q) = b_2 \cdot \log(b_1 + \eta \cdot Q \cdot x) \cdot e^{\lambda x} \cdot \bigl(1 + \alpha \cdot \delta_{-}(x) + \beta \cdot \delta_{+}(x) + \gamma \cdot e^{-\theta Q x^2}\bigr)\]

where:

- `x` is the independent variable (e.g. time or iteration).
- `Q` modulates the scale of adaptation.
- The `delta` functions signal discrete shifts when `x` crosses zero; in this implementation they are approximated using Heaviside step functions.
- Coefficients `alpha`, `beta` and `gamma` control the influence of negative adaptation, positive adaptation and Gaussian decay.
- Logarithmic and exponential terms govern growth dynamics.

## Usage

Run the simulation script:

```bash
python simulator.py
```

It will compute `G(x, y, Q)` over a range of `x` values and print the results.  You can adjust the parameters at the bottom of `simulator.py` to explore different behaviours.

## Background

The Genetic Adaptation model is part of the mathematical toolkit powering Zero’s reasoning framework.  It draws inspiration from genetic algorithms and evolutionary systems to model how AI agents adapt over time.