class Televisao:
    def __init__(self, volume, canal):
        self.canal = canal
        self.volume = volume

    def novo_canal(self, canal_informado):
        if canal_informado > 30:
            print('Canal inválido')
        else:
            self.canal = canal_informado
            print(f'Canal: {self.canal}')

    def aumentar_volume(self):
        if (self.volume + 1) > 50:
            print('Volume já esta no limite')
        else:
            self.volume += 1
            print(f'Volume: {self.volume}')

    def diminuir_volume(self):
        if (self.volume - 1) < 0:
            self.volume = 0
            print('Volume = 0 ')
        else:
            self.volume -= 1
            print(f'Volume: {self.volume}')

tv = Televisao(25,5)

while True:
    print('Controle Remoto')
    print()
    print('Comandos: ')
    print('Volume: + ou -     Canal: C')
    print('Sair: S')

    operacao = input('Insira o comando desejado:').upper()

    if operacao == '+':
        tv.aumentar_volume()

    if operacao == '-':
        tv.diminuir_volume()

    if operacao == 'C':
        canal_informado = int(input('Digite o numero do Canal: '))
        tv.novo_canal(canal_informado)

    if operacao == 'S':
        break

    print()
    print()

