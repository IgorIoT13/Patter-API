from app.dao import UserDao
from app.models import User
from .data import Data

class UserTest:
    @staticmethod
    def create_test() -> User:
        pass
    
    @staticmethod
    def search_test(user: User) -> None:
        pass
    
    @staticmethod
    def update_test(user: User) -> None:
        pass
    
    @staticmethod
    def delete_test(user: User) -> None:
        pass
    
    @staticmethod
    def tests():
        obj = UserTest.create_test()
        assert obj is not None