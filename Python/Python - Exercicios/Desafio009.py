#Faca um programa que leia um numero inteiro qualquer e mostre na tela a sua tabuada
from time import sleep
print('{}{:.^45}{}'.format('\033[34m','Tabuada Personalizada','\033[m'))
numero = int(input('Escolha um numero qualquer: '))
print('{}Gerando tabela...'.format('\033[36m'))
sleep(2)
print('{}{:.^45}{}'.format('\033[34m','Tabuada','\033[m'))
print('{} x 1 = {}   \t{} x 2 = {}   \t{} x 3 = {}'.format(numero,(numero*1),numero,(numero*2),numero,(numero*3)))
print('{} x 4 = {}   \t{} x 5 = {}   \t{} x 6 = {}'.format(numero,(numero*4),numero,(numero*5),numero,(numero*6)))
print('{} x 7 = {}   \t{} x 8 = {}   \t{} x 9 = {}\n{} x 10 = {}'.format(numero,(numero*7),numero,(numero*8),numero,(numero*9),numero,(numero*10)))
print('\033[34m...\033[m'*15)
