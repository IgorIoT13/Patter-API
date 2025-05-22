from app.dao import DeviceDataDao
from app.models import DeviceData

class DeviceDataTest:
    
    precondion_data = {
        "withOutSecure": {
            "secure_status": None,
            "temprature": 100,
            "humidity": 11
        },
        "withOutTemperature": {
            "secure_status": True,
            "temprature": None,
            "humidity": 11
        },
        "withOutHumidity": {
            "secure_status": True,
            "temprature": 100,
            "humidity": None
        },
        "withOutTemperatureAndHumidity": {
            "secure_status": True,
            "temprature": None,
            "humidity": None
        },
        "withOutSecureAndHumidity": {
            "secure_status": None,
            "temprature": 100,
            "humidity": None
        },
        "withOutSecureAndTemperature": {
            "secure_status": None,
            "temprature": None,
            "humidity": 11
        },
        "withOutAll": {
            "secure_status": None,
            "temprature": None,
            "humidity": None
        }
    }
    
    @staticmethod
    def add_data(self, data: dict) -> DeviceData:
        if data["secure_status"] is None and data["temprature"] is None and data["humidity"] is None:
            device_data = DeviceDataDao.create()
        elif data["secure_status"] is None and data["temprature"] is None:
            device_data = DeviceDataDao.create(
                humidity=data["humidity"]
            )
        elif data["secure_status"] is None and data["humidity"] is None:
            device_data = DeviceDataDao.create(
                temprature=data["temprature"]
            )
        elif data["temprature"] is None and data["humidity"] is None:
            device_data = DeviceDataDao.create(
                secure_status=data["secure_status"]
            )
        elif data["secure_status"] is None:
            device_data = DeviceDataDao.create(
                temprature=data["temprature"],
                humidity=data["humidity"]
            )
        elif data["temprature"] is None:
            device_data = DeviceDataDao.create(
                secure_status=data["secure_status"],
                humidity=data["humidity"]
            )
        elif data["humidity"] is None:
            device_data = DeviceDataDao.create(
                secure_status=data["secure_status"],
                temprature=data["temprature"]
            )
        else:
            device_data = DeviceDataDao.create(
                secure_status=data["secure_status"],
                temprature=data["temprature"],
                humidity=data["humidity"]
            )
        return device_data
    
    @staticmethod
    def precondition() -> dict:
        result = dict()
        for key in DeviceDataTest.precondion_data:
            result[key] = DeviceDataTest.add_data(DeviceDataTest.precondion_data[key])
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
    def check_deleted(deleted: dict) -> None:
        DeviceDataTest.clear(deleted)
        for key in deleted:
            device_data = DeviceDataDao.get_by_id(deleted[key].id)
            assert device_data == None
        
    @staticmethod
    def clear(to_delete: dict) -> None:
        for key in to_delete:
            DeviceDataDao.delete(to_delete[key].id)
    
    @staticmethod
    def tests() -> None:
        data = DeviceDataTest.precondition()
        DeviceDataTest.check_created(data)
        DeviceDataTest.check_updated(data)
        DeviceDataTest.check_deleted(data)
