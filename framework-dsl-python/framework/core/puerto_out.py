from .puerto import Puerto

class PuertoOUT(Puerto):
    def leerMensaje(self):
        return self.slot.leerMensaje()
