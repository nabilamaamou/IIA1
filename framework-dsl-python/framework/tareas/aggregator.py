from .tarea import Tarea

class Aggregator(Tarea):
    def __init__(self, entradas, salidas, tipo, raiz=""):
        super().__init__(entradas, salidas, tipo)
        self.raiz = raiz
        self.fragmentos = {}

    def ejecutar(self):
        # La condición que indica cuándo agregar está pendiente de especificar.
        raise NotImplementedError("Definir la condición de agregación")
