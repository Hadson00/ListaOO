class Macaco:
    def __init__(self, nome, buchinxhei):
        self.nome = nome
        self.buchinxhei = buchinxhei

    def Comer(self, alimentos):
        self.buchinxhei = ''.join(alimentos)

    def verBucho(self):
        print(self.buchinxhei)

    def Digerir(self):
        self.buchinxhei = None

masqueico1 = Macaco('Raphael', None)

masqueico1.Comer(str(input('Digite o alimento: ')))
masqueico1.verBucho()