from .tarea import Tarea

class ContextEnricher(Tarea):
    def ejecutar(self):
        # La regla para combinar los dos mensajes debe concretarse.
        raise NotImplementedError("Definir cómo se enriquece el mensaje")
