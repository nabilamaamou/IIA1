from framework.tareas.tipo_tarea import TipoTarea
from framework.tareas import (Splitter, Distribuidor, Replicator, Translator,
    Correlator, CorrelationIdSetter, ContextEnricher, Merger, Aggregator)

class CreadorTareas:
    def crear(self, tipo, entradas, salidas, configuracion=None):
        configuracion = configuracion or {}
        clases = {
            TipoTarea.SPLITTER: Splitter,
            TipoTarea.DISTRIBUIDOR: Distribuidor,
            TipoTarea.REPLICATOR: Replicator,
            TipoTarea.TRANSLATOR: Translator,
            TipoTarea.CORRELATOR: Correlator,
            TipoTarea.CORRELATION_ID_SETTER: CorrelationIdSetter,
            TipoTarea.CONTEXT_ENRICHER: ContextEnricher,
            TipoTarea.MERGER: Merger,
            TipoTarea.AGGREGATOR: Aggregator,
        }
        if tipo not in clases:
            raise ValueError("Tipo de tarea no válido")

        clase = clases[tipo]
        if clase is Splitter:
            return clase(entradas, salidas, configuracion.get("tipo"), configuracion.get("xpath", ""))
        if clase is Distribuidor:
            return clase(entradas, salidas, configuracion.get("tipo"), configuracion.get("listaXpath", []))
        if clase is Translator:
            return clase(entradas, salidas, configuracion.get("tipo"), configuracion.get("rutaArchivoXSLT", ""))
        if clase is Correlator:
            return clase(entradas, salidas, configuracion.get("tipo"), configuracion.get("xpath", ""))
        if clase is Aggregator:
            return clase(entradas, salidas, configuracion.get("tipo"), configuracion.get("raiz", ""))
        return clase(entradas, salidas, configuracion.get("tipo"))
