# f(x) = sin(x) - 1/2x - funkcja

import math


def f(x, f_x):
    wynik = 0
    for i in range(len(f_x)):
        wynik += f_x[i] * x ** i
    return wynik


def x_i(x_p, x_k, f_x):
    x = x_k - (f(x_k, f_x) * (x_k - x_p) / (f(x_k, f_x) - f(x_p, f_x)))
    return x


def warunekCauchyego(x_p, x_k, f_x):
    return True if f(x_p, f_x) * f(x_k, f_x) < 0 else False


# def pochodna(f_x) :
#     fp_x = [0] * (len(f(x)) - 1)
#     for i in range(fp_x) :
#         fp_x[i] = f_x(i+1) * (i+1)
#     return fp_x


if __name__ == '__main__':
    f_x = [-3, -3, 1, 1]  # funkcja
    E = 0.001
    f_c = 1  # losowa wartość większa od E
    x_p = 1
    x_k = 2

    i = 1  # obroty
    while (abs(f_c) > E and warunekCauchyego(x_p, x_k, f_x)):
        print(i, ":")
        i = i + 1
        x = x_i(x_p, x_k, f_x)
        print("x_p =", x_p, "\nx_k =", x_k, "\nx_i =", x)
        f_c = f(x, f_x)
        print("f(x_p) =", f(x_p, f_x))
        print("f(x_k) =", f(x_k, f_x))
        print("f(x_i) =", f_c, "\n")

        if (warunekCauchyego(x_p, x, f_x)):
            x_k = x
        elif (warunekCauchyego(x, x_k, f_x)):
            x_p = x
        else:
            print("Koniec możliwości, żegnam")
