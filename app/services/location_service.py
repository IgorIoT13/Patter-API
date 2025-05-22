from app.dao import LocationDao, DeviceDao
from .device_service import DeviceService
from app.models import Location

class LocationService:
    
    @staticmethod
    def get_all() -> list:
        return LocationDao.get_all()
    
    @staticmethod
    def get_by_id(location_id: int) -> Location:
        location = LocationDao.get_by_id(location_id)
        return location 
    
    @staticmethod
    def get_by_property(room: str = None, adress: str = None) -> Location:
        location = LocationDao.get_by_property(room, adress)
        return location
    
    @staticmethod
    def update(location_id: int, room: str = None, adress: str = None) -> None:
        if location_id is None:
            raise ValueError("Location ID cannot be None")
        if location_id <= 0:
            raise ValueError("Location ID must be a positive integer")
        
        location = LocationDao.get_by_id(location_id)
        
        if location is None:
            raise ValueError("Location not found")
        if room == location.room and adress == location.adress:
            raise ValueError("No changes detected")
        if room is None and adress is None:
            raise ValueError("Room and address cannot be None")
        if room == "" or room == " " or adress == "" or adress == " ":
            raise ValueError("Room and address cannot be empty")
        if LocationDao.get_by_property(room, adress):
            raise ValueError("Location already exists")
        if room is not None and adress is not None:
            LocationDao.update(location_id, room, adress)
        elif room is not None:
            LocationDao.update(location_id, room, location.adress)
        elif adress is not None:
            LocationDao.update(location_id, location.room, adress)
            
    @staticmethod
    def create(room: str = None, adress: str = None) -> Location:
        if room is None or adress is None:
            raise ValueError("Room and address cannot be None")
        if LocationDao.get_by_property(room, adress):
            raise ValueError("Location already exists")
        return LocationDao.create(room, adress)
    
    @staticmethod
    def delete(location_id: int, location: Location = None) -> None:
        id = location_id
        if location is not None:
            id = location.id
        elif location_id is None:
            raise ValueError("Location ID cannot be None")
        elif location_id <= 0:
            raise ValueError("Location ID must be a positive integer")
        
        location = LocationDao.get_by_id(location_id)
        if location is None:
            raise ValueError("Location not found")
        
        LocationDao.delete(location_id)
        #TREBA DO PISATI VIDALENIA DEVICE
        
        
        
        
        
        
        
    