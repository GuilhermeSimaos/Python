'''Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Kn/h, mostre uma mensagem dizendo que ele foi multado
A multa vai custar R$7,00 por cada Km acima do limite'''

vel = int(input('\nQual foi a velocidade registrada? '))
if vel >= 80.0:
    multa = (vel - 80) * 7
    print('{:-^50}\nMultado por excesso de velocidade!'.format('MULTADO'))
    print('Multa : R${}\n'.format(multa))
else:
    print('{:-^50}\nDirigiu dentro do limite, Parabens!'.format('SIGA EM FRENTE'))
