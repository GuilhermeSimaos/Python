'''
Crie um programa que leia um numero real qualquer pelo teclado e mostre na tela
a sua porcao inteira
Ex: Digite um numero:6.127
o numero 6.127 tem a parte inteira 6
'''
import math
numero = float(input('Digite um numero qualquer: '))
print('{:=^20}'.format('Resultado'))
print('Numero digitado : {}\nNumero arredondado : {}'.format(numero,math.floor(numero)))