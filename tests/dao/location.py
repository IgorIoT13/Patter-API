from app.dao import LocationDao
from app.models import Location

class LocationTest:
    @staticmethod
    def create_test() -> Location:
        pass
    
    @staticmethod
    def search_test(device: Location) -> None:
        pass
    
    @staticmethod
    def update_test(device: Location) -> None:
        pass
    
    @staticmethod
    def delete_test(device: Location) -> None:
        pass
    
    @staticmethod
    def tests():
        obj = LocationTest.create_test()
        assert obj is not None