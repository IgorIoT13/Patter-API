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
    def get_by_property(name: str = None, type: str = None, topic: str = None) -> Device:
        query = db.session.query(Device)
        if name is not None:
            query = query.filter(Device.name == name)
        if type is not None:
            query = query.filter(Device.type == type)
        if topic is not None:
            query = query.filter(Device.topic == topic)
        return query.first()
    
    @staticmethod
    def create(
        name: str,
        type: str,
        topic: str,
        location_id: int
        ) -> Device:
        
        device = Device(
            name=name,
            type=type,
            topic=topic,
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
        location_id: int
        ) -> Device:
        device = DeviceDao.get_by_id(device_id)
        
        if name is not None and name != "":
            device.name = name
        if type is not None and type != "":
            device.type = type
        if topic is not None and topic != "":
            device.topic = topic
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