from conta import Conta
from cliente import Cliente

conta_Fabrizio = Conta(123, "Fabrizio", 50000, 300000)
conta_Peter = Conta(456, "Fabrizio", 30000, 100000)

conta_Fabrizio.transferir(10000, conta_Peter)

conta_Fabrizio.extrato()
conta_Peter.extrato()

cliente_Fabrizio = Cliente("Fabrizio")
print(cliente_Fabrizio.nome)
cliente_Fabrizio.nome = "Fafa"
print(cliente_Fabrizio.nome)

conta_Fabrizio.pagamento_credito(500)