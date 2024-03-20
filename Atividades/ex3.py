class Rectangle:
    def __init__(self, sideA:float, sideB:float):
        self.sideA = sideA
        self.sideB = sideB
    def changeSize(self):
        self.sideA = float(input('Digite um valor para a base: '))
        self.sideB = float(input('Digite um valor para a altura: '))
    def __str__(self):
        return f'O valor da base é {self.sideA}cm'
        return f'O valor da altura é {self.sideB}cm'
    def Area(self):
        area = self.sideA * self.sideB
        print(f'A area é {area}cm²')
        return area
    def Perimeter(self):
        perimeter = (self.sideA * 2) + (self.sideB * 2)
        print(f'O perimetro é {perimeter}')

rectangle = Rectangle(5, 6)

rectangle.changeSize()
rectangle.Area()
rectangle.Perimeter()
piso = rectangle.Area()

place = float(input('Digite o tamanho do local(em metros quadrados): '))
calc = place / piso
print(f'Precisa de {calc} pisos')