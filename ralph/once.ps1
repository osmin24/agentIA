# Script para iniciar un ciclo del agente en Windows PowerShell

$issuesDir = "issues"
$issues = Get-ChildItem -Path "$issuesDir\*.md" -ErrorAction SilentlyContinue | Select-Object -ExpandProperty Name

if (-not $issues) {
    $issues = "No hay issues pendientes."
}

$lastCommits = git log --oneline -5 2>$null
if ($LASTEXITCODE -ne 0) {
    $lastCommits = "No hay commits recientes."
}

$prompt = Get-Content -Path "ralph\prompt.md" -Raw

Write-Host "Iniciando ciclo de agente..."
Write-Host "============================="
Write-Host "Issues encontrados:"
Write-Host ($issues -join "`n")
Write-Host "============================="

# Aquí se invocaría la CLI del LLM
Write-Host "Instrucciones enviadas al agente (Simulación)"
# claude --prompt $prompt --context $issues --context $lastCommits --permission-mode acceptEdits
