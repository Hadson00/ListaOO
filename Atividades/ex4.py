class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self._idade = idade
        self.__peso = peso
        self.altura = altura
    def Envelhecer(self)->None:
        self._idade += 1
        self.Crescer()
    def Engordar(self, grama:float)-> None:
        self.__peso += grama
    def Emagrecer(self, grama: float)-> None:
        self.__peso -= grama
    def Crescer(self)-> None:
        if self._idade < 21:
            self.altura += 0.05
        elif self._idade <50 and self._idade > 21:
            self._idade += 1
        else:
            self.altura -= 1
    def __str__(self):
        return f'Eu sou o {self.nome} tenho {self._idade} com {self.__peso}Kg e {self.altura}m'
    def peso(self)->float:
        return self.__peso
    
soneca = Pessoa('Lucas', 19, 50, 1.80)
print(soneca)
soneca.Envelhecer()
soneca.Engordar(20)
soneca.Emagrecer(50)
print(soneca)