from app import db
from app.models import Brocker

class BrockerDao:
    @staticmethod
    def get_all() -> list:
        return Brocker.query.all()
    
    @staticmethod
    def get_by_id(broker_server_id: int) -> Brocker:
        return Brocker.query.get(broker_server_id)
    
    @staticmethod
    def update_data(
        broker_server_id: int,
        ip: str = None,
        port: int = None,
        username: str = None,
        password: str = None
    ) -> Brocker:
        broker_server = BrockerDao.get_by_id(broker_server_id)
        
        if ip is not None:
            broker_server.ip = ip
        if port is not None:
            broker_server.port = port
        if username is not None:
            broker_server.username = username
        if password is not None:
            broker_server.password = password
        
        db.session.commit()
        return broker_server
    
    @staticmethod
    def create(ip: str, port: int, username: str, password: str) -> Brocker:
        broker_server = Brocker(
            ip=ip,
            port=port,
            username=username,
            password=password
        )
        db.session.add(broker_server)
        db.session.commit()
        return broker_server
    
    @staticmethod
    def delete(broker_server_id: int) -> None:
        broker_server = BrockerDao.get_by_id(broker_server_id)
        db.session.delete(broker_server)
        db.session.commit()