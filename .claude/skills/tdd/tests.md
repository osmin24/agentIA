# Buenas Prácticas para Pruebas (Tests)

- Escribe pruebas en archivos separados con el prefijo `test_`, ej: `test_document_processor.py`.
- Usa `pytest`.
- Mantén las pruebas simples y enfocadas en una sola cosa.
- Usa `fixtures` de pytest para preparar el estado inicial (setup) de forma reutilizable.
