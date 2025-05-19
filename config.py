import os

class Config:
    
    username = 'root'
    password = 'root'
    database = 'test_bd'
    
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{username}:{password}@localhost/{database}'
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost/test_bd'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
