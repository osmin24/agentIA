# Agregar tests unitarios para SessionManager

**Prioridad**: Infraestructura (Tests)
**Componente**: `backend/session_manager.py`

## Descripción del Problema
El archivo `backend/session_manager.py` es fundamental porque se encarga de guardar y recuperar el historial de mensajes de los usuarios. Sin embargo, no sabemos si se está comportando adecuadamente bajo distintas situaciones (por ejemplo, cuando se piden historiales de una sesión que no existe). Para seguir el enfoque de TDD, necesitamos tener pruebas sobre nuestros componentes core.

## Tarea Requerida
1. Crea un nuevo archivo de pruebas `backend/test_session_manager.py`.
2. Implementa pruebas para las funcionalidades clave de la clase `SessionManager`.

## Criterios de Aceptación (TDD)
- Test 1: Crear una sesión nueva y verificar que se inicie con el historial vacío (o sólo con el mensaje de sistema).
- Test 2: Agregar un mensaje de usuario y un mensaje de asistente, y verificar que ambos se guarden en el orden correcto.
- Test 3: Tratar de acceder a una sesión inexistente y verificar que devuelva un historial vacío o una nueva sesión correctamente inicializada.
- Asegurarse de que al correr `pytest` estos tests pasen sin errores.
- Comprobar que no haya errores de tipado con `mypy backend/`.
