palavra = 'teamo'.upper()

print('Jogo da Forca')
print()
print('Descubra a palavra')
print()
print('A Palavra é: ', end='')

for letra in palavra:
    print(f'_ ', end='')

conjunto_letras_palavras = set(palavra)
conjunto_letras_digitadas = set()
erros = 0


while (not conjunto_letras_palavras.issubset(conjunto_letras_digitadas)) and erros < 7:
    print()
    print()
    letra_digitada = input('Digite uma letra: ').upper()
    conjunto_letras_digitadas.add(letra_digitada)
    if letra_digitada in conjunto_letras_palavras:
        print('A Palavra é: ', end='')
        for letra in palavra:
            if letra in conjunto_letras_digitadas:
                print(f'{letra} ', end='')
            else:
                print('_ ',end = '')
    else:
        erros += 1
        print(f'-> Erro {erros} de 6. Tente de novo!')

    print()
    print('Letras ja digitadas:', conjunto_letras_digitadas)

if erros <7:
    print('Parabéns!!! Você ganhou!')
else:
    print('Você perdeu!')






