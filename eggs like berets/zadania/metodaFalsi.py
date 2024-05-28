#f(x) = sin(x) - 1/2x - funkcja

import math

def f(x) :
    return 3*x - math.cos(x) - 1


def x_i (x_p, x_k) :
    x = x_p - (f(x_p) * (x_k - x_p)/(f(x_k)-f(x_p)))
    return x


def warunekCauchyego(x_p, x_k) :
    return True if f(x_p)*f(x_k) < 0 else False


if __name__ == '__main__':
    E = 0.00001
    f_c = 1 #losowa wartość większa od E
    x_p = 0.25
    x_k = 0.75

    i=1 #obroty
    while(abs(f_c) > E and warunekCauchyego(x_p, x_k)) :
        print(i,":")
        i=i+1
        x = x_i(x_p, x_k)
        print("x_p =",x_p,"\nx_k =",x_k,"\nx_i =", x)
        f_c = f(x)
        print("f(x_p) =", f(x_p))
        print("f(x_k) =", f(x_k))
        print("f(x_i) =", f_c,"\n")

        if(warunekCauchyego(x_p, x)) :
            x_k = x
        elif (warunekCauchyego(x, x_k)):
            x_p = x
        else : print("Koniec możliwości, żegnam")


