'''Faca um programa que leia um numero inteiro e mostre na tela seu sucessor e antecessor'''
print('{:=^50}'.format('Sucessor e Antecessor'))
n = int(input('Escreva um numero : '))
sucessor = n+1
antecessor = n-1
print('Sucessor : {}{}{}\t\t\tAntecessor : {}{}{}'.format('\033[32m',sucessor,'\033[m','\033[36m',antecessor,'\033[m'))
