'''Faca um programa que leia um ano qualquer e mostre se ele eh bissexto.'''
from datetime import date
ano = int(input('{:-^30}\nDigite um ano qualquer: (coloque 0 para analisar ano atual) '.format("PADRAO")))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 ==0:
    print('O ano {} eh BISSEXTO!'.format(ano))
else:
    print('O ano {} NAO EH BISSEXTO!'.format(ano))
