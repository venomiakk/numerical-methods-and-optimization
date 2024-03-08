import bisekcja
import sieczne

if __name__ == '__main__':
    funkcja1 = [5, -3, 1, 6]
    funkcja2 = [1, 3, -5, 1]
    print(bisekcja.oblicz(funkcja2, 3, 0.5))
    print(sieczne.oblicz(funkcja1, -2, 0))

    # TODO: Pozmieniać metody tak aby działały na dowolnych funkcjacj, [biblioteka sympy (?)] oraz wybór warunku stopu
    # TODO: Dodać interfejs z możliwością wyboru funkcji, metody oraz warunku stopu (iteracje lub |x1-x2|)
    # TODO: Narysować wykresy
    