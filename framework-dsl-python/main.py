from framework.core import Slot, Mensaje, Tipo
from framework.tareas.tipo_tarea import TipoTarea
from framework.factories import CreadorTareas

if __name__ == "__main__":
    entrada = Slot()
    salida1 = Slot()
    salida2 = Slot()

    entrada.escribirMensaje(Mensaje("<dato>Hola</dato>", 1))

    creador = CreadorTareas()
    tarea = creador.crear(
        TipoTarea.REPLICATOR,
        [entrada],
        [salida1, salida2],
        {"tipo": Tipo.TRANSFORMER}
    )
    tarea.ejecutar()

    print("Mensaje en salida 1:", salida1.getLongitudMensaje())
    print("Mensaje en salida 2:", salida2.getLongitudMensaje())
