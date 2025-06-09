from app.dao import DeviceDao, DeviceDao
from app.models import Device, Device
from .device_data_service import DeviceDataService
from .brocker_service import BrockerService
from moduls.tools import log_def

class DeviceService:
    __name__ = "DeviceService"
    
    @log_def(obj_name=__name__)
    @staticmethod
    def get_all() -> list:
        return DeviceDao.get_all()

    @log_def(obj_name=__name__)
    @staticmethod
    def get_by_id(device_id: int) -> Device:
        device = DeviceDao.get_by_id(device_id)
        return device
    
    @log_def(obj_name=__name__)
    @staticmethod
    def get_by_property(name: str = None, type: str = None, topic: str = None) -> Device:
        device = DeviceDao.get_by_property(name, type, topic)
        return device

    @log_def(obj_name=__name__)
    @staticmethod
    def create(name: str, type: str, topic: str, location_id: int) -> Device:
        if name is None or type is None or topic is None or location_id is None:
            raise ValueError("Name, type, topic and location_id cannot be None")
        if DeviceDao.get_by_property(name, type, topic):
            raise ValueError("Device already exists")
        return DeviceDao.create(name, type, topic, location_id)

    @log_def(obj_name=__name__)
    @staticmethod
    def update(
        device_id: int,
        name: str = None,
        type: str = None,
        topic: str = None,
        location_id: int = None
    ) -> None:
        if device_id is None:
            raise ValueError("Device ID cannot be None")
        if device_id <= 0:
            raise ValueError("Device ID must be a positive integer")
        device = DeviceDao.get_by_id(device_id)
        
        if device is None:
            raise ValueError("Device not found")
        if name == device.name and type == device.type and topic == device.topic:
            raise ValueError("No changes detected")
        if name is None and type is None and topic is None:
            raise ValueError("Name, type and topic cannot be None")
        if name == "" or name == " " or type == "" or type == " " or topic == "" or topic == " ":
            raise ValueError("Name, type and topic cannot be empty")
        if DeviceService.get_by_property(name, type, topic):
            raise ValueError("Device already exists")
        
        ready_name, ready_type = device.name, device.type
        ready_topic, ready_location_id = device.topic, device.location_id
        
        if name is not None:
            ready_name = name
        if type is not None:
            ready_type = type
        if topic is not None:
            ready_topic = topic
        if location_id is not None:
            ready_location_id = location_id
            
        if name is not None and type is not None and topic is not None:
            DeviceDao.update(device_id, ready_name, ready_type, ready_topic, ready_location_id)

    @log_def(obj_name=__name__)
    @staticmethod
    def delete(device_id: int, device: Device = None) -> None:
        id = device_id
        if device is not None:
            id = device.id
        elif device_id is None:
            raise ValueError("Device ID cannot be None")
        elif device_id <= 0:
            raise ValueError("Device ID must be a positive integer")
        
        device = DeviceDao.get_by_id(device_id)
        
        if device is None:
            raise ValueError("Device not found")
        
        data = DeviceDataService.get_all_by_device_id(device_id)
        if data is not None:
            for d in data:
                DeviceDataService.delete(d.id)
                
        brocker = BrockerService.get_all_by_property(id_device=device_id)
        if brocker is not None:
            for b in brocker:
                BrockerService.delete(b.id)
        
        DeviceDao.delete(device_id)
    
    @log_def(obj_name=__name__)
    @staticmethod
    def get_by_location(location_id: int) -> list:
        if location_id is None:
            raise ValueError("Location ID cannot be None")
        if location_id <= 0:
            raise ValueError("Location ID must be a positive integer")
        
        devices = DeviceDao.get_all()
        
        for device in devices:
            if device.location_id != location_id:
                devices.remove(device)
        return devices
        