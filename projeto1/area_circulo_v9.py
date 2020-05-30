from math import pi
import sys


def circulo():
    return pi * raio ** 2


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('É necessário informar o raio do circulo')
        print('Sintaxe: area_circulo <raio>')
    else:
        raio = float(sys.argv[1])
        area = circulo()
        print(f'Area do circulo {area:.4f}')
