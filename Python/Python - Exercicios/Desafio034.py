'''Escreva um programa que pergunte o salario de um funcionario e calcule o valor do
seu aumento.
Para salarios superiores a R$1250.00, calcule um aumento de 10%.
Para inferiores ou iguais, o aumento eh de 15%.'''
salario = float(input('Qual o seu salario? R$'))
if salario >= 1250:
    salarioFinal = (salario*10)/100 + salario
else:
    salarioFinal = (salario*15)/100 + salario
print('-'*30)
print('Salario original : R${}'.format(salario))
print('Salario Reajustado : R${}\n'.format(salarioFinal))
