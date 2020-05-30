from math import pi
import sys


def circulo():
    return pi * raio ** 2


def ajuda():
    print('É necessário informar o raio do circulo')
    print(f'Sintaxe: {sys.argv[0]} <raio>')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        ajuda()
#        sys.exit(1)
    else:
        raio = float(sys.argv[1])
        area = circulo()
        print(f'Area do circulo {area:.4f}')
