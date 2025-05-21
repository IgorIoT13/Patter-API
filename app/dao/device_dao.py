from app import db
from app.models import Device, DeviceData, Location

class DeviceDao:
    @staticmethod
    def get_by_id(device_id: int) -> Device: 
        return db.session.query(Device).filter(Device.id == device_id).first()

    @staticmethod
    def get_all():
        return db.session.query(Device).all()
    
    @staticmethod
    def create(
        name: str,
        type: str,
        topic: str,
        data_id: int,
        location_id: int
        ) -> Device:
        
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
    def update(
        device_id: int,
        name: str,
        type: str,
        topic: str,
        data_id: int,
        location_id: int
        ) -> Device:
        device = db.session.query(Device).filter(Device.id == device_id).first()
        
        if name is not None and name != "":
            device.name = name
        if type is not None and type != "":
            device.type = type
        if topic is not None and topic != "":
            device.topic = topic
        if data_id is not None and data_id != "":
            device.data_id = data_id
        if location_id is not None and location_id != "":
            device.location_id = location_id
        db.session.commit()
        
        return device
    
    @staticmethod
    def delete(device_id):
        device = db.session.query(Device).filter(Device.id == device_id).first()
        if device:
            db.session.delete(device)
            db.session.commit()