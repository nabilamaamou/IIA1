from .tarea import Tarea

class CorrelationIdSetter(Tarea):
    def __init__(self, entradas, salidas, tipo):
        super().__init__(entradas, salidas, tipo)
        self.mensajesEntrada = {}

    def relacionar(self, mensaje):
        clave = mensaje.getId()
        self.mensajesEntrada.setdefault(clave, []).append(mensaje)
        mensaje.setIdCorrelacion(clave)

    def ejecutar(self):
        for slot in self.listaEntradas:
            mensaje = slot.leerMensaje()
            if mensaje is not None:
                self.relacionar(mensaje)
                if self.listaSalidas:
                    self.listaSalidas[0].escribirMensaje(mensaje)
