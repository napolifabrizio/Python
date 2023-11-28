
class Conta:

    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f"Extrato: {self.__saldo} | Titular: {self.__titular}")

    def depositar(self, valor):
        self.__saldo += valor
    
    def __pode_sacar(self, valor):
        if (valor > 0):
            max_sacar = self.__saldo + self.__limite
            return valor <= max_sacar

    def sacar(self, valor):
        if (self.__pode_sacar(valor)):
            self.__saldo -= valor

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)

    def get_saldo(self):
        return self.__saldo
    
    def get_titular(self):
        return self.__titular
    
    def get_limite(self):
        return self.__limite
    
    def get_numero(self):
        return self.__numero
    
    def set_limite(self, limite):
        self.__limite = limite
