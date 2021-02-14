'''Crie um programa que leia um numero inteiro e mostre na tela se ele eh PAR ou IMPAR.'''
num = int(input('\nDigite um numero qualquer: '))
if num % 2 ==0:
    print('{:-^30}\nO numero {} eh PAR'.format('RESULTADO',num))
else:
    print('{:-^30}\nO numero {} eh IMPAR'.format('RESULTADO',num))
