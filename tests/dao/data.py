class Data:
    device_data = {
        "withOutSecure": {
            "device_id": 1,
            "secure_status": None,
            "temprature": 100,
            "humidity": 11
        },
        "withOutTemperature": {
            "device_id": 1,
            "secure_status": True,
            "temprature": None,
            "humidity": 11
        },
        "withOutHumidity": {
            "device_id": 1,
            "secure_status": True,
            "temprature": 100,
            "humidity": None
        },
        "withOutTemperatureAndHumidity": {
            "device_id": 1,
            "secure_status": True,
            "temprature": None,
            "humidity": None
        },
        "withOutSecureAndHumidity": {
            "device_id": 1,
            "secure_status": None,
            "temprature": 100,
            "humidity": None
        },
        "withOutSecureAndTemperature": {
            "device_id": 1,
            "secure_status": None,
            "temprature": None,
            "humidity": 11
        },
        "withOutAll": {
            "device_id": 1,
            "secure_status": None,
            "temprature": None,
            "humidity": None
        }
    }
    
    @staticmethod
    def get_device_data() -> dict:
       return Data.device_data
    