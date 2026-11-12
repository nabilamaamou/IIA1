from framework.tareas.tarea import Tarea

class TareaMock(Tarea):
    def __init__(self, entradas=None, salidas=None, tipo=None):
        super().__init__(entradas or [], salidas or [], tipo)
        self.numEjecuciones = 0

    def ejecutar(self):
        self.numEjecuciones += 1

    def comprobarResultado(self):
        return self.numEjecuciones > 0
