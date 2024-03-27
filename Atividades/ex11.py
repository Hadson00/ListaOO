class Carro:

    def __init__(self, consumo, kilometragem, capacidade_tanque):
        self.__consumo = consumo                     
        self.__kilometragem = kilometragem           
        self.__capacidade_tanque = capacidade_tanque 
        self.__combustivel_no_tanque = 0             

    def __verifica_tanque(self, valor):
        if ((self.__combustivel_no_tanque + valor) <= self.__capacidade_tanque):
            return valor
        else:
            return (self.__capacidade_tanque - self.__combustivel_no_tanque)

    def abastecer(self, volume):
        abastecer = self.__verifica_tanque(volume)
        self.__combustivel_no_tanque += abastecer
        print("Tanque abastecido com {} litros de combustível. Seu tanque agora tem {} litros".format(abastecer, self.__combustivel_no_tanque))

    def __pode_andar(self, kilometragem):  
        consumo = (kilometragem / self.__consumo) 
        return (self.__capacidade_tanque >= consumo)

    def andar(self, km): 
        if (self.__pode_andar(km)):
            self.__kilometragem += km
            self.__combustivel_no_tanque -= (km / self.__consumo)
        else:
            print("Combustível insuficiente para andar {}Km".format(km))

    def tanque(self): 
        print("Restam {} litros no tanque de combustível".format(self.__combustivel_no_tanque))

    @property
    def consumo(self):
        return self.__consumo

    @property
    def capacidade_tanque(self):
        return self.__capacidade_tanque

    @property
    def kilometragem(self):
        return self.__kilometragem

    @property
    def combustiven_no_tanque(self):
        return self.__combustivel_no_tanque