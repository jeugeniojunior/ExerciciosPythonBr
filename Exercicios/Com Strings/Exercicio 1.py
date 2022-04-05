s1 = input('Digite uma string: ')
s2 = input('Digite outra string: ')

tamanho1 = len(s1)
tamanho2 = len(s2)

print(f'{s1} = {tamanho1} caracteres')
print(f'{s2} = {tamanho2} caracteres')

comparacao_de_tamanhos = 'diferente'
comparacao_de_conteudos = 'diferente'


if s1 == s2:
    comparacao_de_tamanhos = 'iguais'
    comparacao_de_conteudos = 'iguas'
elif tamanho1 == tamanho2:
    comparacao_de_tamanhos = 'iguais'

print(f'AS duas strings são de tamanhos {comparacao_de_tamanhos}')
print(f'As duas strings possuem conteúdos {comparacao_de_conteudos}')
