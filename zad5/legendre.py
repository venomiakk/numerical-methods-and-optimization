import sympy as sp
import horner

def coefficients(k):
    x = sp.symbols('x')
    expr = (x ** 2 - 1) ** k

    # Oblicz k-tą pochodną wyrażenia (x^2 - 1)^k
    derivative = sp.diff(expr, x, k)

    # Podziel przez 2^k i k!
    factorial_k = sp.factorial(k)
    result = (1 / (2 ** k * factorial_k)) * derivative

    # Rozwiń wielomian i wyodrębnij współczynniki
    poly = sp.Poly(result, x)
    coefficients = poly.all_coeffs()

    # Konwersja do listy liczb (jeśli są to współczynniki typu sympy)
    coefficients = [float(coef) for coef in coefficients]

    return coefficients


if __name__=='__main__':
    cs = coefficients(4)
    print(horner.oblicz(cs, 2))