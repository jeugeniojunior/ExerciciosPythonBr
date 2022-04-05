def contar_caracteres(s):
    """Função que contas os caracteres de uma string

    ex:
    >>> contar_caracteres('renzo')
    {'r': 1, 'e': 1, 'n': 1, 'z': 1, 'o': 1}
    >>> contar_caracteres('banana')
    {'b': 1, 'a': 3, 'n': 2}

    :param s:string a ser contata

    """

    resultado = {}

    for caracter in s:
        resultado[caracter] = resultado.get(caracter, 0) + 1

    return resultado

if __name__ == '__main__':
    print(contar_caracteres('renzo'))
    print()
    print(contar_caracteres('banana'))


