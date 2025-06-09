from app import create_app, db
from tests import Data, DeviceDataTest, DeviceTest, LocationTest, UserTest, BrockerTest
from app.services import DeviceService, LocationService, DeviceDataService, UserService, BrockerService
# import pymysql

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
        
def test_device_service():
    with app.app_context():
        # loc = LocationService.create(room="testServ", adress="testSecrvice")
        # LocationService.update(loc.id, room="testServUpd", adress="testSecrviceUpd")
        
        LocationService.create(room="testServ", adress="testServ")
        LocationService.create(room="testServ1", adress="testServ3")
        loc = LocationService.get_by_property(room="testServ1")
        # loc_out = LocationService.get_by_property(room="testServUpd", adress="testServUpd1")
        
        # print(f"Local_out {loc_out.id}, {loc_out.adress}, {loc_out.room}")
        LocationService.update(loc.id, room="testServUpd", adress="testServUpd1")
        loc = LocationService.get_by_property(adress="testServUpd")
        
        # LocationService.update(-1)
        # LocationService.get_by_property()
        
        
        # dev = DeviceService.create(name="testServ", type="testServ", topic="testServ", location_id=loc.id)
        # DeviceService.update(dev.id, name="testServUpd", type="testServUpd", topic="testServUpd")
        # dev2 = DeviceService.create(name="testServ1", type="testServ", topic="testServ", location_id=loc.id)
        # data1 = DeviceDataService.create(device_id=dev.id, secure_status=True, temprature=1.0, humidity=1.0)
        # data2 = DeviceDataService.create(device_id=dev.id, secure_status=False, temprature=2.0, humidity=2.0)
        # data3 = DeviceDataService.create(device_id=dev.id, secure_status=True, temprature=3.0, humidity=3.0)
        # DeviceDataService.update(data1.id, device_id=dev.id, secure_status=False, temprature=4.0, humidity=4.0)
        # DeviceDataService.update(data2.id, device_id=dev.id, secure_status=True, temprature=5.0, humidity=5.0)
        # DeviceDataService.update(data3.id, device_id=dev.id, secure_status=False, temprature=6.0, humidity=6.0)

        # user = UserService.create(username="testServ", password="testServ", number="testServ")
        # userToDelete = UserService.create(username="testServ1", password="testServ", number="testServ")
        # UserService.update(user.id, username="testServUpd", password="testServUpd", number="testServUpd")
        
        # brocker = BrockerService.create(dev.id, user.id)
        # brocker2 = BrockerService.create(dev2.id, user.id)
        # brocker_to_update = BrockerService.get_all_by_property(dev2.id, user.id)
        # if brocker_to_update:
        #     brocker_to_update = brocker_to_update[0]
        #     BrockerService.update(id=brocker_to_update.id, id_user=userToDelete.id)
        
        # LocationService.delete(loc.id)
        pass
        
if __name__ == '__main__':
    prepare_test_environment()
    test_device_service()
    # test_device_part_dao()
    

