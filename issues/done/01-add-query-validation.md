# Validar la longitud de la consulta del usuario

**Prioridad**: Feature / Polish
**Componente**: `backend/app.py` o `backend/models.py`

## Descripción del Problema
Actualmente, el sistema acepta consultas (`queries`) de cualquier longitud por parte del usuario. Si un usuario envía un texto extremadamente largo, podría causar varios problemas:
1. Superar el límite de tokens de la API de Anthropic, lo cual lanzará una excepción.
2. Afectar el rendimiento de la búsqueda semántica en la base de datos vectorial (ChromaDB).

## Tarea Requerida
1. Agrega validación para asegurarte de que el mensaje del usuario no exceda los 1000 caracteres antes de procesarlo.
2. Si el texto es muy largo, la API (FastAPI) debe devolver un código de error `400 Bad Request` con un mensaje amigable indicando que la consulta es demasiado larga.
3. Utiliza la validación integrada de Pydantic en los modelos (`backend/models.py`) si es posible.

## Criterios de Aceptación (TDD)
- Escribir un test (`pytest`) que envíe un mensaje mayor a 1000 caracteres y confirme que se recibe un error 400.
- Escribir un test que envíe un mensaje válido (ej. 50 caracteres) y confirme que se procesa correctamente.
- Implementar el código mínimo para que ambas pruebas pasen.
- Ejecutar `mypy` para comprobar los tipos.
