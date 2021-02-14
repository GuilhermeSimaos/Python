#Escreva um programa que leia um valor em metros e exiba convertido em centimetros e
#milimetros
m = float(input('Digite o valor em metros: '))
c = m*100
mi = m*1000
print('\n{:=^20}'.format('Resultado'))
print('Metros = {}m\nCentimetros = {}cm\nMilimetros = {}mm\n'.format(m,c,mi))