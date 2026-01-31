## ⚙️ Запуск приложения

### 1. Поднять базу данных через Docker

```bash
docker-compose up -d

Создать и активировать виртуальное окружение

python3 -m venv .venv
source .venv/bin/activate   # macOS/Linux
# .venv\Scripts\activate    # Windows

Установить зависимости
pip install -r requirements.txt


Запуск FastAPI приложения
uvicorn app.main:app --reload

Проверка API
Swagger UI:
http://localhost:8000/docs