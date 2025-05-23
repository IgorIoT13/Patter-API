from app import create_app, db
from tests import Data, DeviceDataTest, DeviceTest, LocationTest, UserTest, BrockerTest
from app.dao import DeviceDataDao
from app.services import DeviceService, LocationService, DeviceDataService, UserService

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
        
def test_device_service():
    with app.app_context():
        pass
        loc = LocationService.create(room="testServ", adress="testSecrvice")
        # LocationService.update(loc.id, room="testServUpd", adress="testSecrviceUpd")
        dev = DeviceService.create(name="testServ", type="testServ", topic="testServ", location_id=loc.id)
        # DeviceService.update(dev.id, name="testServUpd", type="testServUpd", topic="testServUpd")
        # dev2 = DeviceService.create(name="testServ", type="testServ", topic="testServ", location_id=1)
        data1 = DeviceDataService.create(device_id=dev.id, secure_status=True, temprature=1.0, humidity=1.0)
        data2 = DeviceDataService.create(device_id=dev.id, secure_status=False, temprature=2.0, humidity=2.0)
        data3 = DeviceDataService.create(device_id=dev.id, secure_status=True, temprature=3.0, humidity=3.0)
        DeviceDataService.update(data1.id, device_id=dev.id, secure_status=False, temprature=4.0, humidity=4.0)
        DeviceDataService.update(data2.id, device_id=dev.id, secure_status=True, temprature=5.0, humidity=5.0)
        DeviceDataService.update(data3.id, device_id=dev.id, secure_status=False, temprature=6.0, humidity=6.0)
        # DeviceService.delete(dev.id)
        
        # try:
        user = UserService.create(username="testServ", password="testServ", number="testServ")
        userToDelete = UserService.create(username="testServ1", password="testServ", number="testServ")
        # except ValueError as e:
        #     print(f"User creation failed: {e}")
            
        UserService.update(user.id, username="testServUpd", password="testServUpd", number="testServUpd")
        UserService.delete(userToDelete.id)
            

        
        
        # LocationService.delete(loc.id)
        
if __name__ == '__main__':
    prepare_test_environment()
    test_device_service()
    # test_device_part_dao()
    

