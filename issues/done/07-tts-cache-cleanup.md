## Parent PRD

`issues/prd.md`

## What to build

Implementar una estrategia de almacenamiento en caché y limpieza periódica para los archivos de audio temporales generados por el servicio TTS. 
Se debe agregar lógica al módulo `tts_service.py` para borrar los archivos en el directorio `temp_audio/` que tengan más de 24 horas de antigüedad. Esta rutina debe ser invocada por la aplicación, ya sea al inicio (startup event) o mediante una tarea programada o periódica para evitar el crecimiento infinito del almacenamiento en el servidor.

## Acceptance criteria

- [ ] `tts_service.py` expone un método de limpieza (`cleanup_old_files`).
- [ ] Los archivos `.wav` con una marca de tiempo mayor a 24 horas son borrados correctamente.
- [ ] La rutina se ejecuta automáticamente en el ciclo de vida de FastAPI (ej. `startup_event`).
- [ ] No se eliminan los audios recientes que podrían estar siendo solicitados por los usuarios.

## Blocked by

- Blocked by `issues/06-tts-piper-integration.md`

## User stories addressed

- User story 4
- User story 5
