from app import db

class DeviceData(db.Model):
    __tablename__ = 'device_data'

    id = db.Column(db.Integer, primary_key=True)
    secure_status = db.Column(db.Boolean, nullable=False, default=False)
    temprature = db.Column(db.Float, nullable=False)
    humidity = db.Column(db.Float, nullable=False)
    time = db.Column(db.DateTime, nullable=False)
    # device_id = db.Column(db.Integer, db.ForeignKey('devices.id'), nullable=False)
    # timestamp = db.Column(db.DateTime, nullable=False)
    # value = db.Column(db.Float, nullable=False)

    # device = db.relationship('Device', backref='data', lazy=True)

    def __repr__(self):
        return f'<DeviceData {self.device_id} {self.timestamp} {self.value}>'