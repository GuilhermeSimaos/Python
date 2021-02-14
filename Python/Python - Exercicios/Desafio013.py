#Faca um algoritmo que leia o salario de um funcionario e mostre seu novo salario com
#15% de aumento
s = float(input('Digite o salario do funcionario: R$'))
reajuste = s + (s*15/100)
print('{:=^20}'.format('Reajuste'))
print('Salario Inicial : R${:.2f}\nSalario Final : R${:.2f}'.format(s,reajuste))