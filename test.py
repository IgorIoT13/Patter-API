from app import create_app, db
from tests import Data, DeviceDataTest, DeviceTest, LocationTest, UserTest, BrockerTest
from app.dao import DeviceDataDao

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
        
if __name__ == '__main__':
    prepare_test_environment()
    test_device_part_dao()
    

