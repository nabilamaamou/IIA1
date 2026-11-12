from framework.core.conector import Conector

class ConectorBDMock(Conector):
    def __init__(self, puertos, respuestas=None, configuracionConector=""):
        super().__init__(puertos, configuracionConector)
        self.respuestas = respuestas or []
        self.numConsultas = 0

    def ejecutar(self):
        self.numConsultas += 1
        if not self.puertos:
            return
        for mensaje in self.respuestas:
            self.puertos[0].mensajeSlot(mensaje)

    def getNumConsultas(self):
        return self.numConsultas
