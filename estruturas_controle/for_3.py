produto = {'nome': 'Caneta Chic', 'preco': 14.99,
           'importada': True, 'estoque': 793}

for chave in produto:
    print(chave)
print()
for valor in produto.values():
    print(valor)
print()
for chave, valor in produto.items():
    print(chave, '=', valor)

