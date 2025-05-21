from app import db
from app.models import DeviceData
from datetime import datetime

class DeviceDataDao:
    
    @staticmethod
    def get_all() -> list:
        return DeviceData.query.all()
    
    @staticmethod
    def get_by_id(device_data_id) -> DeviceData:
        if device_data_id is None:
            raise ValueError("device_data_id cannot be None")
        return DeviceData.query.get(device_data_id)
    
    @staticmethod
    def update_data(device_data_id, secure_status = False, temprature = 0, humidity = 0) -> DeviceData:
        data = DeviceDataDao.get_device_data_by_id(device_data_id)
        if data is None:
            raise ValueError("DeviceData not found")
        data.secure_status = secure_status
        data.temprature = temprature
        data.humidity = humidity
        data.time = datetime.utcnow()
        db.session.commit()
        return data
    
    @staticmethod
    def create(secure_status = False, temprature = 0, humidity = 0) -> DeviceData:
        data = DeviceData(
            secure_status=secure_status,
            temprature=temprature,
            humidity=humidity,
            time=datetime.utcnow()
        )
        db.session.add(data)
        db.session.commit()
        return data
    
    @staticmethod
    def delete(data_id) -> None:
        data = DeviceDataDao.get_device_data_by_id(data_id)
        if data is None:
            raise ValueError("DeviceData not found")
        db.session.delete(data)
        db.session.commit()
    
    