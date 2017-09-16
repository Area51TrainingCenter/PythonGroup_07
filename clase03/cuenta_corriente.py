class CuentaCorriente:
    def __init__(self, *args, **kwargs):
        if args:
            self.saldo = args[0]
        if 'saldo' in kwargs:
            self.saldo = kwargs['saldo']

    def mostrar_saldo(self):
        print(self.saldo)

    def depositar(self, cantidad):
        self.saldo += cantidad

    def transferir(self, otra_cuenta, cantidad):
        self.saldo -= cantidad
        otra_cuenta.depositar(cantidad)


a_g = CuentaCorriente(999999999)
k_f = CuentaCorriente(saldo=34)

a_g.depositar(3456789)
a_g.mostrar_saldo()  # -> 1003456788
k_f.transferir(a_g, 33)
a_g.mostrar_saldo()  # -> 1003456821
k_f.mostrar_saldo()  # 1
