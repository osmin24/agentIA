## Parent PRD

`issues/prd.md`

## What to build

Reemplazar la implementación simulada (dummy) del endpoint de audio con un motor de síntesis de voz real usando `piper-tts`. 
Se debe crear un módulo profundo `tts_service.py` que encapsule la importación de `piper`, la descarga del modelo en español (`es_MX-ald-medium`) y la lógica para escribir el texto proporcionado por Claude en archivos físicos `.wav` en la carpeta `temp_audio/`.
El endpoint `/api/query` debe pasarle el texto a este servicio usando `BackgroundTasks` de FastAPI, de manera que la generación de audio ocurra en segundo plano sin bloquear la respuesta de texto. El endpoint `/api/audio/{id}` debe esperar a que el archivo esté listo y servirlo.

## Acceptance criteria

- [ ] Se crea el módulo `tts_service.py` ocultando la complejidad de la librería Piper.
- [ ] El servicio descarga el modelo automáticamente si no existe.
- [ ] Se generan verdaderos archivos `.wav` en el disco a partir del texto de la respuesta.
- [ ] El endpoint de audio sirve el archivo real generado de manera asíncrona.

## Blocked by

- Blocked by `issues/05-tts-tracer-bullet.md`

## User stories addressed

- User story 2
- User story 3
