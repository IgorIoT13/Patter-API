import csv
import random

def random_username(i):
    return f"user_{i}"

def random_password():
    return f"pass{random.randint(1000,9999)}"

def random_number(i):
    return f"+380{random.randint(100000000,999999999)}"

def random_room():
    return f"Room-{random.randint(1, 50)}"

def random_address():
    return f"Street {random.randint(1, 100)}, City"

def random_device_name(i):
    return f"Device_{i}"

def random_device_type():
    return random.choice(["sensor", "actuator", "camera"])

def random_topic():
    return f"topic/{random.randint(1, 100)}"

def random_secure_status():
    return random.choice(["True", "False"])

def random_temperature():
    return round(random.uniform(15.0, 30.0), 2)

def random_humidity():
    return round(random.uniform(30.0, 90.0), 2)

with open("test_data.csv", "w", newline='', encoding="utf-8") as csvfile:
    fieldnames = [
        "user_username", "user_password", "user_number",
        "location_room", "location_adress",
        "device_name", "device_type", "device_topic",
        "device_data_secure_status", "device_data_temprature", "device_data_humidity"
    ]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for i in range(1, 1001):
        writer.writerow({
            "user_username": random_username(i),
            "user_password": random_password(),
            "user_number": random_number(i),
            "location_room": random_room(),
            "location_adress": random_address(),
            "device_name": random_device_name(i),
            "device_type": random_device_type(),
            "device_topic": random_topic(),
            "device_data_secure_status": random_secure_status(),
            "device_data_temprature": random_temperature(),
            "device_data_humidity": random_humidity()
        })