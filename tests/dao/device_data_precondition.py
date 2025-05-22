from app.dao import DeviceDataDao, DeviceDao, LocationDao
from app.models import DeviceData, Device, Location
from .data import Data

class DeviceDataTest:
    
    precondion_data = Data.get_device_data()
    
    @staticmethod
    def add_data(id: int, data: dict) -> DeviceData:
        
        if data["secure_status"] is None and data["temprature"] is None and data["humidity"] is None:
            device_data = DeviceDataDao.create(id)
        elif data["secure_status"] is None and data["temprature"] is None:
            device_data = DeviceDataDao.create(
                device_id=id,
                humidity=data["humidity"]
            )
        elif data["secure_status"] is None and data["humidity"] is None:
            device_data = DeviceDataDao.create(
                device_id=id,
                temprature=data["temprature"]
            )
        elif data["temprature"] is None and data["humidity"] is None:
            device_data = DeviceDataDao.create(
                device_id=id,
                secure_status=data["secure_status"]
            )
        elif data["secure_status"] is None:
            device_data = DeviceDataDao.create(
                device_id=id,
                temprature=data["temprature"],
                humidity=data["humidity"]
            )
        elif data["temprature"] is None:
            device_data = DeviceDataDao.create(
                device_id=id,
                secure_status=data["secure_status"],
                humidity=data["humidity"]
            )
        elif data["humidity"] is None:
            device_data = DeviceDataDao.create(
                device_id=id,
                secure_status=data["secure_status"],
                temprature=data["temprature"]
            )
        else:
            device_data = DeviceDataDao.create(
                device_id=id,
                secure_status=data["secure_status"],
                temprature=data["temprature"],
                humidity=data["humidity"]
            )
        return device_data
    
    @staticmethod
    def create_device() -> Device:
        location = LocationDao.create(
            "test",
            "Test12"
        )
        device = DeviceDao.create(
            name="Test Device",
            type="Test Type",
            topic="Test Topic",
            location_id=location.id
        )
        return device
    
    @staticmethod
    def precondition() -> dict:
        default_device = DeviceDataTest.create_device()
        result = dict()
        for key in DeviceDataTest.precondion_data:
            result[key] = DeviceDataTest.add_data(default_device.id, DeviceDataTest.precondion_data[key])
        return result
    
    @staticmethod
    def check_created(data: dict) -> None:
        for key in data:
            device_data = DeviceDataDao.get_by_id(data[key].id)
            assert device_data.id != None
            assert device_data.secure_status == data[key].secure_status
            assert device_data.temprature == data[key].temprature
            assert device_data.humidity == data[key].humidity
        
    @staticmethod
    def check_updated(data: dict) -> None:
        DeviceDataDao.update(
            data["withOutSecure"].id,
            secure_status=True,
            temprature=115,
            humidity=30
        )
        test_data = DeviceDataDao.get_by_id(data["withOutSecure"].id)
        assert test_data.secure_status == True
        assert test_data.temprature == 115
        assert test_data.humidity == 30
        
        DeviceDataDao.update(
            data["withOutTemperature"].id,
            secure_status=False,
            temprature=20,
            humidity=30
        )
        
        test_data = DeviceDataDao.get_by_id(data["withOutTemperature"].id)
        assert test_data.secure_status == False
        assert test_data.temprature == 20
        assert test_data.humidity == 30
    
    @staticmethod
    def check_deleted(deleted: dict, clear_all: bool = False) -> None:
        if clear_all:
            DeviceDataTest.clear(deleted)
            for key in deleted:
                device_data = DeviceDataDao.get_by_id(deleted[key].id)
                assert device_data == None
        else:
            data = DeviceDataTest.add_data(1, {
                "secure_status": False,
                "temprature": 1,
                "humidity": 2
            })
            other = DeviceDataDao.get_by_id(data.id)
            assert other != None
            assert other.id == data.id
            assert other.secure_status == data.secure_status
            assert other.temprature == data.temprature
            assert other.humidity == data.humidity
            assert other.time == data.time
            
            DeviceDataDao.delete(data.id)
            other = DeviceDataDao.get_by_id(data.id)
            assert other == None
            
        
    @staticmethod
    def clear(to_delete: dict) -> None:
        for key in to_delete:
            DeviceDataDao.delete(to_delete[key].id)
    
    @staticmethod
    def tests(clear:bool = True) -> None:
        data = DeviceDataTest.precondition()
        DeviceDataTest.check_created(data)
        DeviceDataTest.check_updated(data)
        DeviceDataTest.check_deleted(data, clear)
