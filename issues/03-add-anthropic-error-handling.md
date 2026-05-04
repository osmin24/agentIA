# Manejo de errores para límites de tasa (Rate Limits) de Anthropic

**Prioridad**: Bugfix / Polish
**Componente**: `backend/ai_generator.py`

## Descripción del Problema
La integración con el modelo Claude mediante la librería de Anthropic puede fallar si excedemos el límite de peticiones (Rate Limit). Actualmente, si la API devuelve un error de tipo `429 Too Many Requests` o si se agota el tiempo de espera, la aplicación probablemente se quiebre (crash) devolviendo un error HTTP 500 generico y confuso para el usuario.

## Tarea Requerida
1. Modifica la llamada a la API de Anthropic en `backend/ai_generator.py` para capturar errores específicos de la API (por ejemplo `anthropic.RateLimitError` y `anthropic.APIConnectionError`).
2. Implementa un mecanismo de "reintento" (retry) simple o devuelve un error controlado hacia el frontend indicando: "El servicio está experimentado alta demanda, por favor intenta en unos segundos".

## Criterios de Aceptación (TDD)
- Escribir un test que haga un "mock" (usando `unittest.mock` o `pytest-mock`) de la API de Anthropic para simular un `RateLimitError`.
- Verificar que el sistema devuelve el mensaje controlado en lugar de hacer crash.
- Implementar la captura de excepciones con `try...except`.
- Verificar tipos con `mypy`.
