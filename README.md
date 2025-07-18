# Versta24 FETCHER

Скрипт для получения точек самовывоза (`PickupPoints`) из API [versta24.ru](https://api.versta24.ru) по 100 крупнейшим городам России.

## 🔧 Функциональность

- Загружает список 100 крупнейших городов из `cities_top_100.json`.
- Делает запросы к `https://api.versta24.ru/openapi/v2/PickupPoints` по каждому городу.
- Сохраняет каждый ответ в файл `responses/<Город>.json`.
- Пропускает запрос, если файл уже существует.
- Объединяет все результаты в единый файл `all_pickup_points.json`.

## 📦 Установка

1. Клонируйте репозиторий:

    ```bash
    git clone <repo_url>
    cd api.versta24
    ```

2. Установите зависимости:

    ```bash
    pip install -r requirements.txt
    ```

3. Создайте файл `.env` с вашим API-ключом:

    ```bash
    VERSTA24_API_KEY=your_api_key_here
    ```

4. Запустите скрипт:

    ```bash
    python main.py
    ```

## 📁 Структура проекта

```bash
api.versta24/
├── .env                    # Файл с API-ключом (в .gitignore)
├── README.md               # Описание проекта
├── main.py                 # Основной скрипт
├── cities_top_100.json     # Список 100 городов
├── all_pickup_points.json  # Объединённый файл со всеми точками (автоматически создаётся)
├── responses/              # Отдельные файлы ответов по каждому городу
└── .gitignore              # Исключения для git
```

## ✅ Зависимости

Укажите в `requirements.txt`:

```bash
requests
python-dotenv
```

## 🛡 Безопасность

- Никогда не коммитьте файл `.env`!
- Убедитесь, что вы не делитесь `all_pickup_points.json`, если он содержит чувствительные данные.

## 📜 Лицензия

MIT
