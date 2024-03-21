class TV:
    def __init__(self, numcanal, volume):
        self.numcanal = numcanal
        self.volume = volume
    def AlterarCanal(self):
        self.numcanal = str(input('Digite o número do canal: '))
    def AlterarVolume(self):
        