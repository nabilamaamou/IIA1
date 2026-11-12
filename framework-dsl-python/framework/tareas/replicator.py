from .tarea import Tarea

class Replicator(Tarea):
    def ejecutar(self):
        if not self.listaEntradas:
            return
        mensaje = self.listaEntradas[0].leerMensaje()
        if mensaje is not None:
            for slot in self.listaSalidas:
                slot.escribirMensaje(mensaje)
