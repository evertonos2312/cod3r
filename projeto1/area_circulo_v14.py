from math import pi
import sys
import errno

ERRO = '\033[31m'
NORMAL = '\033[0m'


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
        print(f'{ERRO}O raio deve ser um valor numerico{NORMAL}')
        sys.exit(errno.EINVAL)

    raio = float(sys.argv[1])
    area = circulo()
    print(f'Area do circulo {area:.4f}')
