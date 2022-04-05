
lista_de_dados = []

def transformar_em_mb(tamanho_em_bytes:str) -> float:
    return int(tamanho_em_bytes) / (2**10) **2


with open('c:/curso/usuarios.txt', 'r') as arquivo:
    for linha in arquivo:
        linha = linha.strip()
        usuario = linha[:15]
        tamanho_em_disco = transformar_em_mb(linha[16:])

        lista_de_dados.append((usuario, tamanho_em_disco))

cabecalho = '''ACME Inc.               Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.    Usuário              Espaço utilizado     % do uso
'''

with open('c:/curso/relatorio.txt', 'w') as arquivo:
    tamanho_total_consumido = sum([tamanho for _,tamanho in lista_de_dados])
    media = tamanho_total_consumido / len(lista_de_dados)
    arquivo.writelines(cabecalho)
    for indice, dados in enumerate(lista_de_dados, start=1):
        usuario, tamanho_em_disco = dados
        arquivo.writelines(f'{indice:<4}    {usuario}        {tamanho_em_disco:9.2f} MB        '
        f'{tamanho_em_disco / tamanho_total_consumido:>6.2%}\n')

    arquivo.writelines('\n')
    arquivo.writelines('\n')
    arquivo.writelines(f'Tamanho total consumido: {tamanho_em_disco:.2f} MB')
    arquivo.writelines('\n')
    arquivo.writelines(f'Tamanho medio consumido: {media:.2f} MB')