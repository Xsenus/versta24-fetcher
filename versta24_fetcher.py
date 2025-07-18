import os
import json
import time
import requests
from dotenv import load_dotenv

# Загрузка API-ключа
load_dotenv()
API_KEY = os.getenv("VERSTA24_API_KEY")
if not API_KEY:
    raise RuntimeError("❌ Не найден VERSTA24_API_KEY в .env файле")

# Константы
API_URL = "https://api.versta24.ru/openapi/v2/PickupPoints"
HEADERS = {
    "Authorization": f"apiKey {API_KEY}",
    "Accept": "application/json"
}
CITIES_FILE = "used_cities.json"
RESPONSES_DIR = "responses"
os.makedirs(RESPONSES_DIR, exist_ok=True)

# Загрузка списка городов
with open(CITIES_FILE, "r", encoding="utf-8") as f:
    cities = json.load(f)

# Шаг 1–3: Получение и сохранение ответов по каждому городу
for city in cities:
    filename = os.path.join(RESPONSES_DIR, f"{city}.json")
    if os.path.exists(filename):
        print(f"⏭️ Пропуск {city}, файл уже существует")
        continue

    params = {"countryId": "RU", "cityName": city}
    try:
        response = requests.get(API_URL, headers=HEADERS, params=params, timeout=15)
        response.raise_for_status()
        data = response.json()

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        print(f"✅ Сохранено: {city} ({len(data.get('pickupPoints', []))} точек)")
    except Exception as e:
        print(f"❌ Ошибка при запросе {city}: {e}")
    
    time.sleep(0.1)

# Шаг 4: Сбор всех ответов в один JSON
combined = {}
for city in cities:
    filename = os.path.join(RESPONSES_DIR, f"{city}.json")
    if not os.path.exists(filename):
        continue

    with open(filename, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
            combined[city] = data.get("pickupPoints", [])
        except json.JSONDecodeError:
            print(f"⚠️ Пропуск повреждённого файла: {filename}")

# Сохранение объединённого JSON
with open("all_pickup_points.json", "w", encoding="utf-8") as f:
    json.dump(combined, f, ensure_ascii=False, indent=2)

print("✅ Объединённый файл сохранён: all_pickup_points.json")