'''
Faca um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente
desse angulo.
'''
from math import sin,cos,tan,radians
ang = float(input('Digite um angulo qualquer: '))
sen = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))
print('{:=^30}'.format('Resultado'))
print('Angulo Digitado : {}*\nSeno : {:.3f}\nCosseno : {:.3f}\nTangente : {:.3f}'.format(ang,sen,cos,tan))
