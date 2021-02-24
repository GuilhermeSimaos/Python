# Crie um algoritmo que leia um numero e mostre seu dobro, triplo e raiz quadrada
print('{}{:=^30}{}'.format('\033[1;33m','Calculadora','\033[m'))
numero = int(input('Digite um numero qualquer: '))
dobro = numero*2
triplo = numero*3
raizQ = numero**2
print('{}{:=^30}{}'.format('\033[1;33m','','\033[m'))
print('Dobro = {}\nTriplo = {}\nRaiz Quadrada = {}'.format(dobro,triplo,raizQ))
print('{}{:=^30}{}'.format('\033[1;33m','','\033[m\n'))