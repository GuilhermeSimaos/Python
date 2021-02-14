'''
Crie um programa que leia o nome completo de uma pessoa e mostre:
O nome com todas as letras maiusculas
O nome com todas minusculas
Quantas letras ao todo(Sem considerar espacos)
Quantas letras tem o primeiro nome
'''
nome = input('Qual o seu nome? : ')
primeiroNome = nome.split()
nomeSemEspaco = nome.replace(' ','')
print('{:-^50}'.format('Resultados'))
print('Seu nome em letras MAIUSCULAS : {}\nSeu nome em letras minusculas : {}'.format(nome.upper(),nome.lower()))
print('Letras no seu nome completo : {}\nLetras no seu primeiro nome : {}'.format(len(nomeSemEspaco),len(primeiroNome[0])))
