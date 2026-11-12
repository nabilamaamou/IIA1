from .tarea import Tarea

class Merger(Tarea):
    def ejecutar(self):
        for entrada in self.listaEntradas:
            mensaje = entrada.leerMensaje()
            if mensaje is not None and self.listaSalidas:
                self.listaSalidas[0].escribirMensaje(mensaje)
