class Reloj:
    def __init__(self, horas=0, minutos=0):
        self.horas = horas
        self.minutos = minutos

    def mostrar_hora(self):
        print('{:02}:{:02}'.format(self.horas, self.minutos))

    def agregar_minuto(self):
        self.minutos += 1
        if self.minutos > 59:
            self.agregar_hora()
            self.minutos = 0

    def agregar_hora(self):
        self.horas += 1
        if self.horas > 23:
            self.horas = 0

rolex = Reloj(horas=23, minutos=59)
rolex.mostrar_hora()
rolex.agregar_hora()
rolex.mostrar_hora()
rolex.agregar_minuto()
rolex.mostrar_hora()
