from app.models import Brocker
from app.dao import BrockerDao
from . import DeviceService, UserService

class BrockerService:
    
    @staticmethod
    def create(id_device: int, id_user: int) -> Brocker:
        device = DeviceService.get_by_id(id_device)
        if not device:
            raise ValueError(f"Device with id {id_device} does not exist.")
        
        user = UserService.get_by_id(id_user)
        if not user:
            raise ValueError(f"User with id {id_user} does not exist.")
        
        brocker = BrockerDao.create(id_device, id_user)
        return brocker
    
    @staticmethod
    def get_all() -> list[Brocker]:
        return BrockerDao.get_all()
    
    @staticmethod
    def get_by_id(id: int) -> Brocker:
        return BrockerDao.get_by_id(id)
    
    @staticmethod
    def get_all_by_property(id_device: int = None, id_user: int = None) -> list:
        data = BrockerDao.get_all()
        if id_device is not None and id_user is not None:
            return [item for item in data if item.id_device == id_device and item.id_user == id_user]
        elif id_device is not None:
            return [item for item in data if item.id_device == id_device]
        elif id_user is not None:
            return [item for item in data if item.id_user == id_user]
        else:
            return data
    
    @staticmethod
    def update(id: int, id_device: int = None, id_user: int = None) -> None:
        if id is None:
            raise ValueError("ID cannot be None.")
        elif id <= 0:
            raise ValueError("ID must be a positive integer.")
        
        brocker = BrockerDao.get_by_id(id)
        if not brocker:
            raise ValueError(f"Brocker with id {id} does not exist.")
        
        ready_id_device = id_device if id_device is not None else brocker.id_device
        ready_id_user = id_user if id_user is not None else brocker.id_user
        
        device = DeviceService.get_by_id(ready_id_device)
        if not device:
            raise ValueError(f"Device with id {ready_id_device} does not exist.")
        user = UserService.get_by_id(ready_id_user)
        if not user:
            raise ValueError(f"User with id {ready_id_user} does not exist.")
        
        brocker = BrockerDao.update(id, ready_id_device, ready_id_user)
    
    @staticmethod
    def delete(id: int) -> None:
        if id is None:
            raise ValueError("ID cannot be None.")
        elif id <= 0:
            raise ValueError("ID must be a positive integer.")
        
        brocker = BrockerDao.get_by_id(id)
        if not brocker:
            raise ValueError(f"Brocker with id {id} does not exist.")
        
        BrockerDao.delete(id)