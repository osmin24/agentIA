## Problem Statement

El chatbot actualmente responde exclusivamente con texto. Los usuarios necesitan una forma de consumir las respuestas de manera auditiva para mejorar la accesibilidad y permitir una interacción más fluida y natural con los materiales educativos, sin depender únicamente de la lectura en pantalla.

## Solution

Implementar un sistema de Text-to-Speech (TTS) integrado en el chatbot que genere un mensaje de voz por cada respuesta de la IA. El sistema utilizará un modelo local (Piper TTS) para evitar costos de API. Se usará una estrategia de carga diferida (lazy loading) donde el frontend recibe el texto inmediatamente junto con una URL de audio. El navegador solicitará la URL, y el backend generará o recuperará de caché el archivo de audio (.wav) para reproducirlo.

## User Stories

1. Como usuario, quiero hacer una pregunta al chatbot y ver la respuesta de texto inmediatamente, para no tener que esperar a que el audio termine de generarse.
2. Como usuario, quiero escuchar la respuesta generada por la IA con una voz natural, para poder comprender el material mientras hago otras cosas o descanso la vista.
3. Como administrador, quiero que el sistema de voz no genere costos recurrentes de API, utilizando modelos open source locales.
4. Como administrador, quiero que el servidor limpie automáticamente los archivos de audio antiguos generados, para que el disco duro no se llene.
5. Como usuario, quiero poder volver a reproducir un audio sin demora, gracias al sistema de caché temporal del backend.
6. Como desarrollador, quiero aislar la complejidad de la generación de voz en un servicio independiente, para que el archivo de rutas (app.py) se mantenga limpio y testeable.

## Implementation Decisions

- **Modelo TTS**: Se usará `piper-tts` con el modelo `es_MX-ald-medium` (Español de México).
- **Módulos**:
  - Se creará un módulo profundo en `backend/tts_service.py` que encapsulará la carga del modelo, la escritura en disco y la limpieza de archivos, exponiendo una interfaz muy sencilla.
- **Cambios en Interfaces**:
  - El modelo `QueryResponse` en `app.py` se modificará para incluir un campo opcional `audio_url`.
- **API Contracts**:
  - `POST /api/query`: Devolverá el JSON de siempre más `audio_url` (ej. `/api/audio/12345`).
  - `GET /api/audio/{audio_id}`: Devolverá el archivo binario de audio. Si no existe, esperará pasivamente (timeout de 30s) o retornará 404.
- **Interacciones Específicas**:
  - La generación de audio se encolará usando `BackgroundTasks` de FastAPI durante la llamada a `/api/query`.
- **UI**: El frontend (`script.js`) detectará `audio_url` e inyectará un `<audio controls autoplay>` en la burbuja del mensaje.

## Testing Decisions

- Un buen test debe probar que si un usuario realiza una consulta, eventualmente puede acceder al audio a través de la URL proporcionada, sin preocuparse de si se usa Piper, Coqui o una API en el fondo.
- Se escribirán tests de integración en `tests/` (si el entorno TDD los requiere) que:
  1. Hagan un `POST /api/query` mockeando el LLM.
  2. Verifiquen que la respuesta incluye un `audio_url`.
  3. Aseguren que el llamado a `GET` en ese `audio_url` retorna un archivo de audio válido tras la generación en segundo plano.

## Out of Scope

- Modelos de pago como OpenAI TTS o ElevenLabs.
- Transmisión por WebSockets en tiempo real (streaming directo de bits).
- Seleccionar voces dinámicamente desde el frontend.
- Historial persistente de audios de sesiones pasadas más allá de las 24 horas.

## Further Notes

- El modelo ONNX se descargará automáticamente la primera vez que arranque el servicio TTS. Esto puede causar un leve retraso en el primer inicio de la aplicación en un servidor limpio.
