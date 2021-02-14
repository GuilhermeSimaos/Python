#Faca um algoritmo que leia o preco de um produto e mostre seu novo preco,
#com 5% de desconto
p = float(input('Digite o preco do produto: R$'))
des = p - ((p*5)/100)
print('{:=^50}'.format('Desconto'))
print('Preco do produto com desconto de 5% = R${:.2f}'.format(des))