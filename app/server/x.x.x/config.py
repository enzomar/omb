class Config(object):
    DEBUG = False
    TESTING = False
    MYSQL_DATABASE_USER = 'webserver'
    MYSQL_DATABASE_PASSWORD = 'webserver'
    MYSQL_DATABASE_DB = 'easycontainer'    
    

class PRDConfig(Config):
    MYSQL_DATABASE_HOST = "10.5.0.2"

    SESSION_COOKIE_SECURE = True

class LOCALConfig(Config):
    DEBUG = True
    MYSQL_DATABASE_HOST = "10.0.0.2"

    SESSION_COOKIE_SECURE = False

class UATConfig(Config):
    TESTING = True
    MYSQL_DATABASE_HOST = "10.1.0.2"

    SESSION_COOKIE_SECURE = False
