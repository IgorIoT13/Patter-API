from app import db
from app.models import User

class UserDao:
    @staticmethod
    def get_all() -> list:
        return User.query.all()
    
    @staticmethod
    def get_by_id(user_id: int) -> User:
        return User.query.get(user_id)
    
    @staticmethod
    def get_by_username(username: str) -> User:
        return User.query.filter_by(username=username).first()
    
    @staticmethod
    def update_data(
        user_id: int,
        username: str = None,
        password: str = None,
        number: str = None
    ) -> User:
        user = UserDao.get_by_id(user_id)
        
        if username is not None:
            user.username = username
        if password is not None:
            user.password = password
        if number is not None:
            user.number = number
        
        db.session.commit()
        return user
    
    @staticmethod
    def create(username: str, password: str, number: str) -> User:
        user = User(
            username=username,
            password=password,
            number=number
        )
        db.session.add(user)
        db.session.commit()
        return user
    
    @staticmethod
    def delete(user_id: int) -> None:
        user = UserDao.get_by_id(user_id)
        db.session.delete(user)
        db.session.commit()