#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a media
n1 = int(input('Digite a primeira nota: '))
n2 = int(input('Digite a segunda nota: '))
m = (n1+n2)/2
print('\n{:=^30}'.format('Resultado da nota'))
print('Media do aluno = {}'.format(m))