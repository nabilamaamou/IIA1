class Mensaje:
    def __init__(self, cuerpo, id):
        self.cabecera = {"id": id, "id_correlacion": None,
                         "id_secuencia": None, "longitud": 0}
        self.cuerpo = cuerpo

    def getId(self):
        return self.cabecera["id"]

    def getIdCorrelacion(self):
        return self.cabecera["id_correlacion"]

    def getIdSecuencia(self):
        return self.cabecera["id_secuencia"]

    def getLongitud(self):
        return self.cabecera["longitud"]

    def getCuerpo(self):
        return self.cuerpo

    def setId(self, id):
        self.cabecera["id"] = id

    def setIdCorrelacion(self, id):
        self.cabecera["id_correlacion"] = id

    def setIdSecuencia(self, n):
        self.cabecera["id_secuencia"] = n

    def setLongitud(self, length):
        self.cabecera["longitud"] = length

    def setCuerpo(self, cuerpo):
        self.cuerpo = cuerpo
