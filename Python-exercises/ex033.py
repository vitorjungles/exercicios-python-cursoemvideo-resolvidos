num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
num3 = int(input('Digite mais um número: '))
# Verificando quem é menor
menor = num1
if num2 < num1 and num3 < num1:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3
# Verificando quem é maior
maior = num1
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3
print('O menor valor digitado foi {}. '.format(menor))
print('O maior valor digitado foi {}. '.format(maior))
