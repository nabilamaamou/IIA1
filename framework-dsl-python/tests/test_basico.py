import unittest
from framework.core import Slot, Mensaje, Tipo
from framework.tareas.tipo_tarea import TipoTarea
from framework.factories import CreadorTareas
from framework.mocks.slot_mock import SlotMock
from framework.mocks.tarea_mock import TareaMock

class FrameworkTest(unittest.TestCase):
    def test_slot(self):
        slot = Slot()
        mensaje = Mensaje("<x>1</x>", 1)
        slot.escribirMensaje(mensaje)
        self.assertIs(slot.leerMensaje(), mensaje)
        self.assertTrue(slot.estaVacio())

    def test_replicator(self):
        entrada, salida1, salida2 = Slot(), Slot(), Slot()
        mensaje = Mensaje("<x>1</x>", 1)
        entrada.escribirMensaje(mensaje)
        tarea = CreadorTareas().crear(
            TipoTarea.REPLICATOR, [entrada], [salida1, salida2],
            {"tipo": Tipo.TRANSFORMER}
        )
        tarea.ejecutar()
        self.assertIs(salida1.leerMensaje(), mensaje)
        self.assertIs(salida2.leerMensaje(), mensaje)

    def test_slot_mock(self):
        slot = SlotMock()
        slot.escribirMensaje(Mensaje("<x/>", 1))
        slot.leerMensaje()
        self.assertEqual(slot.getNumLecturas(), 1)
        self.assertEqual(len(slot.getEscritos()), 1)

    def test_tarea_mock(self):
        tarea = TareaMock()
        tarea.ejecutar()
        self.assertTrue(tarea.comprobarResultado())

if __name__ == "__main__":
    unittest.main()
