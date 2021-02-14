#crie um algoritmo que leia um numero e mostre seu dobro, triplo e raiz quadrada
n = int(input('Digite um numero qualquer: '))
d = n*2
t = n*3
r = n**2
print('\n{:=^20}'.format('Resultados'))
print('Dobro = {}\nTriplo = {}\nRaiz Quadrada = {}\n'.format(d,t,r))