from app.dao import LocationDao, DeviceDao
from .device_service import DeviceService
from app.models import Location
from moduls.tools import VariableTools

class LocationService:
    
    @staticmethod
    def get_all() -> list:
        return LocationDao.get_all()
    
    @staticmethod
    def get_by_id(location_id: int) -> Location:
        VariableTools.check_id(location_id, "Location")
        location = LocationDao.get_by_id(location_id)
        return location 
    
    @staticmethod
    def get_by_property(room: str = None, adress: str = None) -> Location:
        VariableTools.one_can_be_not_none(room, adress)
        if VariableTools.check_not_empty_str(room) and VariableTools.check_not_empty_str(adress):
            location = LocationDao.get_by_property(room, adress)
        elif VariableTools.check_not_empty_str(room):
            location = LocationDao.get_by_room(room)
        elif VariableTools.check_not_empty_str(adress):
            location = LocationDao.get_by_adress(adress)
        else:
            location = None
        return location
    
    @staticmethod
    def update(location_id: int, room: str = None, adress: str = None) -> None:
        VariableTools.check_id(location_id, "Location")
        VariableTools.one_can_be_not_none(room, adress)
        
        location = LocationDao.get_by_id(location_id)
        
        if location is None:
            raise ValueError("Location not found")
        if room == location.room and adress == location.adress:
            raise ValueError("No changes detected")
        
        room = VariableTools.compare_to_empty_str(room, location.room)
        adress = VariableTools.compare_to_empty_str(adress, location.adress)
        
        if LocationDao.get_by_property(room, adress):
            raise ValueError("Location already exists")
        
        LocationDao.update(location_id, room, adress)

            
    @staticmethod
    def create(room: str = None, adress: str = None) -> Location:
        
        VariableTools.one_can_be_not_none(room, adress)
        room = VariableTools.compare_to_empty_str(room, "N/A")
        adress = VariableTools.compare_to_empty_str(adress, "N/A")
        
        if LocationDao.get_by_property(room, adress):
            raise ValueError("Location already exists")
        return LocationDao.create(room, adress)
    
    @staticmethod
    def delete(location_id: int) -> None:
        VariableTools.check_id(location_id, "Location")
        
        location = LocationDao.get_by_id(location_id)
        if location is None:
            raise ValueError("Location not found")
        
        devices = DeviceService.get_by_location(location_id)
        if len(devices) > 0:
            for device in devices:
                DeviceService.delete(device.id)
        LocationDao.delete(location_id)








