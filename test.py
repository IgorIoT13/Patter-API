from app import create_app, db
from tests import DeviceDataTest, Data
from app.dao import DeviceDataDao

app = create_app()

def prepare_test_environment():
    with app.app_context():
        Data.create_base_device_structure()

def test_device_data_dao():
    with app.app_context():
        DeviceDataTest.tests()
        
if __name__ == '__main__':
    prepare_test_environment()
    test_device_data_dao()
    

