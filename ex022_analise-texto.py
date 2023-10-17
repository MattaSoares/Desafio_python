# Desafio 022 - Analisador de textos
# Crie um progrma que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao todo sem considerar espaços.
# - Quantas letras tem o primeiro nome

nome = str(input('Digite o seu nome completo: ')).strip()
nome_lista = nome.split()
print('Analisando o seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome é {} e ele tem {} letras'.format(nome_lista[0], len(nome_lista[0])))
