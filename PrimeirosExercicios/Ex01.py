class ContaCorrente():

    def __init__(self, pCodigo, pTitular, pSaldo, pLimite):
        self.codigo = pCodigo
        self.titular = pTitular
        self.saldo = pSaldo
        self.limite = pLimite

    def tranferir(self, valor, origem, destino):
        
        if valor > 0 and self.saldo >= valor:
            origem.saldo -= valor
            destino.saldo += valor
            print(f"Foi transferido: R${valor} de {origem.titular} para {destino.titular}")
            print(conta_01.titular, conta_01.saldo)
            print(conta_02.titular, conta_02.saldo)
    

conta_01 = ContaCorrente(1, "Matheus", 10000.0, 3000.0)
print(conta_01.titular, conta_01.saldo)
conta_02 = ContaCorrente(2, "Lucas", 2000.0, 1000.0)
print(conta_02.titular, conta_02.saldo)

conta_01.tranferir(1000.0, conta_01, conta_02)