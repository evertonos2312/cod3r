from math import pi

if __name__ == '__main__':
    raio = float(input('Informe o raio: '))
    print(f'Área do círculo {pi * raio ** 2:.4f}')

    print('Nome do módulo', __name__)
    print('Nome do pacote', __package__)
