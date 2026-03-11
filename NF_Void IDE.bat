@echo off
chcp 65001 >nul
title NF_Void IDE

echo ============================================
echo   NF_Void IDE - Десктопная версия
echo ============================================
echo.

echo [1/3] Проверка Ollama...
where ollama >nul 2>nul
if %errorlevel% neq 0 (
    echo ❌ Ollama не найден!
    echo Установите: https://ollama.com/
    pause
    exit
)
echo ✅ Ollama найден

echo [2/3] Запуск Ollama сервера...
start "" ollama serve
timeout /t 3 /nobreak >nul
echo ✅ Ollama сервер запущен

echo [3/3] Запуск NF_Void IDE...
echo.

python desktop_app.py

pause