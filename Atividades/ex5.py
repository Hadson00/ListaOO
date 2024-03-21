class ContaCorrente:
    def __init__(self, numconta, nome_correntista, saldo):
        self.numconta = numconta
        self.nome_correntista = nome_correntista
        self.saldo = saldo
    def alterarNome(self):
        self.nome_correntista = str(input('Digite um nome: '))

    def Depositar(self):
        deposito = float(input('Digite o valor a depositar: '))
        self.saldo += deposito

    def Sacar(self):
        saque = float(input('Digite o valor a sacar: '))
        self.saldo -= saque
    
    def __str__(self):
        return f'O número da conta é {self.numconta}, o nome do correntista é {self.nome_correntista}, seu saldo é de {self.saldo} reais'

corrent = ContaCorrente(1234, 'Hadson', 0)
corrent.alterarNome()
corrent.Depositar()
corrent.Sacar()
print(corrent)