from app import db
from app.models import Device, DeviceData, Location

class DeviceDao:
    @staticmethod
    def get_device_by_id(device_id: int) -> Device:
        if device_id <= 0:
            raise ValueError("device_id must be greater than 0")
        if device_id is None:
            raise ValueError("device_id cannot be None")
        
        return db.session.query(Device).filter(Device.id == device_id).first()

    @staticmethod
    def get_all_devices():
        return db.session.query(Device).all()
    
    @staticmethod
    def add_device(
        name: str,
        type: str,
        topic: str,
        data_id: int,
        location_id: int,
        ) -> Device:
        
        if name is None or "" or " " or type is None or "" or " " or topic is None or "" or " ":
            raise ValueError("Name, type, and topic cannot be None or empty")
        if data_id is None or location_id is None:
            raise ValueError("data_id and location_id cannot be None")
        if data_id <= 0 or location_id <= 0:
            raise ValueError("data_id and location_id must be greater than 0")
        
        device = Device(
            name=name,
            type=type,
            topic=topic,
            data_id=data_id,
            location_id=location_id
        )
        db.session.add(device)
        db.session.commit()
        return device
    
    @staticmethod
    def update_device(device):
        db.session.merge(device)
        db.session.commit()
        return device
    
    @staticmethod
    def delete_device(device_id):
        device = db.session.query(Device).filter(Device.id == device_id).first()
        if device:
            db.session.delete(device)
            db.session.commit()