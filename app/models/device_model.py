from app import db

class Device(db.Model):
    __tablename__ = 'devices'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    type_id = db.Column(db.Integer, db.ForeignKey('device_types.id'), nullable=False)

    def __repr__(self):
        return f'<Device {self.name}>'