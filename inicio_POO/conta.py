

class Conta:

    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print(f"Extrato: {self.saldo} | Titular: {self.titular}")

    def depositar(self, valor):
        self.saldo += valor
    
    def sacar(self, valor):
        self.saldo -= valor