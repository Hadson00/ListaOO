class ContaCorrente:
    def __init__(self, numconta, nome_correntista, saldo):
        self.numconta = numconta
        self.nome_correntista = nome_correntista
        self.saldo = saldo
    def alterarNome():
        self.nome_correntista = str(input('Digite um nome: '))

    def Depositar():
        deposito = float(input('Digite o valor a depositar: '))
        self.saldo += deposito

    def Sacar():
        saque = float(input('Digite o valor a sacar: '))
        self.saldo -= saque

corrent = ContaCorrente

    