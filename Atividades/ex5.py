class ContaCorrente:
    def __init__(self, numconta, nome_correntista, saldo):
        self.numconta = numconta
        self.nome_correntista = nome_correntista
        self.saldo = saldo
    def alterarNome(self, nome):
        self.nome_correntista = nome
        return nome

    def Depositar(self, deposito):
        self.saldo += deposito

    def Sacar(self, saque):
        self.saldo -= saque
    
    def __str__(self):
        return f'O número da conta é {self.numconta}, o nome do correntista é {self.nome_correntista}, seu saldo é de {self.saldo} reais'

corrent = ContaCorrente(1234, 'Hadson', 0)
corrent.alterarNome(nome = str(input('Digite um nome: ')))
corrent.Depositar(deposito = float(input('Digite o valor a depositar: ')))
corrent.Sacar(saque = float(input('Digite o valor a sacar: ')))
print(corrent)