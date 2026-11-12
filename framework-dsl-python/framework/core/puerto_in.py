from .puerto import Puerto

class PuertoIN(Puerto):
    def mensajeSlot(self, mensaje):
        self.slot.escribirMensaje(mensaje)
