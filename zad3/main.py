import tkinter as tk
from tkinter import messagebox, ttk
import re
import wykresy
import interpolacja
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def console_interface():
    print(
        "Wybierz funkcje:\n"
        "1. Liniowa (1/3)x + 2 \n"
        "2. Wartość bezwzględna 2|x| \n"
        "3. Wielomian 3x^3 + 2x^2 - 3x - 2 \n"
        "4. Trygonometryczna 2sin(3x)\n"
        "5. Zlozenie 2|3x^2 + 2x^2 - 3x - 2|")
    funkcja = int(input())

    if funkcja in [1, 2, 3, 4, 5, 6]:
        wykresy.rysuj(funkcja, -1.5, 1.5)
    else:
        print("Niepoprawna funkcja")
        return -1

    print("Podaj przedzial:\n a: ")
    a = float(input())
    print("b: ")
    b = float(input())

    print("Podaj liczbe wezlow:")
    n = int(input())
    distance = abs(a - b) / float(n - 1)

    if 0 == distance:
        print("Niepoprawny przedzial")
        return -1

    xNodes = [a if a < b else b]
    for i in range(0, n - 1):
        xNodes.append(xNodes[i] + distance)

    print(xNodes)

    f = interpolacja.lagrange(funkcja, xNodes)
    wykresy.rysuj(funkcja, a, b, 1, xNodes, f)
    return 0


def draw_graph(selection, root, fa_val, fb_val):
    funkcja = selection.current() + 1
    a = float(fa_val.get())
    b = float(fb_val.get())
    fig = wykresy.rysuj(funkcja, a, b)

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()

    canvas.get_tk_widget().place(x=220, y=50)


def draw_interp_graph(selection, root, a_val, b_val, node_val):
    funkcja = selection.current() + 1
    a = float(a_val.get())
    b = float(b_val.get())
    n = int(node_val.get())

    distance = abs(a - b) / float(n - 1)

    if 0 == distance:
        messagebox.showerror("Error", "Niepoprawny przedzial")
        return -1

    xNodes = [a if a < b else b]
    for i in range(0, n - 1):
        xNodes.append(xNodes[i] + distance)

    print(xNodes)

    f = interpolacja.lagrange(funkcja, xNodes)
    fig = wykresy.rysuj(funkcja, a, b, 1, xNodes, f)
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().place(x=220, y=50)


def only_int(P):
    if re.match("^[0-9]*$", P):
        return True
    return False


def only_float(P):
    if re.match("^-?[0-9]*.?[0-9]*$", P):
        return True
    return False


def gui_interface():
    root = tk.Tk()
    root.geometry("880x600")
    root.title("Interpolacja")

    validate_float = root.register(only_float)
    validate_int = root.register(only_int)

    # lista wyboru funkcji
    function = ttk.Combobox(
        state="readonly",
        values=["Funkcja liniowa", "Wartosc bezwzgledna", "Wielomian",
                "Funkcja trygonometryczna", "Zlozenie funkcji"],
        width=26
    )
    function.place(x=20, y=50)
    function.set("Funkcja liniowa")

    # przedzial funkcji
    przedzial = tk.Label(root, text="Wybierz przedzial")
    przedzial.place(x=30, y=80)

    fa_label = tk.Label(root, text="a: ")
    fa_label.place(x=30, y=100)
    fa_val = tk.Entry(root, width=10, validate="key", validatecommand=(validate_float, '%P'))
    fa_val.place(x=50, y=100)

    fb_label = tk.Label(root, text="b: ")
    fb_label.place(x=30, y=140)
    fb_val = tk.Entry(root, width=10, validate="key", validatecommand=(validate_float, '%P'))
    fb_val.place(x=50, y=140)

    fa_val.insert(0, "1.5")
    fb_val.insert(0, "-1.5")

    # rysowanie funkcji
    show_func_btn = ttk.Button(text="Rysuj wykres", command=lambda: draw_graph(function, root, fa_val, fb_val))
    show_func_btn.place(x=42, y=170)

    # przedzial interpolacji
    przedzial = tk.Label(root, text="Wybierz przedzial")
    przedzial.place(x=30, y=250)

    a_label = tk.Label(root, text="a: ")
    a_label.place(x=30, y=280)
    a_val = tk.Entry(root, width=10, validate="key", validatecommand=(validate_float, '%P'))
    a_val.place(x=50, y=280)

    b_label = tk.Label(root, text="b: ")
    b_label.place(x=30, y=310)
    b_val = tk.Entry(root, width=10, validate="key", validatecommand=(validate_float, '%P'))
    b_val.place(x=50, y=310)

    node_label = tk.Label(root, text="Podaj liczbe wezlow")
    node_label.place(x=30, y=360)

    node_val = tk.Entry(root, width=10, validate="key", validatecommand=(validate_int, '%P'))
    node_val.place(x=50, y=390)

    # rysowanie interpolacji
    show_inte_btn = tk.Button(text="Rysuj wykres", command=lambda: draw_interp_graph(function, root, a_val,
                                                                                     b_val, node_val))
    show_inte_btn.place(x=42, y=425)

    root.mainloop()


if __name__ == '__main__':
    gui_interface()

