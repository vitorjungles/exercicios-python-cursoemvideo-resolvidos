print('='*39)
print('Digite um número para ver seu fatorial.')
print('='*39)
num = int(input('Número escolhido: '))
f = 1
c = num
print(f'Calculando {num}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}')
