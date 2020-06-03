palavra = 'paralelepípedo'
for numero in palavra:
    print(numero, end=',')
print(f'\nFim')

aprovados = ['Rafaela', 'Pedro', 'Renato', 'Maria']
for nome in aprovados:
    print(nome)

for posicao, nome in enumerate(aprovados):
    print(f'{posicao + 1})', nome)

dias_semana = ('Domingo', 'Segunda', 'Terça',
               'Quarta', 'Quinta', 'Sexta', 'Sábado')
for dia in dias_semana:
    print(f'Hoje é dia {dia}')

for numero in {1, 2, 3, 4, 5, 6}:
    print(numero)
