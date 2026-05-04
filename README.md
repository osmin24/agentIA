<div align="center">
  <h1>📚 Course Materials RAG System</h1>
  <p><strong>Un sistema avanzado de Búsqueda y Generación Aumentada (RAG) para consultar materiales de cursos usando inteligencia artificial.</strong></p>
</div>

---

## 📖 Descripción General

Esta aplicación es un sistema **RAG (Retrieval-Augmented Generation)** completo que permite a los usuarios hacer preguntas sobre materiales educativos y recibir respuestas inteligentes y contextualizadas. Combina búsqueda semántica avanzada con modelos generativos de IA para ofrecer respuestas precisas basadas en los documentos proporcionados.

El proyecto cuenta con una interfaz web limpia, una API robusta y ahora integra un **Flujo de Trabajo para Agentes Autónomos (AFK Agent)** que permite el desarrollo guiado por tareas.

## ✨ Características Principales

- **Respuestas Basadas en Contexto**: Utiliza Claude de Anthropic para generar respuestas usando estrictamente la información del curso.
- **Búsqueda Semántica**: Implementado con ChromaDB y Sentence-Transformers para recuperación eficiente de vectores de alta dimensión.
- **Arquitectura Full-Stack**:
  - **Backend**: FastAPI (Python) para alto rendimiento y documentación automática de APIs.
  - **Frontend**: Interfaz web responsiva construida con HTML, Vanilla JS y CSS.
- **Agentes Autónomos (AFK)**: Preparado para automatización de desarrollo mediante integración directa de prompts e instrucciones.

## 🛠️ Tecnologías Utilizadas

- **Python 3.13+** (con gestión de paquetes vía `uv`)
- **FastAPI** & **Uvicorn**
- **ChromaDB** (Almacenamiento Vectorial)
- **Anthropic Claude API** (LLM Generativo)
- **Sentence-Transformers** (Embeddings)

## 📋 Requisitos Previos

Antes de comenzar, asegúrate de tener lo siguiente:
- Python 3.13 o superior.
- [uv](https://github.com/astral-sh/uv) instalado (Gestor de paquetes de Python ultra rápido).
- Una clave API válida de **Anthropic** (Claude).
- *(Opcional)* **Git Bash** si usas Windows para ejecutar scripts `.sh`.

---

## 🚀 Instalación y Configuración

1. **Clonar el repositorio y entrar al directorio:**
   ```bash
   git clone <url-del-repositorio>
   cd starting-ragchatbot-codebase
   ```

2. **Instalar el gestor `uv` (Si no lo tienes):**
   ```bash
   # En macOS y Linux
   curl -LsSf https://astral.sh/uv/install.sh | sh
   # En Windows
   powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
   ```

3. **Instalar Dependencias de Python:**
   ```bash
   uv sync
   ```

4. **Configurar las Variables de Entorno:**
   Crea un archivo `.env` en la raíz del proyecto tomando como base el archivo `.env.example`:
   ```env
   ANTHROPIC_API_KEY=tu_clave_api_de_anthropic_aqui
   ```

---

## 💻 Uso de la Aplicación

### Opción 1: Inicio Rápido (Recomendado)
Puedes ejecutar el script de inicialización provisto:
```bash
# Otorgar permisos (Linux/macOS/Git Bash)
chmod +x run.sh
./run.sh
```

### Opción 2: Inicio Manual
Si prefieres inicializar el servidor manualmente:
```bash
cd backend
uv run uvicorn app:app --reload --port 8000
```

**Accesos:**
- 🌐 **Interfaz Web**: `http://localhost:8000`
- 📚 **Documentación de la API (Swagger UI)**: `http://localhost:8000/docs`

---

## 🤖 Flujo de Trabajo del Agente AFK

Este repositorio incluye infraestructura para que un agente de IA pueda trabajar en el código de forma semi-autónoma, siguiendo principios de TDD (Test-Driven Development).

1. **Crear una tarea**: Añade un archivo Markdown en la carpeta `issues/` describiendo la funcionalidad o el bug.
2. **Ejecutar el Agente**:
   - **En Windows**: `.\ralph\once.ps1`
   - **En macOS/Linux**: `./ralph/once.sh`
3. El agente leerá las instrucciones base (`ralph/prompt.md`), las buenas prácticas (`.claude/skills/tdd/`) e intentará resolver el issue.

---

## 🤝 Contribuciones

Si deseas contribuir:
1. Crea un archivo describiendo tu propuesta en la carpeta `issues/`.
2. Sigue las directrices de pruebas documentadas en `.claude/skills/tdd/`.
3. Asegúrate de ejecutar `pytest` y `mypy` antes de hacer tus commits.

---
*Desarrollado con ❤️ para transformar la interacción con el material educativo.*
