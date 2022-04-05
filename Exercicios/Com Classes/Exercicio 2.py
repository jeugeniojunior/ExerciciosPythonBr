class Quadrado:
    def __init__(self, tamanho = 4):
        self.tamanho = tamanho

    def muda_tamanho(self, tamanho):
        self.tamanho = tamanho

    def area(self):
        return (self.tamanho) ** 2


quadrado1 = Quadrado()
quadrado2 = Quadrado()

quadrado2.muda_tamanho(5)

print(quadrado1.area())
print(quadrado2.area())
