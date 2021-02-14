#crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos
#Dolares ela pode comprar
print('{:-^40}'.format('Conversor Monetario'))
m = float(input('Quanto dinheiro voce possui na carteira? : R$'))
d = m*3.27
print('Eh possivel voce comprar ${:.2f} Dolares, (US$1,00 = R$3.27)\n'.format(d))