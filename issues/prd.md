## Problem Statement

El proyecto RAG Chatbot necesita varias mejoras estructurales y funcionales para asegurar su robustez. Por un lado, el chatbot actualmente responde exclusivamente con texto, lo que limita la accesibilidad. Por otro lado, la aplicación carece de validaciones de entrada seguras para los usuarios, no maneja correctamente caídas por límites de la API de terceros (Anthropic), no cuenta con pruebas en la gestión de sesiones y sufre de falta de visibilidad interna en producción por carecer de un sistema de logging estructurado.

## Solution

Se abordará una actualización integral que unificará cinco pilares de mejora:
1. **Text-to-Speech (TTS):** Implementación de voz mediante el motor local `piper-tts` con estrategia de "lazy loading" (carga diferida).
2. **Validación de Consultas:** Protección contra payloads gigantes limitando la entrada del usuario a 1000 caracteres (HTTP 400).
3. **Robustez de la API (Anthropic):** Intercepción de errores de Rate Limit (`429 Too Many Requests`) para enviar mensajes controlados al usuario en lugar de quebrar el servidor con errores 500.
4. **Visibilidad (Logging):** Reemplazar llamadas nativas a `print()` por el módulo estándar de `logging` en Python.
5. **Calidad de Código (TDD):** Implementación de la primera suite de pruebas unitarias dirigidas específicamente a `SessionManager`.

## User Stories

1. Como usuario, quiero hacer una pregunta al chatbot y ver la respuesta de texto inmediatamente, sin esperar a que el audio termine. (TTS)
2. Como usuario, quiero escuchar la respuesta generada por la IA con una voz natural, para interactuar de forma auditiva. (TTS)
3. Como sistema, necesito rechazar automáticamente con un código 400 las consultas mayores a 1000 caracteres, para proteger la base de datos vectorial y no exceder los límites de Anthropic. (Issue 01)
4. Como desarrollador, quiero contar con pruebas automatizadas para `SessionManager`, para garantizar que el historial se guarda y recupera sin fallos tras futuras modificaciones. (Issue 02)
5. Como usuario, si la IA de Anthropic está saturada, quiero recibir un aviso amigable ("Servicio experimentando alta demanda") en lugar de ver que la aplicación simplemente deja de funcionar. (Issue 03)
6. Como administrador de sistemas/DevOps, quiero visualizar logs estructurados (INFO, WARNING, ERROR) de las peticiones en el backend, para depurar ágilmente. (Issue 04)
7. Como administrador, quiero que el servidor borre periódicamente el caché de audios (`temp_audio/`) para no saturar el disco. (TTS)

## Implementation Decisions

- **TTS**: Descarga y ejecución de modelo ONNX de Piper (Español) en `backend/tts_service.py`. Encolamiento en segundo plano (`BackgroundTasks`).
- **Validación de Input**: Usar validación en los modelos Pydantic (`QueryRequest`) o comprobación explícita en el endpoint `/api/query`.
- **Manejo de API Externa**: Captura de `anthropic.RateLimitError` y `anthropic.APIConnectionError` en `ai_generator.py` retornando strings seguros en vez de lanzar excepciones no manejadas.
- **Logs**: Importar `logging` en `app.py`, configurar un nivel básico (`INFO`) e inyectarlo en los puntos críticos de la aplicación.
- **Tests**: Archivo `test_session_manager.py` usando `pytest` para verificar inicialización, persistencia e historiales inexistentes.

## Testing Decisions

- Test unitario: Enviar consulta de >1000 caracteres mediante `TestClient` (FastAPI) y afirmar un status code 400.
- Test unitario/Mocking: Usar `unittest.mock` sobre el cliente de Anthropic para forzar un `RateLimitError` y comprobar la salida gracefully controlada.
- Test de logs: Realizar peticiones simuladas y verificar la salida del logger (opcional mediante fixtures de pytest como `caplog`).

## Out of Scope

- Proveedores TTS Cloud (OpenAI, Google) o web sockets (streaming binario).
- Integración de sistemas de logs externos (Datadog, Kibana). El alcance se limita a log estándar de consola.
- Reintentos automáticos sofisticados (Exponential Backoff) con la API de Anthropic.

## Further Notes

- El documento ha sido unificado combinando el nuevo *Feature* (TTS) con la deuda técnica previa documentada en los issues (01 al 04). Todas las tareas están listas para su abordaje en paralelo o secuencia.
