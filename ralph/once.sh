#!/bin/bash
# Script para iniciar un ciclo del agente

# Leer los issues abiertos
ISSUES_DIR="issues"
ISSUES=$(ls $ISSUES_DIR/*.md 2>/dev/null || echo "No hay issues pendientes.")

# Leer los últimos commits
LAST_COMMITS=$(git log --oneline -5 2>/dev/null || echo "No hay commits recientes.")

# Cargar el prompt
PROMPT=$(cat ralph/prompt.md)

echo "Iniciando ciclo de agente..."
echo "============================="
echo "Issues encontrados:"
echo "$ISSUES"
echo "============================="

# Aquí en un entorno real, se pasaría esto a la API del LLM o a una herramienta como la CLI de Claude con --permission-mode acceptEdits
echo "Instrucciones enviadas al agente (Simulación)"
# claude --prompt "$PROMPT" --context "$ISSUES" --context "$LAST_COMMITS" --permission-mode acceptEdits
