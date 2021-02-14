'''
O mesmo profesor do desafio anterior quer sortear a ordem de apresentacao de trabalho dos 
alunos. faca um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
'''
from random import shuffle
aluno1 = input('Digite o nome do primeiro aluno(a): ')
aluno2 = input('Digite o nome do segundo aluno(a): ')
aluno3 = input('Digite o nome do terceiro aluno(a): ')
aluno4 = input('Digite o nome do ultimo aluno(a): ')
ordem = [aluno1,aluno2,aluno3,aluno4]
shuffle(ordem)
print('{:=^30}'.format('Sorteados'))
print('A ordem de apresentacao sera >>> {}'.format(ordem))