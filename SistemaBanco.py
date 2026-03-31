from Cliente import Cliente
from Conta import Conta


class SistemaBanco:
    def __init__(self):
        self._conta = []

    def criar_conta(self):
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        numero = len(self._conta) + 1

        cliente = Cliente(nome, telefone)
        conta = Conta(cliente, numero)
        self._conta.append(conta)
        print("Conta criada com sucesso!")

    def encontrar_conta(self, numero):
        for conta in self._conta:
            if conta.numero == numero:
                return conta
        return None

    def listar_conta(self):
        print("\n----Contas----")
        for conta in self._conta:
            print(f"Numero: {conta.numero} | Cliente: {conta.cliente.get_nome()}")
    #MENU
    def operar(self):
        while True:
            print("\n 1 - Criar conta")
            print(" 2 - Depositar valor")
            print(" 3 - Sacar")
            print(" 4 - Extrato")
            print(" 5   Listar contas")
            print(" 0 - Sair")

            opcao = input("Escolha: ").strip()
            if opcao == "1":
                self.criar_conta()
            elif opcao in ["2", "3", "4"]:
                numero = int(input("Numero da Conta: "))
                conta = self.encontrar_conta(numero)
                if conta:
                    if opcao == "2":
                        valor = float(input("Valor: R$ "))
                        conta.deposita(valor)
                    elif opcao == "3":
                        valor = float(input("Valor: R$ "))
                        conta.saque(valor)
                    elif opcao == "4":
                        conta.extrato()
                    else:
                        print("Conta não encontrada!")

            elif opcao == "5":
                 self.listar_conta()

            elif opcao == "0":
                print("Saindo...")
                break

            else:
                print("Opção invalida!")
