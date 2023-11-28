import json

class Conta:

    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__codigo_banco = "001"


    @property
    def saldo(self):
        return self.__saldo
   
    @property
    def titular(self):
        return self.__titular
    
    @property
    def limite(self):
        return self.__limite
    
    @property
    def numero(self):
        return self.__numero
    
    @staticmethod
    def codigo_banco():
        return "001"
    
    @staticmethod
    def codigos_bancos():
        caminho_arquivo_json = "banco_codigo.json"

        with open(caminho_arquivo_json, 'r') as arquivo:
            dados = json.load(arquivo)

        for dicionario in dados:
            print(dicionario)
    
    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    def extrato(self):
        print(f"Extrato: {self.__saldo} | Titular: {self.__titular}")

    def depositar(self, valor):
        self.__saldo += valor
    
    def __pode_sacar(self, valor):
        if (valor > 0):
            max_sacar = self.__saldo + self.__limite
            return valor <= max_sacar
        else:
            return False

    def sacar(self, valor):
        if (self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("Valor inválido")

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)
