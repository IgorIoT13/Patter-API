from app.dao import LocationDao
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
    def create(room: str = None, adress: str = None) -> Location:
        if room is None or adress is None:
            raise ValueError("Room and address cannot be None")
        if LocationDao.get_by_property(room, adress):
            raise ValueError("Location already exists")
        return LocationDao.create(room, adress)