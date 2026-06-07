## Parent PRD

`issues/prd.md`

## What to build

Crear una bala trazadora (tracer bullet) vertical para la funcionalidad de Text-to-Speech. El objetivo de este issue es tener una ruta end-to-end funcionando sin la complejidad del modelo local real. 
En el backend, se debe modificar el endpoint `/api/query` para que devuelva una URL de audio "falsa" y un ID único. Se debe crear un nuevo endpoint `/api/audio/{id}` que simule un retraso y luego devuelva un archivo de audio estático o generado en blanco.
En el frontend, se debe procesar el `audio_url` de la respuesta y renderizar un reproductor HTML5 `<audio controls autoplay>` para que intente cargar y reproducir dicho archivo.

## Acceptance criteria

- [ ] El modelo `QueryResponse` incluye el campo opcional `audio_url`.
- [ ] Al hacer un POST a `/api/query`, la respuesta JSON incluye una URL hacia `/api/audio/{id}`.
- [ ] El endpoint GET `/api/audio/{id}` devuelve un archivo de audio válido (aunque sea estático o vacío) simulando una carga diferida.
- [ ] El frontend inyecta un reproductor `<audio>` debajo del mensaje cuando la IA responde.
- [ ] El reproductor intenta reproducir automáticamente el audio.

## Blocked by

None - can start immediately

## User stories addressed

- User story 1
- User story 6
