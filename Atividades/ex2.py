class Square:
    def __init__(self, sizeside:float):
        self.sizeside = sizeside
    def changeSize(self):
        self.sizeside = float(input('Digite um valor para o lado: '))
    def __str__(self):
        return f'O valor do lado é {self.sizeside}cm'
    def Area(self):
        area = self.sizeside ** 2
        print(area)

square = Square(5)

square.changeSize()
square.Area()
print(square)