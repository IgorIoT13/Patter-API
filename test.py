from app import create_app, db
from tests import Data, DeviceDataTest, DeviceTest, LocationTest, UserTest, BrockerTest
from app.dao import DeviceDataDao
from app.services import DeviceService, LocationService

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
        loc = LocationService.create(room="testServ", adress="testSecrvice")
        LocationService.update(loc.id, room="testServUpd", adress="testSecrviceUpd")
        dev = DeviceService.create(name="testServ", type="testServ", topic="testServ", location_id=loc.id)
        DeviceService.update(dev.id, name="testServUpd", type="testServUpd", topic="testServUpd")
        
if __name__ == '__main__':
    prepare_test_environment()
    test_device_service()
    # test_device_part_dao()
    

