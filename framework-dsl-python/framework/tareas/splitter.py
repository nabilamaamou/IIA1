from .tarea import Tarea

class Splitter(Tarea):
    def __init__(self, entradas, salidas, tipo, xpath=""):
        super().__init__(entradas, salidas, tipo)
        self.xpath = xpath

    def ejecutar(self):
        # Comportamiento específico pendiente de definir en el diseño funcional.
        raise NotImplementedError("Definir la regla XPath del Splitter")
