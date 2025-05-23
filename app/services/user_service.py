from app.models import User
from app.dao import UserDao

class UserService:
    
    @staticmethod
    def get_all() -> list:
        return UserDao.get_all()
    
    @staticmethod
    def get_by_id(user_id: int) -> User:
        if user_id is None:
            raise ValueError("User ID cannot be None")
        if user_id < 1:
            raise ValueError("User ID must be greater than 0")
        return UserDao.get_by_id(user_id)
    
    @staticmethod
    def get_by_property(username: str = None, number: str = None) -> list:
        data = UserService.get_all()
        if username and number:
            return [user for user in data if user.username == username and user.number == number]
        elif username:
            return [user for user in data if user.username == username]
        elif number:
            return [user for user in data if user.number == number]
        else:
            return data
        
    @staticmethod
    def create(username: str, password: str, number: str) -> User:
        if username is None or password is None or number is None:
            raise ValueError("Username, password and number cannot be None")
        if UserService.get_by_property(username=username, number=number):
            raise ValueError("User with this username or number already exists")
        
        user = UserDao.create(username=username, password=password, number=number)
        return user
        
    @staticmethod
    def update(user_id: int, username: str = None, password: str = None, number: str = None) -> None:
        if user_id is None:
            raise ValueError("User ID cannot be None")
        if user_id < 1:
            raise ValueError("User ID must be greater than 0")
        if username is None and password is None and number is None:
            raise ValueError("At least one of username, password or number must be provided")
        
        user = UserService.get_by_id(user_id)
        
        ready_user_name = username if username is not None else user.username
        ready_user_password = password if password is not None else user.password
        ready_user_number = number if number is not None else user.number
        
        if UserService.get_by_property(username=ready_user_name, number=ready_user_number):
            raise ValueError("User with this username or number already exists")
        
        UserDao.update(user_id=user_id, username=ready_user_name, password=ready_user_password, number=ready_user_number)

    @staticmethod
    def delete(user_id: int) -> None:
        if user_id is None:
            raise ValueError("User ID cannot be None")
        if user_id < 1:
            raise ValueError("User ID must be greater than 0")
        
        data = UserService.get_by_id(user_id)
        if not data:
            raise ValueError("User with this ID does not exist")
        
        # Check if the user exists
        UserDao.delete(user_id)
        