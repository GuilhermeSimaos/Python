'''Faca um programa que leia tres numero e mostre qual eh o maior e qual eh o menor.'''
n1 = int(input('\nDigite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O maior valor eh {}'.format(maior))
print('O menor valor eh {}'.format(menor))
# 13-02-2020 / simplificado e logica melhorada