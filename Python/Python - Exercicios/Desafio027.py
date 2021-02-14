'''
Faca um programa que leia o nome completo de uma pessoa, mostrando em seguida 
o primeiro e ultimo nome separadamente.

EX: 
    Ana Maria de Souza
    primeiro = Ana
    Ultimo = Souza
'''
nome = str(input('Escreva seu nome completo : ')).strip()
n1 = nome.split()
print('Nome original : {}'.format(nome))
print('Primeiro nome : {}'.format(n1[0]))
print('Ultimo nome : {}'.format(n1[len(n1)-1]))
