# Desarrollo Guiado por Pruebas (TDD) en Python

## Proceso
1. **Rojo (Red)**: Escribe una prueba (test) que defina la nueva funcionalidad o el bug. Ejecuta `pytest` y confirma que la prueba falla.
2. **Verde (Green)**: Escribe la cantidad MÍNIMA de código necesaria para que la prueba pase. Ejecuta `pytest` y confirma que la prueba pasa.
3. **Refactorizar (Refactor)**: Limpia el código, mejora la estructura, elimina redundancias, asegurándote de que `pytest` siga pasando y `mypy` no detecte errores de tipado.

Usa `/tdd` para iniciar este proceso cuando trabajes en un issue.
