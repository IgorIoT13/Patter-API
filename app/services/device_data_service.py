from app.models import DeviceData
from app.dao import DeviceDataDao

class DeviceDataService:
    @staticmethod
    def get_all() -> list:
        return DeviceDataDao.get_all()

    @staticmethod
    def get_by_id(device_data_id: int) -> DeviceData:
        device_data = DeviceDataDao.get_by_id(device_data_id)
        return device_data

    @staticmethod
    def create(device_id: int, 
        secure_status: bool = False,
        temprature: float = 0,
        humidity: float = 0
    ) -> DeviceData:
        if device_id is None:
            raise ValueError("Device ID cannot be None")
        if device_id <= 0:
            raise ValueError("Device ID must be a positive integer")
        if secure_status is None:
            raise ValueError("Secure status cannot be None")
        if temprature is None or humidity is None:
            raise ValueError("Temperature and humidity cannot be None")
        device_data = DeviceDataDao.create(device_id, secure_status, temprature, humidity)
        return device_data
        
    
    @staticmethod
    def update(
        device_data_id: int,
        device_id: int = None,
        secure_status: bool = None,
        temprature: float = None,
        humidity: float = None
    ) -> DeviceData:
        data = DeviceDataDao.get_by_id(device_data_id)
        ready_device_id = device_id if device_id is not None else data.device_id
        ready_secure_status = secure_status if secure_status is not None else data.secure_status
        ready_temprature = temprature if temprature is not None else data.temprature
        ready_humidity = humidity if humidity is not None else data.humidity
        
        if device_id is None and secure_status is None and temprature is None and humidity is None:
            raise ValueError("At least one fild must be updated")
        DeviceDataDao.update(
            device_data_id,
            device_id=ready_device_id,
            secure_status=ready_secure_status,
            temprature=ready_temprature,
            humidity=ready_humidity
        )
        
    @staticmethod
    def get_by_device_id(device_id: int) -> DeviceData:
        if device_id is None:
            raise ValueError("Device ID cannot be None")
        if device_id <= 0:
            raise ValueError("Device ID must be a positive integer")
        device_data = DeviceDataDao.get_all()
        device_data = [data for data in device_data if data.device_id == device_id]
        return device_data
        
    @staticmethod
    def delete(device_data_id: int) -> None:
        if device_data_id is None:
            raise ValueError("Device data ID cannot be None")
        if device_data_id <= 0:
            raise ValueError("Device data ID must be a positive integer")
        device_data = DeviceDataDao.get_by_id(device_data_id)
        
        if device_data is None:
            raise ValueError("Device data not found")
        
        DeviceDataDao.delete(device_data.id)
    