class Config(object):
    DEBUG = False
    TESTING = False
    MYSQL_DATABASE_USER = 'webserver'
    MYSQL_DATABASE_PASSWORD = 'webserver'
    MYSQL_DATABASE_DB = 'easycontainer' 
    MYSQL_DATABASE_HOST = "mysql"   
    

class PRDConfig(Config):    
    SESSION_COOKIE_SECURE = True

class LOCALConfig(Config):
    DEBUG = True
    
    SESSION_COOKIE_SECURE = False

class UATConfig(Config):
    TESTING = True    
    SESSION_COOKIE_SECURE = False
