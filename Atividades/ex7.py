class Tamagushi:
    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome 
        self.saude = saude 
        self.idade = idade 
    
    def AltStatus(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome 
        self.saude = saude 
        self.idade = idade

    def Mostrar(self):
        print(f'\nNome: {self.nome}')
        print(f'Fome: {self.fome}')
        print(f'Saúde: {self.saude}')
        print(f'Idade: {self.idade}')
        humor = self.fome + self.saude
        print(f'Humor: {humor}')
    
tamagotchi = Tamagushi('Hades',50, 30, 88)
nome = str(input('Digite o nome: '))
fome = int(input('Digite o nível de fome: '))
saude = int(input('Digite o nível de saúde: '))
idade = int(input('Digite a idade: '))
tamagotchi.AltStatus(nome, fome, saude, idade)
tamagotchi.Mostrar()