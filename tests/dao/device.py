from app.dao import DeviceDao
from app.models import Device

class DeviceTest:
    @staticmethod
    def create_test() -> Device:
        pass
    
    @staticmethod
    def search_test(device: Device) -> None:
        pass
    
    @staticmethod
    def update_test(device: Device) -> None:
        pass
    
    @staticmethod
    def delete_test(device: Device) -> None:
        pass
    
    @staticmethod
    def tests():
        obj = DeviceTest.create_test()
        assert obj is not None