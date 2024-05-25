import numpy as np
import matplotlib.pyplot as plt
from scipy.special import legendre
from scipy.integrate import quad

# Funkcje do aproksymacji
def linear(x):
    return x

def absolute(x):
    return np.abs(x)

def polynomial(x):
    return x**3 - 2*x**2 + 1

def trigonometric(x):
    return np.sin(x)

# Schemat Hornera
def horner_scheme(coefficients, x):
    result = coefficients[0]
    for coef in coefficients[1:]:
        result = result * x + coef
    return result

# Wybór funkcji do aproksymacji
print("Wybierz funkcję do aproksymacji:")
print("1. Funkcja liniowa (y = x)")
print("2. Funkcja |x|")
print("3. Funkcja wielomianowa (y = x^3 - 2x^2 + 1)")
print("4. Funkcja trygonometryczna (y = sin(x))")
choice = int(input("Podaj numer funkcji: "))

if choice == 1:
    function = linear
elif choice == 2:
    function = absolute
elif choice == 3:
    function = polynomial
elif choice == 4:
    function = trigonometric
else:
    print("Niepoprawny wybór funkcji.")
    exit()

# Parametry aproksymacji
interval_start = float(input("Podaj początek przedziału aproksymacji: "))
interval_end = float(input("Podaj koniec przedziału aproksymacji: "))
degree = int(input("Podaj stopień wielomianu aproksymującego: "))

# Przeskalowanie funkcji na przedział [-1, 1]
def rescaled_function(t):
    x = 0.5 * (interval_end - interval_start) * t + 0.5 * (interval_end + interval_start)
    return function(x)

# Obliczanie współczynników wielomianów Legendre'a
coefficients = []
for n in range(degree + 1):
    Pn = legendre(n)
    numerator, _ = quad(lambda t: rescaled_function(t) * Pn(t), -1, 1)
    denominator, _ = quad(lambda t: Pn(t)**2, -1, 1)
    coefficient = numerator / denominator
    coefficients.append(coefficient)

# Obliczanie wartości aproksymowanego wielomianu Legendre'a
x_values = np.linspace(interval_start, interval_end, 100)
y_values_approx = np.array([horner_scheme(coefficients, (2 * x - interval_end - interval_start) / (interval_end - interval_start)) for x in x_values])

# Obliczanie wartości funkcji oryginalnej
y_values_original = function(x_values)

# Wykres danych oryginalnych i aproksymowanych
plt.plot(x_values, y_values_original, color='red', label='Funkcja oryginalna')
plt.plot(x_values, y_values_approx, color='blue', label='Aproksymacja Legendre\'a')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Aproksymacja wielomianem Legendre\'a')
plt.legend()
plt.grid(True)
plt.show()

# Obliczanie błędu aproksymacji
def error_function(t):
    x = 0.5 * (interval_end - interval_start) * t + 0.5 * (interval_end + interval_start)
    return (function(x) - horner_scheme(coefficients, t))**2

approximation_error, _ = quad(error_function, -1, 1)
approximation_error = np.sqrt(approximation_error)
print("Błąd aproksymacji:", approximation_error)
