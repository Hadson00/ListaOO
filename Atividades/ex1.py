class Bola:
    def __init__(self, cor:str, circunferencia:float, material:str):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self, nova_cor):
        self.cor = nova_cor
        return nova_cor

    def mostraCor(self):
        print(f'A cor da bola é {self.cor}')
    
    def __str__(self):
        return f'A cor da bola é {self.cor}, com {self.circunferencia}cm de circunferencia e feita de {self.material}'
bola = Bola('Vermelha', 10, 'plastico')


bola.trocaCor(str(input('Digte uma nova cor: ')))
bola.mostraCor()
print(bola)