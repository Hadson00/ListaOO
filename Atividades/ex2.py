class Square:
    def __init__(self, sizeside:float):
        self.sizeside = sizeside
    def changeSize(self, new_size):
        self.sizesize = new_size    
        return
    def __str__(self):
        return f'O valor do lado é {self.sizeside}cm'
    def Area(self):
        area = self.sizeside ** 2
        print(area)

square = Square(5)

square.changeSize(float(input('Digite um valor para o lado: ')))
square.Area()
print(square)