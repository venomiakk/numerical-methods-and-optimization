import tkinter as tk
from tkinter import messagebox, ttk
import re
import wykresy
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import legendre
import horner
import approx
import funkcje


def draw_graph(selection, root, fa_val, fb_val):
    funkcja = selection.current() + 1
    a = float(fa_val.get())
    b = float(fb_val.get())
    fig = wykresy.rysuj(funkcja, a, b)

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()

    canvas.get_tk_widget().place(x=220, y=50)


def draw_approx(selected_func, selected_mode, mode_input, root, a_val, b_val, node_val):
    """
    @param selected_func: aproksymowana funkcja
    @param selected_mode: 0 - stopien wielomianu, 1 - blad aproksymacji
    @param mode_input: k stopien wielomianu lub wartosc bledu
    @param root: okienko
    @param a_val: poczatek przedzialu
    @param b_val: koniec przedzialu
    @param node_val: liczba wezlow
    @return:
    """
    # print("draw approx")
    f_type = selected_func.current() + 1
    f = funkcje.wybor_funkcji(f_type)
    mode = selected_mode.current()
    mode_val = mode_input.get()
    if mode == 0:
        mode_val = int(mode_val)
    else:
        mode_val = float(mode_val)

    a = float(a_val.get())
    b = float(b_val.get())
    nodes = int(node_val.get())
    # print(f"funkcja {f}, {type(f)}")
    # print(f"tryb {mode}")
    # print(f"wart trybu {mode_val}, {type(mode_val)}")
    # print(f"a {a}")
    # print(f"b {b}")
    # print(f"wezly {nodes}")
    if mode == 0:
        wsp, err = approx.wsp_approx(mode_val, f, a, b, nodes)
        print(wsp)
        print(err)
        fig = wykresy.rysuj_approx(wsp, mode_val, a, b, f)
        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.draw()

        canvas.get_tk_widget().place(x=220, y=50)

        flabel = tk.Label(root, text=f"wartosc: {err}", width=6)
        flabel.place(x=220, y=550)
    else:
        print("blad")


def approximation(root, funkcja, selected_mode, mode_input):
    print("asda")

def only_int(P):
    if re.match("^[0-9]*$", P):
        return True
    return False


def only_float(P):
    if re.match("^-?[0-9]*.?[0-9]*$", P):
        return True
    return False


def valid_float_int(P):
    if re.match("^-?[0-9]*.?[0-9]*$", P) or re.match("^[0-9]*$", P):
        return True
    return False


def gui_interface():
    root = tk.Tk()
    root.geometry("880x600")
    root.title("Aproksymacja")

    validate_float = root.register(only_float)
    validate_int = root.register(only_int)
    validate_float_int = root.register(valid_float_int)

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

    # TODO APROKSYMACJA

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

    mode = ttk.Combobox(
        state="readonly",
        values=["Stopien wielomianu", "Blad aproksymacji"],
        width=21
    )
    mode.place(x=20, y=420)
    mode.set("Stopien wielomianu")

    mode_input = tk.Entry(root, width=10, validate="key", validatecommand=(validate_float_int, '%P'))
    mode_input.place(x=50, y=450)

    '''
    mode:
        0 - stopien - tj. Px gdzie x to stopien czyli jeden z wielomianow Legendre'a
        1 - blad - tj. zwiekszanie iteracyjnie stopnia poki blad nie jest mniejszy niz zadany
    '''
    if mode == 0:
        print("Stopien wielomianu")
    else:
        print("iteeracyjnie blad")
    # rysowanie aproksymacji
    show_approx_btn = tk.Button(text="Rysuj wykres",
                                command=lambda: draw_approx(function, mode, mode_input, root, a_val,
                                                            b_val, node_val))
    show_approx_btn.place(x=42, y=495)

    root.mainloop()


if __name__=="__main__":
    gui_interface()