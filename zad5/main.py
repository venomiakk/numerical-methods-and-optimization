import sympy as sp
import numpy as np
import legendre
import horner
import gui

def przyklad():
    # Przykład użycia:
    k = 3
    coefficients = legendre.coefficients(k)

    print(f"Współczynniki wielomianu Legendre'a P_{k}(x): {coefficients}")
    print(horner.oblicz(coefficients, 1))


if __name__ == "__main__":
    gui.gui_interface()