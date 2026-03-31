class Conta:
    def __init__(self,cliente,numero):
        self._saldo = 0
        self._numero = numero
        self._cliente = cliente
        self._historico = []

    @property
    def saldo(self):
     return self._saldo

    @property
    def numero(self):
        return self._numero

    @saldo.setter
    def saldo(self,saldo):
            if (saldo < 0):
                print("O saldo não pode ser negativo")
            else:
                self._saldo = saldo

    @property
    def cliente(self):
        return self._cliente

    def saque(self,valor):
        if valor > self._saldo:
            print("Saldo insuficiente")
        elif valor <= 0:
          print("Valor invalido")
        else:
            self._saldo -= valor
            self._historico.append(f"Saque: -R$ {valor}")
            print("Saque realizado com sucesso")
    def deposita(self,valor):
        if valor <= 0:
            print("Valor invalido")
        else:
             self._saldo += valor
             self._historico.append(f"Deposito: +R$ {valor}")
             print("Deposito realizado com sucesso!")

    def extrato(self):
        print("\n ----Extrato----")
        print(f"Cliente: {self._cliente.get_nome()}")
        print(f"Conta: {self._numero}")
        print(f"Saldo: $ {self._saldo:.2f}")
        print("\nHistorico: ")
        for item in self._historico:
            print(item)




