class Macaco:
    def __init__(self, nome):
        self.nome = nome
        self.buchinxhei = []

    def Comer(self, alimentos):
        self.buchinxhei.append(alimentos)

    def verBucho(self):
        for i in self.buchinxhei:
            print(i)

    def Digerir(self):
        self.verBucho()
        self.buchinxhei = []

masqueico1 = Macaco('Raphael', None)

masqueico1.Comer(str(input('Digite o alimento: ')))
masqueico1.verBucho()
