# faca um programa que leia um numero inteiro e mostre na tela seu sucessor e antecessor
n = int(input('Escreva um numero : '))
sucessor = n+1
antecessor = n-1
print('{:=^20}'.format('Resultados'))
print('Sucessor : {}\nAntecessor : {}'.format(sucessor,antecessor))
