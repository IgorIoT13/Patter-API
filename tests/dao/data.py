from app.dao import DeviceDataDao, DeviceDao, LocationDao
from app.models import DeviceData, Device, Location

class Data:
    device_data = {
        "common": {
            "device_id": 1,
            "secure_status": True,
            "temprature": 100,
            "humidity": 11
        },
        "to_delete": {
            "device_id": 1,
            "secure_status": True,
            "temprature": 100,
            "humidity": 11
        },
        "change": {
            "device_id": 1,
            "secure_status": False,
            "temprature": 200,
            "humidity": 22
        }
    }
    
    device = {
       "common": {
           "device_id": 1,
           "location_id": 1,
           "name": "test_device",
           "type": "test_type",
           "topic": "test_topic"
       },
       "to_delete": {
           "device_id": 1,
           "location_id": 1,
           "name": "test_device_to_delete",
           "type": "test_type_to_delete",
           "topic": "test_topic_to_delete"
       },
       "change":{
            "device_id": 1,
            "location_id": 1,
            "name": "test_device_change",
            "type": "test_type_change",
            "topic": "test_topic_change"
       }
    }
    
    location = {
        "common": {
            "room": "test_location",
            "adress": "test_address"
        },
        "to_delete": {
            "room": "test_location_to_delete",
            "adress": "test_address_to_delete"
        },
        "change": {
            "room": "test_location_change",
            "adress": "test_address_change"
        }
    }
    
    @staticmethod
    def get_device_data() -> dict:
       return Data.device_data
   
    @staticmethod
    def get_device() -> dict:
       return Data.device
   
    @staticmethod
    def get_location() -> dict:
       return Data.location
#----------------------------------------------------------------------------------
    @staticmethod
    def create_base_location() -> Location:
        location = LocationDao.create(
            room=Data.location["common"]["room"],
            adress=Data.location["common"]["adress"]
        )
        Data.device["common"]["location_id"] = location.id
        Data.device["change"]["location_id"] = location.id
        Data.device["to_delete"]["location_id"] = location.id
        return location
    
    @staticmethod
    def create_base_device() -> Device:
        device = DeviceDao.create(
            location_id=Data.device["common"]["location_id"],
            name=Data.device["common"]["name"],
            type=Data.device["common"]["type"],
            topic=Data.device["common"]["topic"]
        )
        Data.device_data["common"]["device_id"] = device.id
        Data.device_data["change"]["device_id"] = device.id
        Data.device_data["to_delete"]["device_id"] = device.id
        return device
    
    @staticmethod
    def create_base_device_data() -> DeviceData:
        device_data = DeviceDataDao.create(
            device_id=Data.device_data["common"]["device_id"],
            secure_status=Data.device_data["common"]["secure_status"],
            temprature=Data.device_data["common"]["temprature"],
            humidity=Data.device_data["common"]["humidity"]
        )
        return device_data
    
    @staticmethod
    def create_base_device_structure() -> dict:
        location = Data.create_base_location()
        device = Data.create_base_device()
        device_data = Data.create_base_device_data()
        return {
            "location": location,
            "device": device,
            "device_data": device_data
        }