from app import create_app, db
from .tests.dao import DeviceDataTest

app = create_app()

def test_device_data_dao():
    with app.app_context():
        DeviceDataTest.tests()

