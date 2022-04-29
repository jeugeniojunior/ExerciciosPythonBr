class BombaCombustivel:
    def __init__(self, tipo_combustivel: str, valor_litro: float, qtd_combustivel: float):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.qtd_combustivel = qtd_combustivel

    def abastecer_por_valor(self, valor: float):
        litros_abastecidos = valor / self.valor_litro
        self._apresentar_abastecimento_se_possivel(litros_abastecidos, valor)

    def _apresentar_abastecimento_se_possivel(self, litros_abastecidos:float, valor:float):
        if litros_abastecidos > self.qtd_combustivel:
            print(f'Não pe possível abastecer, faltam {litros_abastecidos - self.qtd_combustivel:.2f} litros.')
            print('Reabasteça a bomba')
        else:
            self.qtd_combustivel -= litros_abastecidos
            print(f'Foram abastecidos {litros_abastecidos:.2f} litros a um valor de R$ {valor:.2f}')
            print(f'Sobraram na bomba {self.qtd_combustivel:.2f} litros.')

    def abastecer_por_litros(self, litros_abastecidos: float):
        valor = litros_abastecidos * self.valor_litro
        self._apresentar_abastecimento_se_possivel(litros_abastecidos, valor)

    def adicionar_combustivel(self,litros_adicionados:float):
        if litros_adicionados >= 0:
            self.qtd_combustivel += litros_adicionados
            print(f'A bomba agora contém: {self.qtd_combustivel} litros')
        else:
            print('Sai pra lá ladrão')

while True:

    operacao = input('Qual operação você deseja fazer (A)-Abartecer   (R)-Reabastecer bomba  (S)-Sair: ').upper()

    if operacao == 'R':
        tipo = input('Tipo de combustivel ( G - gasolina, A - alcool): ').upper()
        if tipo == 'G':
            bomba = BombaCombustivel('gasolina', 4.59, 100.0)
            litros_adicionados = float(input('Quantidade a ser colocada na bomba: '))
            bomba.adicionar_combustivel(litros_adicionados)

        elif tipo == 'A':
            bomba = BombaCombustivel('alcool', 2.00, 50.0)
            litros_adicionados = float(input('Quantidade a ser colocada na bomba: '))
            bomba.adicionar_combustivel(litros_adicionados)


    else:
        tipo = input('Tipo de combustivel ( G - gasolina, A - alcool: ').upper()
        if tipo == 'G':
           bomba = BombaCombustivel('gasolina', 4.59, 100.0)
        elif tipo == 'A':
            bomba = BombaCombustivel('alcool', 2.00, 50.0)

        condicao_abastecimento = input('Condição de abastecimento (D - dinheiro ou L - litros: ').upper()

        if condicao_abastecimento == 'D':
            valor_gasto = float(input('Digite o valor: '))
            bomba.abastecer_por_valor (valor_gasto)
        elif condicao_abastecimento == 'L':
            qtd_desejada = float(input('Digite a quantidade: '))
            bomba.abastecer_por_litros (qtd_desejada)

    if operacao == 'S':
        break




