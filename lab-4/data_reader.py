import csv
import requests
import time

API_URL = "https://data.cityofnewyork.us/resource/hvrh-b6nb.json"

def read_data(file_path, limit=10):
    """Зчитує дані з CSV-файлу, повертає список рядків (словників)."""
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        data = []
        for i, row in enumerate(reader):
            if i >= limit:
                break
            data.append(row)
    return data

def fetch_and_save_data_csv(csv_path, total_rows=10000, batch_size=1000, sleep_sec=0.5):
    """
    Завантажує total_rows рядків з API частинами та зберігає у CSV-файл.
    """
    all_rows = []
    offset = 0
    for _ in range(0, total_rows, batch_size):
        params = {
            "$limit": batch_size,
            "$offset": offset
        }
        resp = requests.get(API_URL, params=params)
        resp.raise_for_status()
        batch = resp.json()
        if not batch:
            break
        all_rows.extend(batch)
        offset += batch_size
        time.sleep(sleep_sec)  # щоб не перевантажити API
    if all_rows:
        # Зберігаємо у CSV
        import csv
        keys = set()
        for row in all_rows:
            keys.update(row.keys())
        keys = list(keys)
        with open(csv_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            writer.writerows(all_rows)
    return len(all_rows)
