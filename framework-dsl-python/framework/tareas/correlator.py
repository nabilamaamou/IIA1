from .tarea import Tarea

class Correlator(Tarea):
    def __init__(self, entradas, salidas, tipo, xpath=""):
        super().__init__(entradas, salidas, tipo)
        self.xpath = xpath
        self.mensajesEntrada = {}

    def relacionar(self, mensaje):
        clave = mensaje.getIdCorrelacion()
        self.mensajesEntrada.setdefault(clave, []).append(mensaje)

    def ejecutar(self):
        for slot in self.listaEntradas:
            mensaje = slot.leerMensaje()
            if mensaje is not None:
                self.relacionar(mensaje)
