# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a media
print('{}{:-^40}{}'.format('\033[32m','Media Escolar','\033[m'))
nota1 = int(input('Qual foi a primeira nota? '))
nota2 = int(input('Qual foi a segunda nota? '))
media = (nota1 + nota2)/2
print('{}{:-^40}{}'.format('\033[32m','Resultado da nota','\033[m'))
print('Media do aluno = {}'.format(media))
print('{}{:-^40}{}'.format('\033[32m','','\033[m\n'))
