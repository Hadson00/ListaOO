class Tamagotchi:
    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome 
        self.saude = saude 
        self.idade = idade 
    
    def __str__(self):
        return f'O nome do Tamagotchi é {self.nome}, 
        sua fome está em {self.fome}, está com {self.saude} de saúde e tem {self.idade} anos'
    
    def 