#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade
#de dias pelos quais ele foi alugado. Calcule o preco a pagar, sabendo que o carro custa R$60 por dia
#e R$0,15 por Km rodado.
k = float(input('Quantos kilometros foram andados? '))
d = int(input('Por quantos dias o carro foi alugado? '))
t = (k*0.15) + (d*60)
print('{:=^30}'.format('Boleto'))
print('Km percorridos : {}Km\nDias alugados : {} Dias\nTotal a pagar : R${:.2f}'.format(k,d,t))