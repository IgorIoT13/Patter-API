from app import db

class DeviceType(db.Model):
    __tablename__ = 'device_types'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

    devices = db.relationship('Device', backref='type', lazy=True)

    def __repr__(self):
        return f'<DeviceType {self.name}>'