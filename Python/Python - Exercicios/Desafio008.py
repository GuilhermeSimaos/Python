# Escreva um programa que leia um valor em metros e exiba convertido em centimetros e milimetros
print('{}{:~^50}{}'.format('\033[35m','Conversor de medidas','\033[m'))
metros = float(input('Digite um valor (em metros) para a conversao: '))
centimentros = metros * 100
milimetros = metros * 1000
kilometros = metros / 1000 #bonus
milhas = metros / 1609 #bonus
jardas = metros * 1.094 #bonus
pes = metros * 3.281 #bonus
print('{}{:~^50}{}'.format('\033[35m','Resultados','\033[m'))
print('Metros = {} m(s)\n\nCentimetros = {} cm(s)\nMilimetros = {} mm(s)'.format(metros,centimentros,milimetros))
print('Kilometros = {} km(s)\n\nMilhas = {:.3f} mile(s)\nJardas = {:.3f} yd(s)\nPes = {:.3f} ft(s)'.format(kilometros,milhas,jardas,pes))
print('{}{:~^50}{}'.format('\033[35m','','\033[m'))