# MilReg API

REST API для управления кадровыми данными (сотрудники, подразделения, штатное расписание, документы и т.д.) с использованием **FastAPI**, **SQLAlchemy** (асинхронный режим) и **PostgreSQL**.

## Стек технологий

- Python 3.10+
- FastAPI
- SQLAlchemy 2.0 (asyncpg)
- Pydantic 2.x
- PostgreSQL 14+

---

## 🚀 Быстрый старт

### 1. Клонирование репозитория

```bash
git clone <url-репозитория>
cd <папка-проекта>
```

2. Создание и активация виртуального окружения
Windows (CMD/PowerShell):

```bash
python -m venv venv
venv\Scripts\activate
```
Linux / macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```
3. Установка зависимостей
```bash
pip install --upgrade pip
pip install -r requirements.txt
```
4. Настройка базы данных PostgreSQL
Убедитесь, что PostgreSQL запущен и создана база данных для проекта.
Пример команды (через psql):

```sql
CREATE DATABASE hr_db;
```
5. Настройка переменных окружения
Создайте файл .env в корне проекта (рядом с requirements.txt) со следующим содержимым:

```env
DB_HOST=localhost
DB_PORT=5432
DB_USER=postgres
DB_PASS=your_password
DB_NAME=hr_db
```
Замените your_password на пароль вашего пользователя PostgreSQL.
Если база удалённая – укажите соответствующий хост и порт.

6. Запуск приложения
```bash
uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
```
--reload – автоматический перезапуск при изменении кода (удобно для разработки).

--host 0.0.0.0 – позволяет принимать соединения с других устройств в сети.

--port 8000 – порт, на котором будет доступен сервер.

7. Проверка работоспособности
Откройте браузер и перейдите по адресу:

Swagger UI (интерактивная документация): http://localhost:8000/docs

ReDoc (альтернативная документация): http://localhost:8000/redoc

Корневой эндпоинт: http://localhost:8000/ – вернёт {"message": "HR Management API is running"}

🗄️ Структура базы данных
Таблицы создаются автоматически при первом запуске приложения (используется Base.metadata.create_all).
Схема включает следующие сущности:

departments – подразделения

staffing_table – штатное расписание (привязка к подразделению)

persons – сотрудники (связь со штатной единицей)

drivers_licenses – водительские удостоверения

education_docs – документы об образовании

languages – знание языков

passports – паспортные данные

Все первичные ключи имеют тип UUID (генерируются автоматически).
Внешние ключи настроены с каскадным удалением (CASCADE) или SET NULL в зависимости от логики.

📦 Структура проекта
```text
src/
├── core/                # настройки, подключение к БД, общие типы
│   ├── config.py
│   ├── database.py
├── models/              # SQLAlchemy модели (по одному файлу на таблицу)
│   ├── department.py
│   ├── staffing.py
│   └── ...
├── schemas/             # Pydantic схемы (Create, Update, Response)
├── service_and_rep/     # репозитории (CRUD + бизнес-логика)
├── routers/             # эндпоинты FastAPI
└── main.py              # точка входа
```

📌 Дополнительные команды
Применить миграции (если используется Alembic) – пока не реализовано, таблицы создаются автоматически.

Остановить сервер – Ctrl + C в терминале.

Деактивировать виртуальное окружение – deactivate.