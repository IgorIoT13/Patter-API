from app import create_app, db
from tests import DeviceDataTest
from app.dao import DeviceDataDao

app = create_app()

def test_device_data_dao():
    with app.app_context():
        DeviceDataTest.tests()
        
if __name__ == '__main__':
    test_device_data_dao()
    

