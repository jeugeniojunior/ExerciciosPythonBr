class Retangulo:
    def __init__(self, comprimento, largura):
        self.largura = largura
        self.comprimento = comprimento

    def muda_altura(self, largura):
        self.largura = largura

    def muda_base(self, comprimento):
        self.comprimento = comprimento

    def area(self):
        return self.comprimento * self.largura

    def perimetro(self):
        return (self.comprimento * 2) + (self.largura * 2)


comprimento1 = float(input('Valor do comprimento: '))
largura1 = float(input('valor da largura: '))
retangulo1 = Retangulo(comprimento1, largura1)

print(f'O Total de rodapé é {retangulo1.perimetro()} metros')
print(f'O Total de piso é {retangulo1.area()} metros2')

