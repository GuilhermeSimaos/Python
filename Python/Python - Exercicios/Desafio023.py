'''
Faca um programa que leia o numero de 0 a 9999 e mostre a tela cada um dos digitos separados
Ex: 
    digite um numero:1834
    unidade : 4
    dezena : 3
    centena 8
    milhar : 1
Tentar fazer matematicamente e utilizando manipulacao de texto
'''
#Matematicamente
from math import log,floor
numero = int(input('Digite um numero entre 0 a 9999: '))
uni = numero // 1 % 10                  
dez = numero // 10 % 10
cen = numero // 100 % 10
mil = numero // 1000 % 10
numeroT = str(numero)
print('{:=^30}\nNumero original : {}\nUnidade : {}\nDezena : {}\nCentena : {}\nMilhar : {}'.format('Matematicamente',numero,uni,floor(dez),floor(cen),mil))

#Manipulando o texto
print('{:=^30}\nNumero original : {}\nUnidade : {}\nDezena : {}\nCentena : {}\nMilhar : {}'.format('Manipulando Texto',numeroT,numeroT[3],numeroT[2],numeroT[1],numeroT[0]))

#logica da forma matematica atualizada