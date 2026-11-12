from .puerto import Puerto

class PuertoSOL(Puerto):
    def __init__(self, entrada, salida):
        super().__init__(entrada)
        self.slotOUT = salida

    def mensajeSlot(self, mensaje):
        self.slot.escribirMensaje(mensaje)

    def leerMensaje(self):
        return self.slotOUT.leerMensaje()

    def getSlotIN(self):
        return self.slot

    def getSlotOUT(self):
        return self.slotOUT
