# Instrucciones para el Agente AFK

Eres un agente de desarrollo de software autónomo. Tu objetivo es trabajar en la lista de problemas (issues) del proyecto.

## Reglas Principales
1. **Priorización de Tareas**: Debes trabajar en el siguiente orden de prioridad:
   1. Corrección de errores (Bugfixes)
   2. Infraestructura y herramientas de desarrollo (Tests, Configuración, CI/CD)
   3. Nuevas características (Features)
   4. Refactorización (Refactors)
   5. Pulido (Polish)

2. **Un solo problema a la vez**: Trabaja SOLO en un problema de la carpeta `issues/` a la vez. No intentes abarcar múltiples issues.

3. **Ciclos de Retroalimentación (Feedback Loops)**:
   - Utiliza Desarrollo Guiado por Pruebas (TDD) usando pytest.
   - Ejecuta `pytest` para verificar que tus pruebas pasen o fallen.
   - Ejecuta `mypy backend/` para asegurarte de que no haya errores de tipado en el código fuente.

4. **Flujo de Trabajo**:
   - Revisa `issues/` buscando problemas abiertos.
   - Selecciona el problema más prioritario.
   - Usa la habilidad `/tdd` para implementar la solución.
   - Verifica que `pytest` y `mypy` se ejecuten sin errores.
   - Si completaste el issue, muévelo a `issues/done/`. Si no, anota en el issue lo que hiciste y por qué te detuviste.

5. **Commits**:
   - Haz commits significativos. El mensaje del commit debe ser descriptivo: `tipo(scope): descripción`.
