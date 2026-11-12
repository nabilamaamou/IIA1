from framework.mocks.tarea_mock import TareaMock

class CreadorTareasMock:
    def crear(self, tipo, entradas, salidas, configuracion=None):
        return TareaMock(entradas, salidas, tipo)
