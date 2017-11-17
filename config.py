class Config(object):
    pass

class ProdConfig(Config):
    pass

class DevConfig(Config):
    Debug = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:pass123@localhost:3306/blogdb"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
