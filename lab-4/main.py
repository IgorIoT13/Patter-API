from data_reader import read_data
from strategy import get_strategy

# from data_reader import fetch_and_save_data_csv


if __name__ == "__main__":
    # Вкажіть шлях до вашого CSV-файлу
    # fetch_and_save_data_csv("green_taxi_sample.csv")
    file_path = "green_taxi_sample.csv"  # або інший шлях до датасету
    data = read_data(file_path, limit=10)  # limit для тесту, можна прибрати
    strategy = get_strategy()
    strategy.output(data)
