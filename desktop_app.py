import webview
import threading
import time
import sys
import os
import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

# === FastAPI приложение ===
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def read_index():
    from fastapi.responses import FileResponse
    return FileResponse('static/index.html')


# === Запуск сервера в отдельном потоке ===
def run_server():
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="error")


# === Запуск десктопного приложения ===
def run_desktop():
    # Запускаем сервер в фоне
    server_thread = threading.Thread(target=run_server, daemon=True)
    server_thread.start()

    # Ждём пока сервер запустится
    time.sleep(2)

    # Создаём окно приложения
    window = webview.create_window(
        title='NF_Void IDE',
        url='http://127.0.0.1:8000',
        width=1400,
        height=900,
        min_size=(800, 600),
        resizable=True,
        fullscreen=False,
        text_select=True
    )

    # Запускаем приложение
    webview.start()


if __name__ == '__main__':
    print("=" * 60)
    print("🚀 NF_Void IDE - Десктопная версия")
    print("=" * 60)
    print()
    print("Запуск приложения...")
    print()
    run_desktop()