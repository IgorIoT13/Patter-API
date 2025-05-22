from app import db
from app.models import Location

class LocationDao:
    
    @staticmethod
    def get_all() -> list:
        return Location.query.all()

    @staticmethod
    def get_by_id(location_id: int) -> Location:
        location = Location.query.get(location_id)
        return location

    @staticmethod
    def create(room: str, adress: str) -> Location:
        new_location = Location(room=room, adress=adress)
        db.session.add(new_location)
        db.session.commit()
        return new_location

    @staticmethod
    def update(location_id: int, room: str, adress: str) -> Location:
        location = LocationDao.get_by_id(location_id)
        if room is not None or "" or " ":     
            location.room = room
        if adress is not None or "" or " ":
            location.adress = adress
            
        db.session.commit()
        return location
    
    @staticmethod
    def get_by_property(room: str, adress: str) -> Location:
        location = Location.query.filter_by(room=room, adress=adress).first()
        return location
        

    @staticmethod
    def delete(location_id: int) -> bool:
        location = LocationDao.get_location_by_id(location_id)
        db.session.delete(location)
        db.session.commit()
        return True