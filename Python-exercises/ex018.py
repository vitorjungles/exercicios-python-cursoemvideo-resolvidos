from math import radians, sin, cos, tan
ang = float(input('Digite um ângulo qualquer: '))
print(f'Segue o valor do seno, cosseno e tangente para o ângulo de {ang}°.')
rad = radians(ang)
sen = sin(rad)
cos = cos(rad)
tan = tan(rad)
print('=' * 18)
print(f'O SENO é {sen:.2f}.\nO COSSENO é {cos:.2f}.\nA TANGENTE é {tan:.2f}.')
print('=' * 18)
