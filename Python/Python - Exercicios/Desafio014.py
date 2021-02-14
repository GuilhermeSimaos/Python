#Escreva um programa que converta uma temperatura digitada em celsius e converta para Farenheit
t = float(input('Digite a temperatura em celsius: '))
f = (t*9/5) + 32
print('{:=^50}'.format('Conversor de Temperatura'))
print('Celsius -> {}\nFarenheit -> {}'.format(t,f))