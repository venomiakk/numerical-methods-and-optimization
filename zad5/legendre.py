import sympy as sp
import horner

def coefficients(k):
    x = sp.symbols('x')
    expr = (x ** 2 - 1) ** k

    # obliczanie k-tej pochodnej (x^2 - 1)^k
    derivative = sp.diff(expr, x, k)

    # dzielenie przez 2^k i k!
    factorial_k = sp.factorial(k)
    result = (1 / (2 ** k * factorial_k)) * derivative

    # rozwiniecie wielomianu i wyodrebnienie wspolczynnikow
    poly = sp.Poly(result, x)
    coefficients = poly.all_coeffs()

    coefficients = [float(coef) for coef in coefficients]

    return coefficients


if __name__=='__main__':
    cs = coefficients(4)
    print(horner.oblicz(cs, 2))