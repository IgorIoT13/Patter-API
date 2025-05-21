from app import db
from app.models import Device

class DeviceDao:
    @staticmethod
    def get_device_by_id(device_id):
        return db.session.query(Device).filter(Device.id == device_id).first()

    @staticmethod
    def get_all_devices():
        return db.session.query(Device).all()
    
    @staticmethod
    def add_device(device):
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