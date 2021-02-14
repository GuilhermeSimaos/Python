'''
Faca um programa que leia uma frase pelo teclado e mostre:

Quantas vezes aparece a letra "A"
Em que posicao ela aparece a primeira vez
Em que posicao ela aparece a ultima vez
'''
palavra = input('Digite uma palavra ou frase qualquer : ').strip().lower()
print('{:=^40}\nA letra [A] aparece {} vez(es)'.format('Resultados',palavra.count('a')))
print('Primeira posicao da letra A : {}'.format(palavra.find('a')+1))
print('Posicao em que aparece por ultimo : {}'.format(palavra.rfind('a')+1))