from math import pi
import sys
import errno


def circulo():
    return pi * raio ** 2


def ajuda():
    print('É necessário informar o raio do circulo')
    print(f'Sintaxe: {sys.argv[0]} <raio>')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        ajuda()
        sys.exit(errno.EPERM)
    if not sys.argv[1].isnumeric():
        ajuda()
        print('O raio deve ser um valor numerico')
        sys.exit(errno.EINVAL)

    raio = float(sys.argv[1])
    area = circulo()
    print(f'Area do circulo {area:.4f}')
