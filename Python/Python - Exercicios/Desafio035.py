'''Desenvolva um programa que leia o comprimento de tres retas e diga
ao usuario se elas podem ou nao formar um triangulo
Obs: para verificar se tres comprimentos formam um triangulo deve se fazer o seguinte. Somar
os dois menores comprimentos e verificar se eh maior ou igual que o maior lado'''
lado1 = int(input('\nDigite o comprimento da primeira reta: '))
lado2 = int(input('Digite o comprimento da segunda reta: '))
lado3 = int(input('Digite o comprimento da terceira reta: '))
if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print('Os comprimentos PODEM FORMAR um triangulo!')
else:
    print('Os segmento NAO PODEM FORMAR um triangulo!')
print('-='*30)