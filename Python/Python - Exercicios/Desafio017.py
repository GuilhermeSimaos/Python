'''
Faca um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo,
calcule e mostre o comprimento da hipotenusa
'''
import math
catOposto = float(input('Forneca o comprimento do cateto oposto: '))
catAdjacente = float(input('Forneca o comprimento do cateto adjacente: '))
hipotenusa = math.hypot(catAdjacente,catOposto)
print('{:=^30}'.format('Resultado'))
print('Cateto Oposto: {}\nCateto Adjacente : {}\nHipotenusa : {}'.format(catOposto,catAdjacente,hipotenusa))