'''
Crie um programa que leia o nome de uma cidade e diga se ela comecao ou nao com o nome "SANTO"
'''
cidade = input('Digite o nome da sua cidade : ').strip()
print('Nome da cidade comeca com santo? {}'.format(cidade[:5].lower() == 'santo'))
