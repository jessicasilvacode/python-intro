
class Conta:

# __x__ = função que constroi o objeto
# usar métodos pra encapsular os objetos e restringir acesso aos atributos e mante-los privados usando __x

    def __init__(self, numero, titular, saldo, limite):
        print('Construindo objeto ...{}'.format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print('Saldo de {} reais do titular {}.'.format(self.__saldo, self.__titular))

    def depositar(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel
    
    def sacar(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print('O valor {} passou o limite da conta.'.format(valor))

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigos_bancos():
        return {'Banco do Brasil': '001', 'Caixa Econômica': '104', 'Bradesco': '237', 'Nubank': '260', 'Santander': '033'}


# no Python Console:
# from conta import Conta
# conta = Conta(numero, titular, saldo, limite)