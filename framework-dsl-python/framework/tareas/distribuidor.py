from .tarea import Tarea

class Distribuidor(Tarea):
    def __init__(self, entradas, salidas, tipo, listaXpath=None):
        super().__init__(entradas, salidas, tipo)
        self.listaXpath = listaXpath or []

    def ejecutar(self):
        raise NotImplementedError("Definir las reglas de distribución XPath")
