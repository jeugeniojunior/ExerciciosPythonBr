class Bicho_virtual:
    def __init__(self, nome:str, fome:int, saude:int, idade:int):
        self.idade = idade
        self.saude = saude
        self.fome = fome
        self.nome = nome

    def dar_nome(self, novo_nome):
        self.nome = novo_nome
        print(f'O nome do seu bichino é {self.nome}')

    def alimentar_bem(self):
        self.fome += 2
        print(f'A fome do {self.nome} é {self.fome}')

    def alimentar_mal(self):
        self.fome += 1
        self.saude -= 1
        print(f'A fome do {self.nome} é {self.fome}')

    def dar_remedio(self):
        self.saude += 2
        print(f'A saúde do {self.nome} é {self.saude}')

    def exercicio(self):
        if self.fome < 3:
            self.saude -= 1
            self.fome -= 1
            print(f'A fome do {self.nome} é {self.fome} e a saude é {self.saude}')

        else:
            self.saude += 1
            self.fome -= 1
            print(f'A fome do {self.nome} é {self.fome} e a saude é {self.saude}')


    def humor(self):

        nivel_humor = (self.fome + self.saude) / 2

        if nivel_humor > 8:
            print(f'{self.nome} esta muito feliz')
            print(f'Nivel de Humor: {nivel_humor}')

        elif 5 <= nivel_humor < 8:
            print(f'{self.nome} esta feliz')
            print(f'NIvel de Humor: {nivel_humor}')

        elif 3 <= nivel_humor < 5:
            print(f'{self.nome} esta triste')
            print(f'Nivel de Humor: {nivel_humor}')

        elif nivel_humor < 3:
            print(f'{self.nome} esta muito triste')
            print(f'Nivel de Humor: {nivel_humor}')


    def morte(self):
        if self.fome <= 0:
            print(f'O {novo_nome} morreu!!')


        if self.saude <= 0:
            print(f'O {novo_nome} morreu!!')

    def esta_morto(self):
        return self.fome <= 0 or self.saude <= 0

    def esta_vivo(self):
        return self.fome > 0 and self.saude > 0


tamagushi = Bicho_virtual('nome', 3, 3, 2)

print('Bichinho Virtual')
print()
print('Você acaba de ganhar um bichinho virtual: ')
print()
novo_nome = input('Qual vai ser o nome dele:')
tamagushi.dar_nome(novo_nome)

while tamagushi.esta_vivo():
    print()
    print(f'O que vamos fazer com o {novo_nome}??')
    print(' Dar comida -> C ')
    print(' Dar remedio -> R ')
    print(' Fazer Exercicio -> E ')
    print(' Ver o Humor -> H ')

    operacao = input('Digite uma atividade:').upper()

    if operacao == 'C':
        print('Temos 2 tipode comida:')
        print('1 - Salada, frango grelhado e arroz integral')
        print('2 - Batata frita, cochinha e hangurguer')

        tipo_de_comida = input('Digite qual comida voce quer dar: ')

        if tipo_de_comida == 1:
            tamagushi.alimentar_bem()
            tamagushi.morte()
        else:
            tamagushi.alimentar_mal()
            tamagushi.morte()

    if operacao == 'R':
        tamagushi.dar_remedio()
        tamagushi.morte()

    if operacao == 'E':
        tamagushi.exercicio()
        tamagushi.morte()

    if operacao == 'H':
        tamagushi.humor()
        tamagushi.morte()



## atribuir morte





