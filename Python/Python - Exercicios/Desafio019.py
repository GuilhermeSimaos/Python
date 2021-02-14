'''
Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faca um programa
que ajude ele, lendo o nome dele e escrevendo o nome escolhido
'''
from random import choice
aluno1 = input('Digite o nome do primeiro aluno(a): ')
aluno2 = input('Digite o nome do segundo aluno(a): ')
aluno3 = input('Digite o nome do terceiro aluno(a): ')
aluno4 = input('Digite o nome do ultimo aluno(a): ')
escolhido = [aluno1,aluno2,aluno3,aluno4]
print('\n{:-^40}'.format('Escolhido'))
print('O aluno(a) escolhido para apagar o quadro : {}'.format(choice(escolhido)))
