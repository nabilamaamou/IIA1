from abc import ABC, abstractmethod

class Conector(ABC):
    def __init__(self, puertos, configuracionConector=""):
        self.puertos = puertos
        self.configuracionConector = configuracionConector

    @abstractmethod
    def ejecutar(self):
        pass
