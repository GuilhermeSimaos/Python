'''Desenvolva um programa que pergunte a distancia de uma viagem em Km. Calcule o preco da
passagem, cobrando R$0.50 por Km para viagens de ate 200Km e R$0.45 para viagens mais longas.'''
dis = float(input('\nQual a distancia a ser viajada? '))
if dis <= 200:
    pre = dis * 0.50
else:
    pre = dis * 0.45
print('{:-^30}\nPreco da passagem : R${}'.format('RESULTADO',pre))
print('Tenha uma boa viagem!\n')
