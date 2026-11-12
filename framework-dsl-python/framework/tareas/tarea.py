from abc import ABC, abstractmethod

class Tarea(ABC):
    def __init__(self, entradas, salidas, tipo):
        self.listaEntradas = entradas
        self.listaSalidas = salidas
        self.tipo = tipo

    @abstractmethod
    def ejecutar(self):
        pass
