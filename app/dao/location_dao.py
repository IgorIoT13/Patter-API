from app import db
from app.models import Location

class LocationDAO:
    
    @staticmethod
    def get_all() -> list:
        return Location.query.all()

    @staticmethod
    def get_by_id(location_id: int) -> Location:
        location = Location.query.get(location_id)
        
        if location is None:
            raise ValueError("Location not found")
        
        return location

    @staticmethod
    def add(room: str, adress: str) -> Location:
        if room is None or "" or " " or adress is None or "" or " " :
            raise ValueError("Room and address cannot be None or empty")
          
        new_location = Location(room=room, adress=adress)
        db.session.add(new_location)
        db.session.commit()
        return new_location

    @staticmethod
    def update_data(location_id: int, room: str, adress: str) -> Location:
        if room is None or "" or " " and adress is None or "" or " " :
            raise ValueError("Room and address cannot be None or empty")
        
        location = LocationDAO.get_location_by_id(location_id)
        
        if location is None:
            raise ValueError("Location not found")

        if room is not None or "" or " ":     
            location.room = room
        if adress is not None or "" or " ":
            location.adress = adress
            
        db.session.commit()
        return location

    @staticmethod
    def delete(location_id: int) -> bool:
        location = LocationDAO.get_location_by_id(location_id)
        
        if location is None:
            raise ValueError("Location not found")
        
        db.session.delete(location)
        db.session.commit()
        return True