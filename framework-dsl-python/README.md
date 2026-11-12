# Framework DSL en Python

Implementación mínima de la estructura del diagrama UML.

## Requisitos
- Python 3.10 o superior.
- No necesita instalar paquetes externos.

## Ejecutar el ejemplo
```bash
python main.py
```

## Ejecutar las pruebas
```bash
python -m unittest discover -s tests -v
```

## Estructura
- `framework/core`: mensajes, slots, puertos, conectores y enumeración `Tipo`.
- `framework/tareas`: clase base, nueve tareas y enumeración `TipoTarea`.
- `framework/factories`: fábrica de tareas.
- `framework/mocks`: dobles de prueba.
- `tests`: pruebas básicas.

## Nota sobre el alcance
Esta es una implementación mínima de la estructura y de las relaciones del diagrama.
Las operaciones cuyo algoritmo no está definido en el diagrama (`Splitter`,
`Distribuidor`, `Translator`, `ContextEnricher` y `Aggregator`) lanzan
`NotImplementedError` hasta que se especifiquen sus reglas. No se inventa
un comportamiento funcional que el UML no describe.
