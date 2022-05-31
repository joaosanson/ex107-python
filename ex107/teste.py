import moeda

p = float(input('Digite um preço: '))
print(f'A metade de {p} é {moeda.metade(p)}')
print(f'O dobro de {p} é {moeda.dobro(p)}')
print(f'Diminuindo 10% de {p}, temos {moeda.diminuir(p, 10)}')
print(f'Aumentando 10% de {p}, temos {moeda.aumentar(p, 10)}')
