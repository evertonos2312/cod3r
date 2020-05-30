from math import pi


def circulo():
    return pi * raio ** 2


if __name__ == '__main__':
    raio = float(input('Informe o raio: '))
    area = circulo()
    print(f'Area do circulo {area:.4f}')
