class Conta_corrente:
    def __init__(self, numero_da_conta: int, nome_do_correntista: str, saldo: float):
        self.saldo = saldo
        self.nome_do_correntista = nome_do_correntista
        self.numero_da_conta = numero_da_conta

    def alterar_nome(self, novo_nome_do_correntista):
        self.nome_do_correntista = novo_nome_do_correntista

    def deposito(self, valor_depositado):
        self.saldo += valor_depositado
        print(f' o saldo atual é {self.saldo}')

    def saque(self, valor_sacado):
        if valor_sacado <= self.saldo:
            self.saldo -= valor_sacado
            print(f' o saldo atual é {self.saldo}')
        else:
            print('Saldo insuficiente')

    def ver_saldo(self):
        print(f' O saldo atual é {self.saldo}')


conta = Conta_corrente(123456, 'José da Silva', 10000.00)

print('Banco do Povo')
print()
print('Caixa Eletrônico')
print('Operações:  SQ - saque    D - deposito     SD - saldo    AN - alterar nome')

operação = input('Digite qual a sua operação: ').upper()

if operação == 'AN':
    novo_nome_do_correntista = input('Digite o novo nome: ')
    conta.alterar_nome(novo_nome_do_correntista)
    print(f'Nome alterado para {novo_nome_do_correntista}')

if operação == 'SQ':

    valor_sacado = float(input('Qual o valor a ser sacado:'))
    conta.saque(valor_sacado)

if operação == 'SD':
    conta.ver_saldo()

if operação == 'D':
    valor_depositado = float(input('Qual o valor do depósito:'))
    conta.deposito(valor_depositado)






