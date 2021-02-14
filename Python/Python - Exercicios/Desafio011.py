#Faca um programa que leia a largura e altura de uma parede em metros, calcule a sua area
#e quantidade de tinta necessaria para pinta-la, sabendo que cada litro de tinta, pinta
#uma area de 2m^2.
a = float(input('Digite a altura da parede em metros: '))
l = float(input('Digite a largura da parede em metros: '))
ar = a*l
arp = ar/2
print('{:-^30}'.format('Resultados'))
print('Area da parede = {}m^2\nQuantidade de litros para pinta-la = {:.2f}L'.format(ar,arp))
