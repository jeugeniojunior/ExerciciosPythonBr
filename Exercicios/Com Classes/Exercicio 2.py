class Quadrado:
    def __init__(self):
        self.tamanho = 10

    def muda_tamanho(self, tamanho):
        self.tamanho = tamanho

    def area(self):
        return (self.tamanho) *2


quadrado1 = Quadrado()
quadrado2 = Quadrado()

quadrado2.muda_tamanho(15)

print(quadrado1.area())
print(quadrado2.area())
