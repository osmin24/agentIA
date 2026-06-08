# Implementar logging estructurado en la API

**Prioridad**: Infraestructura
**Componente**: `backend/app.py`

## Descripción del Problema
Cuando el backend en FastAPI se está ejecutando, tenemos muy poca visibilidad de lo que ocurre internamente, excepto por la salida estándar de uvicorn. Si falla una inserción en la base de datos vectorial o si se completa una petición con éxito, deberíamos registrar estos eventos para que sean más fáciles de depurar en producción.

## Tarea Requerida
1. Configurar el módulo estándar `logging` de Python.
2. Reemplazar cualquier uso de `print()` que exista en el código por llamadas a `logger.info()`, `logger.warning()`, o `logger.error()`.
3. Asegurar que las consultas entrantes a los endpoints y los errores críticos queden registrados.

## Criterios de Aceptación (TDD)
- Crear una prueba básica verificando la configuración del log.
- Enviar peticiones simuladas (usando `TestClient` de FastAPI) y asegurar que el logger capta el evento de inicio y finalización del request.
- Integrar la configuración y probar que la app pasa `pytest` y `mypy` sin advertencias.
