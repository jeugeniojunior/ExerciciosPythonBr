nome = input('Digite seu nome: ').upper()
nome_ao_contrario = ''.join(reversed(nome))
nome_invertido = ' '.join(reversed(nome.split()))

print(f'Nome com letras em maiúsculo: {nome}')
print(f'Nome com letras em maiúsculo invertido por letras: {nome_ao_contrario}')
print(f'Nome com letras em maiúsculo invertido por palavras: {nome_invertido}')


