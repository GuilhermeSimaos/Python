'''Escreva um programa que faca o computador "pensar" em um numero inteiro entre 0 e 5
e peca para o usuario tentar descobrir qual foi o numero escolhido pelo computador.'''
import random
num = int(input('{:-^30}\nEm qual numero estou pensando?(de 0 a 5) '.format('PADRAO')))
esc = random.randint(0,5)
if num == esc:
    print('{:-^30}\nVoce acertou o numero!'.format('VENCEU',esc))
else:
    print('{:-^30}\nEu pensei no numero {}'.format('PERDEU',esc))
print('Obrigado por brincar comigo.\n')
