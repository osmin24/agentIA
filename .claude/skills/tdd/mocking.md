# Mocking en Python

- Para aislar componentes, utiliza `unittest.mock.patch` o la librería `pytest-mock` (mocker fixture).
- Falsifica (mock) llamadas de red, accesos a base de datos o interacciones con APIs externas.
- Verifica no solo el resultado de retorno, sino también que las funciones falsificadas se hayan llamado con los argumentos correctos usando `mock_object.assert_called_with()`.
