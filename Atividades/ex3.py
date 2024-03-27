class Rectangle:
    def __init__(self, sideA:float, sideB:float):
        self.sideA = sideA
        self.sideB = sideB
    def changeSize(self, newA, newB):
        self.sideA = newA
        self.sideB = newB
    def ReturnValue(self):
        print (f'O valor da base é {self.sideA}cm')
        print (f'O valor da altura é {self.sideB}cm')
    def Area(self):
        area = self.sideA * self.sideB
        return area
    def Perimeter(self):
        perimeter = (self.sideA * 2) + (self.sideB * 2)
        print(f'O perimetro é {perimeter}')

rectangle = Rectangle(5, 6)

newA = float(input('Digite um valor para a base: '))
newB = float(input('Digite um valor para a altura: '))
rectangle.changeSize(newA, newB)
rectangle.ReturnValue()
rectangle.Area()
rectangle.Perimeter()
piso = rectangle.Area()

place = float(input('Digite o tamanho do local(em metros quadrados): '))
calc = place / piso
print(f'Precisa de {calc} pisos')