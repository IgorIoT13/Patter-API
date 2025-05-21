from app import db
from app.models import DeviceData
from datetime import datetime
from typing import Optional

class DeviceDataDao:
    
    @staticmethod
    def get_all() -> list:
        return DeviceData.query.all()
    
    @staticmethod
    def get_by_id(device_data_id: int) -> DeviceData:
        return DeviceData.query.get(device_data_id)
    
    @staticmethod
    def update(
        device_data_id: int,
        secure_status: Optional[bool] = None, 
        temprature: Optional[float] = None, 
        humidity: Optional[float] = None 
    ) -> DeviceData:
        data = DeviceDataDao.get_device_data_by_id(device_data_id)
        if secure_status is not None:
            data.secure_status = secure_status
        if temprature is not None:
            data.temprature = temprature
        if humidity is not None:
            data.humidity = humidity
    
        data.time = datetime.utcnow()
        db.session.commit()
        return data
    
    @staticmethod
    def create(secure_status: bool = False, temprature: float = 0, humidity: float = 0) -> DeviceData:
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
    def delete(data_id: int) -> None:
        data = DeviceDataDao.get_device_data_by_id(data_id)
        db.session.delete(data)
        db.session.commit()
    
    