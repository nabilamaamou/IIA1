class Slot:
    def __init__(self):
        self.listaMensajes = []

    def leerMensaje(self):
        if self.estaVacio():
            return None
        return self.listaMensajes.pop(0)

    def escribirMensaje(self, mensaje):
        self.listaMensajes.append(mensaje)

    def getLongitudMensaje(self):
        return len(self.listaMensajes)

    def estaVacio(self):
        return len(self.listaMensajes) == 0

    def siguienteMensaje(self):
        if self.estaVacio():
            return None
        return self.listaMensajes[0]
