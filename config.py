import os

class Config:
    
    username = 'root'
    password = 'root'
    database = 'ajax_pattern'
    
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{username}:{password}@localhost:3306/{database}'
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost/test_bd'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
