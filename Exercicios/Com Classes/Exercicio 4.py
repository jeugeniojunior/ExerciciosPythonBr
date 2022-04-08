class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        if self.idade < 21:
            self.altura += 0.5
        self.idade += 1

junior = Pessoa('Junior',2 , 12 , 80)

for _ in range(22):
    junior.envelhecer()
    print(f'Idade de {junior.nome} é: {junior.idade} anos e sua altura é {junior.altura} cm')