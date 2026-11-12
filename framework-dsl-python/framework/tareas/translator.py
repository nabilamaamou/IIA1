from .tarea import Tarea

class Translator(Tarea):
    def __init__(self, entradas, salidas, tipo, rutaArchivoXSLT=""):
        super().__init__(entradas, salidas, tipo)
        self.rutaArchivoXSLT = rutaArchivoXSLT

    def ejecutar(self):
        raise NotImplementedError("Añadir la transformación XSLT")
