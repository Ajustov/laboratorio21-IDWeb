import math

class Figura:
    def area(self):
        pass

    def perimetro(self):
        pass


class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)


class Triangulo(Figura):
    def __init__(self, lado):
        self.lado = lado

    def area(self):

        return (math.sqrt(3) / 4) * self.lado ** 2

    def perimetro(self):
        return 3 * self.lado

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2

    def perimetro(self):
        return 2 * math.pi * self.radio

figuras = [
    Rectangulo(4, 5),
    Triangulo(6),
    Circulo(3)
]

for f in figuras:
    print("Figura:", f.__class__.__name__)
    print("Área:", round(f.area(), 2))
    print("Perímetro:", round(f.perimetro(), 2))
    print("-" * 20)

