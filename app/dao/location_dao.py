from app import db
from app.models import Location

class LocationDAO:
    
    @staticmethod
    def get_all():
        return Location.query.all()

    @staticmethod
    def get_by_id(location_id):
        location = Location.query.get(location_id)
        if location is None:
            raise ValueError("Location not found")
        return location

    @staticmethod
    def add(room, adress):
        if room is None or adress is None:
            raise ValueError("Room and address cannot be None")
        new_location = Location(room=room, adress=adress)
        db.session.add(new_location)
        db.session.commit()
        return new_location

    @staticmethod
    def update_data(location_id, room, adress):
        location = LocationDAO.get_location_by_id(location_id)
        if location is None:
            raise ValueError("Location not found")
        if room is None or adress is None:
            raise ValueError("Room and address cannot be None")
        if location:
            location.room = room
            location.adress = adress
            db.session.commit()
            return location
        return None

    @staticmethod
    def delete(location_id):
        """Delete a location from the database."""
        location = LocationDAO.get_location_by_id(location_id)
        if location is None:
            raise ValueError("Location not found")
        if location:
            db.session.delete(location)
            db.session.commit()
            return True
        return False