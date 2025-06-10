from app import create_app, db
from tests import Data, DeviceDataTest, DeviceTest, LocationTest, UserTest, BrockerTest
from app.services import DeviceService, LocationService, DeviceDataService, UserService, BrockerService
# import pymysql

import random
import time

app = create_app()

with app.app_context():
    db.drop_all()
    print("All tables dropped!")
    
app = create_app()

def prepare_test_environment():
    with app.app_context():
        Data.create_data_base()

def test_device_part_dao():
    with app.app_context():
        DeviceDataTest.tests()
        DeviceTest.tests()
        LocationTest.tests()
        UserTest.tests()
        BrockerTest.tests()
        UserTest.delete_test(id = Data.get_broker()["to_delete"]["user_id"])
        
def BaseLocationTablesServices():
    LocationService.create("kitchen", "Lviv, Ukraine")
    LocationService.create("living room", "Lviv, Ukraine")
    LocationService.create("bedroom", "Lviv, Ukraine")
    
    LocationService.create("office", "Kyiv, Ukraine")
    LocationService.create("garage", "Kyiv, Ukraine")
    LocationService.create("garden", "Kyiv, Ukraine")
    
def BaseDeviceTablesServices(list_locations=None):
    min = 1
    max = len(list_locations) if list_locations else 1
    
    DeviceService.create("Kitchen Light", "Light", "kitchen/light", random.randint(min, max))
    DeviceService.create("Living Room Fan", "Fan", "living_room/fan", random.randint(min, max))
    DeviceService.create("Living Room Light", "Light", "living_room/light", random.randint(min, max))
    DeviceService.create("Bedroom Light", "Light", "bedroom/light", random.randint(min, max))
    
    DeviceService.create("Office Light", "Light", "office/light", random.randint(min, max))
    DeviceService.create("Garage Light", "Light", "garage/light", random.randint(min, max))
    DeviceService.create("Garden Light", "Light", "garden/light", random.randint(min, max))

def Device_test_service():
    cur_device = DeviceService.get_by_property(name="test_device")
    cur_location = LocationService.get_by_property(room="garden", adress="Kyiv, Ukraine")
    DeviceService.update(cur_device.id, topic="empty")
    DeviceService.update(cur_device.id, name="Garden Light Updated", location_id=cur_location.id)
    time.sleep(15)
    DeviceService.delete(cur_device.id)
    
def BaseDeviceDataTablesServices(device_list=None):
    min = 1
    max = len(device_list) if device_list else 1
    
    DeviceDataService.create(
        random.randint(min, max), secure_status=True, 
        temprature=random.uniform(0.4, 35.0), 
        humidity=random.uniform(0.1, 99.9)
    )
    DeviceDataService.create(
        random.randint(min, max), secure_status=False, 
        humidity=random.uniform(0.1, 99.9)
    )
    DeviceDataService.create(
        random.randint(min, max), secure_status=True, 
        humidity=random.uniform(0.1, 99.9)
    )
    DeviceDataService.create(
        random.randint(min, max), secure_status=False, 
        temprature=random.uniform(0.4, 35.0),
    )

def DeviceData_test_service():
    cur_device = DeviceDataService.get_by_id(2)
    print(f"DeviceData: {cur_device.id}")
    DeviceDataService.update(
        cur_device.id, 
        secure_status=True, 
        temprature=100.0, 
        humidity=-59
    )
    time.sleep(15)
    DeviceDataService.delete(cur_device.id)
        
def test_device_service():
    with app.app_context():
        BaseLocationTablesServices()
        list_locations = LocationService.get_all()
        BaseDeviceTablesServices(list_locations)
        list_devices = DeviceService.get_all()
        BaseDeviceDataTablesServices(list_devices)
        DeviceData_test_service()
        
        # Device_test_service()        
        # pass
        
if __name__ == '__main__':
    prepare_test_environment()
    test_device_service()
    # test_device_part_dao()
    

